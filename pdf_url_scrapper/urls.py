
from django.conf.urls import url, include
from django.contrib import admin



# class 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('url_scrapper.urls', namespace = "url_scrapper")),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
]
