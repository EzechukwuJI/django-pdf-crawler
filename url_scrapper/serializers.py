from url_scrapper.models import UploadedFile, WebUrl
from rest_framework import serializers




class UploadedFileSerializer(serializers.ModelSerializer):
	total_urls    =     serializers.IntegerField(read_only = True)
	class Meta:
		model = UploadedFile
		fields  =  ('id', 'filename', 'total_urls')


class WebUrlSerializer(serializers.ModelSerializer):
	doc_count =  serializers.IntegerField(read_only = True)
	class Meta:
		model = WebUrl
		fields = ('id', 'url_string','is_live', 'doc_count')