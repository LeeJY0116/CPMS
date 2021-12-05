from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.cpms_main, name='not_login'),
    path('login/', views.cpms_login),
    path('<str:user_name>/', views.cpms_main_login)
]