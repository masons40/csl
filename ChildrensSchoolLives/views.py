from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html", generateBaseInfo())
	
def NewsAndPublications(request):
	infoDictionary = generateBaseInfo()
	infoDictionary["news_articles"] = NewsArticle.objects.all
	return render(request, "NewsAndPublications.html", infoDictionary)
	
def About(request):
	infoDictionary  = generateBaseInfo()
	return render(request, "About.html", infoDictionary)

def InformationforParticipants(request):
	return render(request, "InformationforParticipants.html", generateBaseInfo())

def InformationforResearchers(request):
	infoDictionary = generateBaseInfo()
	infoDictionary["schools_in_munster"] = NumberofSchoolsInMunster.objects.first()
	infoDictionary["schools_in_leinster"] = NumberofSchoolsInLeinster.objects.first()
	infoDictionary["schools_in_ulster"] = NumberofSchoolsInUlster.objects.first()
	infoDictionary["schools_in_connacht"] = NumberofSchoolsInConnacht.objects.first()
	return render(request, "InformationforResearchers.html", infoDictionary)

def PV(request):
	infoDictionary = generateBaseInfo()
	employees = Employee.objects.all
	infoDictionary["Employess"] = employees
	infoDictionary["jobposts"] = jobPost.objects.all
	return render(request, "PeopleAndVacancies.html", infoDictionary)



def generateBaseInfo():
	email_address = WebsiteEmailAddress.objects.all
	phone_number = WebsitePhoneNumber.objects.all

	return {"email_address" : email_address, "phone_numbers":phone_number}