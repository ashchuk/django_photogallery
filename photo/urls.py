from django.conf import settings

__author__ = 'ashchuk'

from django.conf.urls import patterns, url
from photo import views
urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^category/(?P<pk>\d+)$', views.AlbumsView.as_view(), name='category'),
    url(r'^albums/(?P<pk>\d+)$', views.PhotoView.as_view(), name='albums'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^error/$', views.error, name='error'),
    url(r'^feedback/$', views.feedback, name='feedback'),
)