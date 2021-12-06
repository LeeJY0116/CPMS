from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.cpms_main, name='not_login'),
    path('login/', views.cpms_login, name='trying_login'),
    path('login/signup/', views.cpms_signup),
    path('login_success/<str:user_name>/', views.cpms_main_login, name='login_of_user_name'),
]