from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



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
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })

    except:
        raise Http404()
