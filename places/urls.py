from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('park/', views.park, name='park'),
    path('school/', views.school, name='school'),
    path('church/', views.church, name='church'),
    path('turf/', views.turf, name='turf'),
    path('apartments/', views.apartments, name='apartments'),
]
