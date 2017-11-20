# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


# Create your models here.

class UploadedFile(models.Model):
	filename            =     models.CharField(max_length = 200)
	slug                =     models.SlugField(max_length  =  250)
	date_scrapped       =     models.DateTimeField(auto_now = True)
	


	def save(self, *args, **kwargs):
		self.slug = slugify(self.filename)
		super(UploadedFile,self).save(*args, **kwargs)


	def get_urls(self):
		return self.web_url.all()

	def __unicode__(self):
		return self.filename




class WebUrl(models.Model):
	file_attached         =     models.ForeignKey(UploadedFile, related_name="web_url", null=True)
	url_string            =     models.URLField(max_length = 350)
	http_response_status  =     models.CharField(max_length = 50)
	is_live               =     models.BooleanField(default = True)


	def __unicode__(self):
		return '{} - {}'.format(self.url_string, self.http_response_status)


class TemporaryFile(models.Model):
	file         =   models.FileField(upload_to= "file/pdf")
	related_to   =   models.ForeignKey(UploadedFile, related_name="temporary_file")

