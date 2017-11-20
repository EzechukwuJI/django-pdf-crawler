from django.conf.urls import url, include

from url_scrapper import views

from rest_framework import routers


router = routers.DefaultRouter()

# router.register(r'parsed-files', views.DisplayParsedFile)
# router.register(r'url-in-files', views.DisplayUrlsInFile)

urlpatterns = [
	url(r'^upload/$', views.parseFileView, name = "parse-file"),
	url(r'^fetch-uploaded-documents/(?P<output_type>[-\w]+)/$', views.DisplayParsedFile.as_view(), name='fetch-parsed-file'),
	url(r'^fetch-doc-urls/(?P<doc_name_slug>[-\w]+)/$', views.FetchDocUrls.as_view(), name="fetch-doc-urls"),
	url(r'^fetch-all-urls/$', views.FetchAllUrls.as_view(), name = 'fetch-all-urls'),
]

