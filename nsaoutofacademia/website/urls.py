from django.conf.urls import pattern, include, url
from website.views import universities

urlpatterns = patterns('',
    url(r'^$', universities, name = 'universities'),
)
