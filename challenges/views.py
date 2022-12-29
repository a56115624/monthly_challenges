from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def challenges_month(request, month):
    challenges_test = None
    if month == "january":
        challenges_test = "Eat no meat for the entire month!"
    elif month == "February":
        challenges_test = "walk for at least 20 minutes every day"
    elif month == "march":
        challenges_test = "Learn Django"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenges_test)
