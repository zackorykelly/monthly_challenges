from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no vegetables for one month!",
    "february": "Eat no vegetables for one month!",
    "march": "Eat no vegetables for one month!",
    "april": "Eat no vegetables for one month!",
    "may": "Eat no vegetables for one month!",
    "june": "Eat no vegetables for one month!",
    "july": "Eat no vegetables for one month!",
    "august": "Eat no vegetables for one month!",
    "september": "Eat no vegetables for one month!",
    "october": "Eat no vegetables for one month!",
    "november": "Eat no vegetables for one month!",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    forward_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
