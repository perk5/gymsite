from django.shortcuts import render
from django.http import HttpResponse
from .models import Information


def index(request):

    return render(request, 'index.html')


def workouts(request):
    return render(request, 'workouts.html')


def nutrition(request):
    return render(request, 'nutrition.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def submitted(request):
    print('form submitted...')
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['project']

    i = Information(name=name, email=email, message=message)
    i.save()
    return render(request, 'index.html')
