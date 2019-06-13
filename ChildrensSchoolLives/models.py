
from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # SOCIALMEDIA_CHOICES = (
    #     ('Ld', 'Linkedin'),
    #     ('Fb', 'Facebook'),
    #     ('Tw', 'Twitter'),
    # )
    phone_number = models.IntegerField()
    email = models.EmailField()
    # social_media_Type = models.CharField(max_length=150, choices=SOCIALMEDIA_CHOICES)
    # social_media_Link = models.CharField(max_length=250)
    job_title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="employees")
    employee_about_area = models.TextField()

class WebsitePhoneNumber(models.Model):
    phone_number = models.CharField(max_length=50)

class WebsiteEmailAddress(models.Model):
    email_address = models.EmailField()


class NewsArticle(models.Model):
    title = models.CharField(max_length=400)
    news_article_company = models.CharField(max_length=400)
    news_article_url = models.URLField(max_length=500)


class NumberofSchoolsInConnacht(models.Model):
    no_of_schools = models.IntegerField()

class NumberofSchoolsInMunster(models.Model):
    no_of_schools = models.IntegerField()

class NumberofSchoolsInLeinster(models.Model):
    no_of_schools = models.IntegerField()

class NumberofSchoolsInUlster(models.Model):
    no_of_schools = models.IntegerField()


class jobPost(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    data_post_expires = models.DateField()
    about = models.TextField()
    requirements = models.TextField()
    aboutChangeKey = str(models.AutoField(primary_key=True))+'about'
    requirementsChangeKey = str(models.AutoField(primary_key=True))+'requirements'