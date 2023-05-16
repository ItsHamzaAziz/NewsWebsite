from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Opinion(models.Model):
    opinion_photo = models.FileField(upload_to='Opinion/', max_length=250, null=True, default=None)
    opinion_heading = models.CharField(max_length=300)
    opinion_content = HTMLField()
    writer = models.CharField(max_length=100)
    writer_description = models.CharField(max_length=500, default=None)
    written_at = models.DateTimeField(auto_now_add=True)

    # String to be displayed in admin panel
    def __str__(self):
        return str(self.opinion_heading)
    