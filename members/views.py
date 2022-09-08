from pickle import FALSE
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue, plant_inf
from .forms import VenueForm, plant_infoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def add_plants(request):
    submitted = False
    if request.method == 'POST':
        form = plant_infoForm( request.POST )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_plants?submitted=True')
    else:
        form = plant_infoForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'authentication/add_plant_info.html', {'form':form, 'submitted': submitted})

    

@login_required(login_url='/accounts/login/')
def plant_info(request):
   plant_info = plant_inf.objects.all()
   return render(request, 'authentication/plant_info.html',
        {'plant_info': plant_info})

def accounts(request):
    accounts = Event.objects.all()
    return render(request, 'home.html',
        {'accounts': accounts  })



def search_venues(request):
    if request.method == 'POST':
        print(request.POST)
        searched = request.POST.get('searched')
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'authentication/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'authentication/search_venues.html', {})

@login_required(login_url='/accounts/login/')
def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'authentication/show_venue.html',
        {'venue': venue })


@login_required(login_url='/accounts/login/')
def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'authentication/venue.html',
        {'venue_list': venue_list  })



@login_required(login_url='/accounts/login/')
def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'authentication/add_venue.html', {'form':form, 'submitted': submitted})
  




def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'event_list.html',
        {'event_list': event_list  })




def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    isloggedin = FALSE
    return render(request, 'authentication/home.html', {})