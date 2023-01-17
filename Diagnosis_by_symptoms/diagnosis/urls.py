from django.urls import path

from . import views

app_name = 'diagnosis'
urlpatterns = [
    path('', views.index, name='index'),
]