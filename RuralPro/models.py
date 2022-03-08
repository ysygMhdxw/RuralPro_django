from django.db import models


# Create your models here.

class platform(models.Model):
    Webname = models.CharField("Webname", primary_key=True, max_length=100)
    url = models.CharField('url', primary_key=False, max_length=255)
    pic = models.CharField('pic', primary_key=False, max_length=255)
    introduction = models.CharField('introduction', primary_key=False, max_length=500)
    type = models.CharField('type', primary_key=False, max_length=50)
