from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january" : "It is january",
    "feburary": "it is feburary",
    "march" : "it is march",
    "april" : "it is april",
    "may" : "it is may",
    "june" : "it is june",
    "july" : "it is july",
    "august" : "it is august",
    "september" : "it is september",
    "october" : "it is october",
    "november" : "it is november",
    "december" : None
}

def month_by_number(request, month):
    if month > 12:
        return HttpResponseNotFound("Invalid Month")
    months = list(monthly_challenges.keys())
    res = months[month-1]
    pathRedirect = reverse("monthly-challenge",args=[res])
    return HttpResponseRedirect(pathRedirect)

def monthlyChallenge(request, month):
    try:
        return render(request,"challenges/challenges.html",{
            "month_name" : month,
            "task" : monthly_challenges[month]
        })
    except:
        raise Http404()

def firstPage(request):
    monthChallengeList = ""
    for i,j in monthly_challenges.items():
        capitalized_month = i.capitalize()
        month_path = reverse("monthly-challenge",args=[i])
        monthChallengeList += f"<li><a href= \"{month_path}\">{capitalized_month}</a></li>"
    
    return render(request,"challenges/index.html",{
        "months" : list(monthly_challenges.keys())
    })