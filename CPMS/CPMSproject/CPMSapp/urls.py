from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.cpms_main, name='not_login'),
    path('login/', views.cpms_login, name='trying_login'),
    path('login/signup/', views.cpms_signup, name='trying_signup'),
    path('login_success/<str:user_name>/', views.cpms_main_login, name='login_of_user_name'),
<<<<<<< HEAD
<<<<<<< HEAD
=======
    path('login_success/<str:user_name>/ticket/', views.cpms_ticket),
    path('login_success/<str:user_name>/createticket/', views.cpms_create_ticket),
    path('login_success/<str:user_name>/ticket/ticketdetails/', views.cpms_ticket_details),
>>>>>>> 708934baab6a3b5f32aaf5fca91b7b60848011c9
=======
    path('login_success/<str:user_name>/ticket/', views.cpms_ticket),
    path('login_success/<str:user_name>/createticket/', views.cpms_create_ticket),
    path('login_success/<str:user_name>/ticket/ticketdetails/', views.cpms_ticket_details),
>>>>>>> 708934baab6a3b5f32aaf5fca91b7b60848011c9
]