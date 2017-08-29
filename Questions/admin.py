from django.contrib import admin
from .models import AskedQuestions, Replies, Vote
# Register your models here.



admin.site.register(AskedQuestions)
admin.site.register(Replies)
admin.site.register(Vote)