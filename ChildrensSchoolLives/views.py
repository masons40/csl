from django.shortcuts import render
from .models import Employee

# Create your views here.


def index(request):
    return render(request, "index.html", )
	
def NewsAndPublications(request):
	return render(request, "NewsAndPublications.html", {})
	
def About(request):
	employees = Employee.objects.all
	return render(request, "About.html", {"Employees":employees})

def InformationforParticipants(request):
	return render(request, "InformationforParticipants.html", {})

def InformationforResearchers(request):
	return render(request, "InformationforResearchers.html", {})

def PV(request):
	return render(request, "PeopleAndVacancies.html", {})
