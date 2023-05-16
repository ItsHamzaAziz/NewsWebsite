from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from ContactUs.views import contact_us

# Create your views here.
def index(request):
    news_object = TopNews.objects.all().order_by('-id')     # Sorting objects in reverse order so that latest comes at top

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    # Using first three objects as in home page only top three news will be shown
    data = {
        'news_object_one' : news_object[0],
        'news_object_two' : news_object[1],
        'news_object_three' : news_object[2],
        'title' : 'TheNewsPro'      # Title on home page
    }

    return render(request, 'News/TopNews/HomePage.html', data)

def top_news_detail(request, top_news_id):
    news_object = TopNews.objects.get(id=top_news_id)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data = {
        'news_object':news_object,
        'title':news_object.news_heading
    }

    return render(request, 'News/TopNews/TopNewsDetail.html', data)

def pakistan_news(request):
    news_objects = PakistanNews.objects.all().order_by('-id')   # Sorting the objects in reverse order so get latest on top

    # Displaying maximum 8 news per page
    p = Paginator(news_objects, 8)
    page_num = request.GET.get('page')
    final_data = p.get_page(page_num)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data = {
        'news_objects' : news_objects,
        'title' : 'Pakistan - TheNewsPro',
        'final_data' : final_data
    }

    return render(request, 'News/PakistanNews/PakistanNews.html', data)

def pakistan_news_detail(request, pakistan_news_id):
    news_object = PakistanNews.objects.get(id=pakistan_news_id)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data  = {
        'news_object' : news_object,
        'title' : news_object.news_heading
    }

    return render(request, 'News/PakistanNews/PakistanNewsDetail.html', data)

def world_news(request):
    news_objects = WorldNews.objects.all().order_by('-id')   # Sorting the objects in reverse order so get latest on top

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    # Displaying maximum 8 news per page
    p = Paginator(news_objects, 8)
    page_num = request.GET.get('page')
    final_data = p.get_page(page_num)
    
    data = {
        'news_objects' : news_objects,
        'title' : 'World - TheNewsPro',
        'final_data' : final_data
    }

    return render(request, 'News/WorldNews/WorldNews.html', data)

def world_news_detail(request, world_news_id):
    news_object = WorldNews.objects.get(id=world_news_id)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data  = {
        'news_object' : news_object,
        'title' : news_object.news_heading
    }

    return render(request, 'News/WorldNews/WorldNewsDetail.html', data)

def business_news(request):
    news_objects = BusinessNews.objects.all().order_by('-id')    # Sorting the objects in reverse order so get latest on top

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    # Displaying maximum 8 news per page
    p = Paginator(news_objects, 8)
    page_num = request.GET.get('page')
    final_data = p.get_page(page_num)
    
    data = {
        'news_objects' : news_objects,
        'title' : 'Business - TheNewsPro',
        'final_data' : final_data
    }

    return render(request, 'News/BusinessNews/BusinessNews.html', data)

def business_news_detail(request, business_news_id):
    news_object = BusinessNews.objects.get(id=business_news_id)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data  = {
        'news_object' : news_object,
        'title' : news_object.news_heading
    }

    return render(request, 'News/BusinessNews/BusinessNewsDetail.html', data)

def sports_news(request):
    news_objects = SportsNews.objects.all().order_by('-id')      # Sorting the objects in reverse order so get latest on top

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    # Displaying maximum 8 news per page
    p = Paginator(news_objects, 8)
    page_num = request.GET.get('page')
    final_data = p.get_page(page_num)
    
    data = {
        'news_objects' : news_objects,
        'title' : "Sports - TheNewsPro",
        'final_data' : final_data
    }

    return render(request, 'News/SportsNews/SportsNews.html', data)

def sports_news_detail(request, sports_news_id):
    news_object = SportsNews.objects.get(id=sports_news_id)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data  = {
        'news_object' : news_object,
        'title' : news_object.news_heading
    }

    return render(request, 'News/SportsNews/SportsNewsDetail.html', data)
