from django.db import models
from .. import settings
import os

class PersonalInfo(models.Model):
    blurb = models.CharField(max_length=140)
    name  = models.CharField(max_length=30)
    link  = models.URLField()
    profilePic = models.ImageField(upload_to = 'PathBreakers', default = 'media/PathBreakers/Default.png')

    class Meta:
        abstract = True
