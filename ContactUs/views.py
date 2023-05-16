from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .models import Contact

# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        contact_us_email = request.POST['contact_us_email']
        contact_us_message = request.POST['contact_us_message']

        contact = Contact(contact_us_email=contact_us_email, contact_us_message=contact_us_message)
        contact.save()      # Saving user email and the message left

