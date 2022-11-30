from django.shortcuts import render, redirect
from django.contrib import messages


def NetflixView(request):
    return render(request, 'netflix.html')


def IndexView(request):
    return render(request, 'index.html')


def SignupViews(request):
    return render(request, 'signup.html')


def SigninViews(request):
    return render(request, 'signin.html')


def NetflixViews(request):
    return render(request, 'netflix_view.html')
