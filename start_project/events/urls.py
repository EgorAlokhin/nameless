
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:year>/<str:month>', home, name='home'),
    path('', home, name='home'),
    path('events', all_events, name='all_events'),
    path('add_venue', add_venue, name='add_venue'),
    path('all_venues', all_venues, name='all_venues'),
    path('update_venue/<venue_id>', update_venue, name='update_venue'),
    path('delete_venue/<venue_id>', delete_venue, name='delete_venue'),
    path('search_venues', search_venues, name='search_venues'),
    path('venue_txt', venue_txt, name='venue_txt'),
    path('venue_csv', venue_csv, name='venue_csv'),
    path('show_venue/<venue_id>', show_venue, name='show_venue'),
    path('my_venue/<user_id>', my_venue, name='my_venue'),
    path('show_event/<event_id>', show_event, name='show_event')

]