from django.db import models


# Create your models here.

# ORM，对数据库的操作

class testNews(models.Model):
    Title = models.CharField("title", primary_key=True, max_length=100)
    url = models.CharField('url', primary_key=False, max_length=255)
    # createTime = models.CharField('createTime', primary_key=False, max_length=255)
    # editor = models.CharField('editor', primary_key=False, max_length=500)
    # digest = models.CharField('digest', primary_key=False, max_length=1000)

# 新增数据
# testNews.objects.create(Title="")

class TestScrapy(models.Model):
    text= models.CharField(max_length=255)
    author= models.CharField(max_length=255)

    class Meta:
        app_label = 'RuralPro'
        db_table = 'test_scrapy'
