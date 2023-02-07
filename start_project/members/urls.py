from .views import *
from django.urls import path, include

urlpatterns = [
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', register_user, name = 'register')
]