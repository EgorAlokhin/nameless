from django import forms
from django.forms import  ModelForm
from .models import  Venue

class VenueForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'name'}), label='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'address'}), label='')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'phone'}), label='')
    web = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'website address'}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'email'}), label='')
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone', 'email', 'web', 'image')