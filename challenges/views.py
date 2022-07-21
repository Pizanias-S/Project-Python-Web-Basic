from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


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

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("months-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month!")
    redirect_month = months[month - 1]
    # /challenge/january
    redirect_path = reverse("months-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
