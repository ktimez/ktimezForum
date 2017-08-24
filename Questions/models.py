from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from .utils import unique_slug_generator
#from django.utils.text import slugify
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# Create your models here.


class AskedQuestions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(help_text='tanga ubundi busobanuro burenzeho ku kibazo, niba ubufite', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    #slug = AutoSlugField(populate_from='title',default=None)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=AskedQuestions)


class Replies(models.Model):
    ques = models.ForeignKey(AskedQuestions)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)

    def disaprove(self):
        self.approved = False
        self.save()

    def __str__(self):
        return self.text