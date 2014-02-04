from django.conf.urls import pattern, include, url
from website.views import index

urlpatterns = patterns('',
    url(r'^$', index, name = 'index'),
)
