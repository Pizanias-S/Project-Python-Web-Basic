from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes",
    "march": "Learn Django for 60 minutes",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes",
    "june": "Learn Django for 60 minutes",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes",
    "september": "Learn Django for 60 minutes",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes",
    "december": "Learn Django for 60 minutes"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{redirect_month}")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
