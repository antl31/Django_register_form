from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new_post, name='new_post'),
]