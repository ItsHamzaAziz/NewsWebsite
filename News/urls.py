from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('topnews/<top_news_id>', views.top_news_detail, name='top_news_detail'),

    path('pakistan/', views.pakistan_news, name='pakistan'),
    path('pakistan/<pakistan_news_id>', views.pakistan_news_detail, name='pakistan_news_detail'),

    path('world/', views.world_news, name='world'),
    path('world/<world_news_id>', views.world_news_detail, name='world_news_detail'),

    path('business/', views.business_news, name='business'),
    path('business/<business_news_id>', views.business_news_detail, name='business_news_detail'),

    path('sports/', views.sports_news, name='sports'),
    path('sports/<sports_news_id>', views.sports_news_detail, name='sports_news_detail'),

]
