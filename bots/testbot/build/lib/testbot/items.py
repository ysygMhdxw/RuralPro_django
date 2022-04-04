import scrapy
from scrapy_djangoitem import DjangoItem
from RuralPro.models import TestScrapy

class TestbotItem(DjangoItem):
    django_model = TestScrapy