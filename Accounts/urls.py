from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.sign_user_up, name='signup'),
    path('login', views.log_user_in, name='login'),
    path('logout', views.log_user_out, name='logout'),
]
