from django.conf.urls import patterns, include, url
from website.views import universities

urlpatterns = patterns('',
    url(r'^$', universities, name = 'universities'),
)
