
from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SOCIALMEDIA_CHOICES = (
        ('Ld', 'Linkedin'),
        ('Fb', 'Facebook'),
        ('Tw', 'Twitter'),
    )
    phone_number = models.IntegerField()
    email = models.EmailField()
    social_media_Type = models.CharField(max_length=150, choices=SOCIALMEDIA_CHOICES)
    social_media_Link = models.CharField(max_length=250)
    job_title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="employees")