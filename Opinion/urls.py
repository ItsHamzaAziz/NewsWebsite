from django.urls import path
from . import views

urlpatterns = [
    path('', views.opinion_page, name='opinion'),
    path('<opinion_id>', views.complete_opinion, name='complete_opinion'),
    path('<opinion_id>/login', views.login_user_opinion, name='login_opinion'),
]