from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^places/', views.PlaceList, name='placeList'),
    url(r'^placecreate/$', csrf_exempt(views.PlaceCreate), name='placeCreate'),
]