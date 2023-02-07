from django.contrib import admin
from .models import Event, Venue, My_club_users
# Register your models here.
# admin.site.register(Event)
# admin.site.register(Venue)
@admin.register(Venue)
class Venue_admin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('-name', )
    search_fields = ('name', 'address')
@admin.register(Event)
class Event_admin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'manager', 'description')
    fields = (('name', 'event_date'), ('venue', 'manager'), 'attendees', 'description')
    list_filter = ('event_date', 'venue')
admin.site.register(My_club_users)