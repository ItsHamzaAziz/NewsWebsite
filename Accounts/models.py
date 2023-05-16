from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # Only one user has relationship to corresponding defualt user.
    user_country = models.CharField(max_length=300)     # Extra field

    # String to be displayed in admin panel
    def __str__(self):
        return str(self.user)
