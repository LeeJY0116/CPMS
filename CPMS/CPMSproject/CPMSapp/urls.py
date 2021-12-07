from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.cpms_main, name='not_login'),
    path('login/', views.cpms_login, name='trying_login'),
    path('login/signup/', views.cpms_signup, name='trying_signup'),
    path('login_success/<str:user_name>/', views.cpms_main_login, name='login_of_user_name'),
    path('login_success/<str:user_name>/ticket/', views.cpms_ticket, name='myticket'),
    path('login_success/<str:user_name>/createticket/', views.cpms_create_ticket, name='create_ticket'),
    path('login_success/<str:user_name>/ticket/ticketdetails=<str:ticket_code>/', views.cpms_ticket_details),
]