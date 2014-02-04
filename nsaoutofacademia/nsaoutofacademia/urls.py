from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from nsaoutofacademia.views import index, about
    
urlpatterns = patterns('',
    # base urls
    url(r'^$', index, name = 'index'),
    url(r'^about/$', about, name = 'about'),

    # app sub-urls
    url(r'universities/$', include('website.urls')),

    # admin interface
    url(r'^admin/', include(admin.site.urls)),
)
