from django.conf.urls import url

from . import views
app_name = 'booking'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view_rooms$', views.view_rooms, name='view_rooms'),
]