# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db.models import Sum, Count

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from url_scrapper.models import WebUrl, UploadedFile
from url_scrapper.utils import extract_urls_from_pdf, ext_type_is_valid, check_url_status

from rest_framework import viewsets, generics
from url_scrapper.serializers import WebUrlSerializer, UploadedFileSerializer
import json





def parseFileView(request):
	context = {}
	if request.method == "POST":
		if ext_type_is_valid(request.FILES['pdf_file'].name, 'pdf'):
			# create new Uploaded file object
			file_obj, is_created = UploadedFile.objects.get_or_create(filename = request.FILES['pdf_file'].name)
			if is_created:
				url_list = extract_urls_from_pdf('/home/hypermatrix/Desktop/django rest.pdf') 
				for url in url_list:
					is_live, status_code = check_url_status(url)
					url_obj = WebUrl.objects.create(url_string = url,http_response_status = status_code, is_live = is_live, file_attached = file_obj)
				context['url_list'] = url_list
			else:
				context['url_list'] = file_obj.get_urls()
				messages.info(request, "This file has been parsed")
		else:
			messages.info(request, "Only pdf files are allowed")	
	return render(request, 'url_scrapper/index.html', context)




class DisplayParsedFile(generics.ListCreateAPIView):
	queryset = UploadedFile.objects.all().distinct()
	serializer_class = UploadedFileSerializer


	def get_queryset(self):
		return self.queryset.annotate(total_urls = Count('web_url'))

	
	
class FetchAllUrls(generics.ListCreateAPIView):
	queryset = WebUrl.objects.all().select_related().distinct()
	serializer_class  =  WebUrlSerializer

	def get_queryset(self):
		return self.queryset.annotate(doc_count = Count('file_attached'))


	
class FetchDocUrls(generics.ListCreateAPIView):
	serializer_class  =  WebUrlSerializer

	def get_queryset(self):
		queryset = UploadedFile.objects.get(slug = self.kwargs['doc_name_slug'])
		return queryset.web_url.all().distinct()
		
		
		




