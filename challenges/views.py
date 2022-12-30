from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "walk for at least 20 minutes every day",
    "march": "Learn Django",
    "april": "Learn English",
    "may": "Learn Chinese",
    "june": "Eat dinner",
    "july": "Play ball",
    "August": "GO swimming",
    "September": "Go mountaineering",
    "October": "Go goddess",
    "November": "Go ride a bicycle",
    "december": "Go ride a bike",
}


def challenges_month_by_number(request, month):
    months = list(monthly_challenges.keys())
    Redirect_month = months[month]
    return HttpResponseRedirect("/challenges/"+Redirect_month)


def challenges_month(request, month):
    try:
        challenges_test = monthly_challenges[month]
        return HttpResponse(challenges_test)
    except KeyError:
        return HttpResponseNotFound("Invalid month")
