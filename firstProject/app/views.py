
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def user_profile(request, username):
    return HttpResponse(f(request, 'user_profile.html', {'username': username}))