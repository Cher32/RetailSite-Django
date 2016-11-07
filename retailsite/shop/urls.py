from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^products/$', views.products, name='Products'),
	url(r'^contact/$', views.contact, name='Contact'),
	url(r'^signin/$', views.signin, name='Signin'),
]