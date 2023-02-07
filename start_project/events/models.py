from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    name = models.CharField('Event name', max_length = 50)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey('Venue', blank = True, null = True, on_delete = models.CASCADE)
    manager =  models.ForeignKey(User, blank = True, null = True, on_delete = models.SET_NULL)
    description = models.TextField(blank = True)
    attendees = models.ManyToManyField('My_club_users')
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField('Contact phone', max_length = 15, blank = True)
    web = models.URLField('Website address', blank = True)
    email = models.EmailField('Email address', blank = True)
    owner = models.IntegerField('venue_owner', blank=False, default=1)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

class My_club_users(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField('user email')
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Cat(models.Model):
    name = models.CharField(max_length = 10)
    age = models.CharField(max_length=2)
    def __str__(self):
        return self.name