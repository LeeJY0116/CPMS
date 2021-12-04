from django.urls import path
from . import views

urlpatterns = [
    path('', views.cpms_main),
    path('login/', views.cpms_login),
]