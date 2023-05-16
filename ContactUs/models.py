from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_us_email = models.CharField(max_length=500)
    contact_us_message = models.TextField()
    
    # String to be displayed in admin panel
    def __str__(self):
        return str(self.contact_us_email)
