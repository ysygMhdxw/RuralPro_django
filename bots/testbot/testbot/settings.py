# Scrapy settings for testbot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# # scrapy项目的settings.py文件中加入下面内容
import os
import sys
#
# # DJANGO INTEGRATION
# # E:\code\django_scrapy\extra_apps\mySpider\mySpider/set
# # 注意这个路径修改成自己的Django项目所在的路径
sys.path.append('C:/Users/86188/PycharmProjects/RuralPro/djangoProject')
sys.path.append('C:/Users/86188/PycharmProjects/RuralPro/djangoProject/bots')
# # Do not forget the change Crawler part based on your mySpider name
# # 下面这行的django_scrapy修改为自己的Django项目名字
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject.settings'
# # import os,sys
# # root_path = os.path.abspath(__file__)
# # root_path = '/'.join(root_path.split('/')[:-2])
# # sys.path.append(root_path)
# from bots import init
# init.setup_django_env()
# This is required only if Django Version > 1.8
import django

django.setup()

# DJANGO INTEGRATION
BOT_NAME = 'testbot'

SPIDER_MODULES = ['testbot.spiders']
NEWSPIDER_MODULE = 'testbot.spiders'

DOWNLOAD_HANDLERS = {'s3': None}
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 100

CONCURRENT_REQUESTS_PER_IP=1

ITEM_PIPELINES = {
    'testbot.pipelines.TestbotPipeline': 1,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'testbot (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'testbot.middlewares.TestbotSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'testbot.middlewares.TestbotDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'testbot.pipelines.TestbotPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
