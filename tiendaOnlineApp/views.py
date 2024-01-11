from django.shortcuts import render, HttpResponse
from services.models import Service
# Create your views here.

def home(request):
    return render(request, 'tiendaOnlineApp/home.html')


