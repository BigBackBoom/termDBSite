from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tinymce/', include('tinymce.urls')),
]
