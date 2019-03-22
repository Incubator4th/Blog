from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager


# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,null=False)
    mod_date = models.DateTimeField('Create_Time',default=timezone.now)
    content = MDTextField()
    tags = TaggableManager(blank=True)


