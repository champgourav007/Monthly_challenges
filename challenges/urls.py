from django.urls import path
from . import views


urlpatterns = [
    path("",views.firstPage,name = "index"),
    path("<int:month>",views.month_by_number),
    path("<str:month>",views.monthlyChallenge,name="monthly-challenge")
]