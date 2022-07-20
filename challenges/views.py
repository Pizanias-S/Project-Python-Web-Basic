from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes"
    elif month == "march":
        challenge_text = "Learn Django for 60 minutes"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
