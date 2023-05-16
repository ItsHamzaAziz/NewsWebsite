from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TopNews(models.Model):
    news_photo = models.FileField(upload_to='TopNews/', max_length=250, null=True, default=None)
    news_heading = models.CharField(max_length=150)
    news_subheading = models.CharField(max_length=400)
    news_content = HTMLField()
    news_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_heading)

class PakistanNews(models.Model):
    news_photo = models.FileField(upload_to='PakistanNews/', max_length=250, null=True, default=None)
    news_heading = models.CharField(max_length=150)
    news_subheading = models.CharField(max_length=400)
    news_content = HTMLField()
    news_city = models.CharField(max_length=50)
    news_province = models.CharField(max_length=60)
    news_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.news_heading)

class WorldNews(models.Model):
    news_photo = models.FileField(upload_to='WorldNews/', max_length=250, null=True, default=None)
    news_heading = models.CharField(max_length=150)
    news_subheading = models.CharField(max_length=400)
    news_content = HTMLField()
    news_country = models.CharField(max_length=100)
    news_continent = models.CharField(max_length=60)
    news_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_heading)

class BusinessNews(models.Model):
    news_photo = models.FileField(upload_to='BusinessNews/', max_length=250, null=True, default=None)
    news_heading = models.CharField(max_length=150)
    news_subheading = models.CharField(max_length=400)
    news_content = HTMLField()
    news_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_heading)

class SportsNews(models.Model):
    news_photo = models.FileField(upload_to='SportsNews/', max_length=250, null=True, default=None)
    news_heading = models.CharField(max_length=150)
    news_subheading = models.CharField(max_length=400)
    news_content = HTMLField()
    news_category = models.CharField(max_length=50)
    news_at = models.DateTimeField(auto_now_add=True)

    # String to be displayed in admin panel
    def __str__(self):
        return str(self.news_heading)
    
