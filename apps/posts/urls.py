from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^post$', views.post),
	url(r'^delete/(?P<note_id>\d+)$', views.delete),
	url(r'^edit/(?P<note_id>\d+)$', views.edit),
	url(r'^save/(?P<note_id>\d+)$', views.save)
]