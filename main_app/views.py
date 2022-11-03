from django.shortcuts import render
from .calendar_API import test_calender

# Create your views here.
def home(request):
    return render(request, 'home.html')


def GoogleCalendarRedirectView(request):
    results = test_calender() 
    context = {"results": results}
    return render(request, 'demo.html', context)    