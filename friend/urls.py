from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('tpd/', views.tpd, name='tpd'),

]
