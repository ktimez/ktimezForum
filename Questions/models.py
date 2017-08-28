from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from .utils import unique_slug_generator
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from django.conf import settings


class AskedQuestions(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text='tanga ubundi busobanuro burenzeho ku kibazo, niba ubufite', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=AskedQuestions)


class Replies(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    ques = models.ForeignKey(AskedQuestions)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)

    def disaprove(self):
        self.approved = False
        self.save()

    def __str__(self):
        return self.text