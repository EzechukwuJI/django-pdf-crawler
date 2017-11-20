# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from url_scrapper.models import WebUrl, UploadedFile, TemporaryFile

# Register your models here.



admin.site.register(WebUrl)
admin.site.register(UploadedFile)
admin.site.register(TemporaryFile)