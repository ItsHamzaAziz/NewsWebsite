from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from ContactUs.views import contact_us
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def opinion_page(request):
    opinion_objects = Opinion.objects.all().order_by('-id')     # Sorting the objects in reverse order so get latest on top

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    # Displaying maximum 8 opinions per page
    p = Paginator(opinion_objects, 8)
    page_num = request.GET.get('page')
    final_data = p.get_page(page_num)
    
    data = {
        'opinion_objects' : opinion_objects,
        'title' : "Opinion - TheNewsPro",
        'final_data' : final_data,
    }

    return render(request, 'Opinion/Opinion.html', data)

def complete_opinion(request, opinion_id):
    opinion_object = Opinion.objects.get(id=opinion_id)

    # Importing contact_us function from views file in ContactUs app, so that we can use it again and again
    contact_us(request)

    data  = {
        'opinion_object' : opinion_object,
        'title' : opinion_object.opinion_heading
    }

    return render(request, 'Opinion/CompleteOpinion.html', data)

def login_user_opinion(request, opinion_id):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # If username or password is incorrect, authenticate function returns None
        if user is not None:
            login(request, user)        # Logging user in
            return redirect('complete_opinion', opinion_id=opinion_id)     # Redirecting to home page
        else:
            messages.info(request, 'Invalid Info.')
            return redirect('login')        # Redirecting to login page so that correct information can be entered

    data = {
        'title' : 'Login - TheNewsPro',     # Title of Login Page
    }

    return render(request, 'Accounts/Login.html', data)
