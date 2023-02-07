from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from .models import Event, Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
import csv
from django.contrib.auth.models import User


def home(request, year = 2022, month = 'december'):
    data = 'Alokhin Egor 20.11.2010'
    events = Event.objects.all()
    month_number = list(calendar.month_name).index(month.title())
    month_number = int(month_number)
    calen = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'events/home.html', {'my_data': data, 'year' : year, 'month' : month_number, 'calen' : calen, 'events' : events})

def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/all_events.html', {'events' : events})

def add_venue(request):
    submited = False
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            venue = form.save(commit=False)
            venue.owner=request.user.id
            venue.save()
            return HttpResponseRedirect('/add_venue?submited=True')
    else:
        form = VenueForm
        if 'submited' in request.GET:
            submited = True
    return render(request, 'events/add_venue.html', {'form' : form, 'submited' : submited})

def all_venues(request):
    venues = Venue.objects.all()
    p = Paginator(venues, 2)
    page = request.GET.get('page')
    list_venue = p.get_page(page)
    nums = list_venue.paginator.num_pages * 'a'
    return render(request, 'events/all_venues.html', {'venues': venues, 'list_venue' : list_venue, 'nums' : nums})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id)
    form = VenueForm(request.POST or None, request.FILES or None, instance = venue )
    if form.is_valid():
        form.save()
        return redirect('all_venues')
    return render(request, 'events/update_venue.html', {'venue': venue, 'form' : form})

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('all_venues')

def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['Searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched' : searched, 'venues' : venues})
    else:
        return redirect('all_venues')

def venue_txt(request):
    responce = HttpResponse(content_type='text/plain')
    responce['Content-Disposition']= 'attachment; filename=venues.txt'
    venues = Venue.objects.all()
    lines = []
    for v in venues:
        lines.append(f'{v.name}\n{v.address}, {v.phone}, {v.web}, {v.email}\n\n')
    responce.writelines(lines)
    return responce

def venue_csv(request):
    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = 'attachment; filename=venues.csv'
    venues = Venue.objects.all()
    writer = csv.writer(responce)
    writer.writerow(['name', 'address', 'phone', 'web', 'email'])
    for v in venues:
        writer.writerow([v.name, v.address, v.phone, v.web, v.email])
    return responce

def show_venue(request, venue_id):
    venues = Venue.objects.get(pk = venue_id)
    venue_owner = User.objects.get(pk = venues.owner)
    return render(request, 'events/show_venue.html', {'venue' : venues, 'venue_owner' : venue_owner})

def my_venue(request, user_id):
    venues = Venue.objects.filter(owner = user_id)
    return render(request, 'events/my_venue.html', {'my_venue' : venues})

def show_event(request, event_id):
    events = Event.objects.get(pk = event_id)
    print(events.name)
    return render(request, 'events/show_event.html', {'event' : events})