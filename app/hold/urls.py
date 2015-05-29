from django.conf.urls import patterns, url

from app.hold import views

urlpatterns = patterns('',
    url(r'index/$', views.index, name='index'),
    url(r'detail/(?P<fund_id>\d+)/$', views.detail, name='detail'),
    url(r'get_hold/(?P<fund_id>\d+)/$', views.get_hold, name='get_hold'),
)
