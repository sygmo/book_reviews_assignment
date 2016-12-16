from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^books$', views.index, name='bookreviews-index'),
	url(r'^add$', views.index, name='add-book'),
	url(r'^books/(?P<id>\d+)$', views.index, name='book-info'),
]