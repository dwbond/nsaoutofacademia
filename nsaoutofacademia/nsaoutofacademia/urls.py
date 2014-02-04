from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
from nsaoutofacademia.views import about
    
urlpatterns = patterns('',
    # base urls
    url(r'^about/$', about, name = 'about'),

    # app sub-urls
    url(r'nsaout/', include('website.urls')),

    # admin interface
    url(r'^admin/', include(admin.site.urls)),
)
