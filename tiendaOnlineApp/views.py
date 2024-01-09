from django.shortcuts import render, HttpResponse
from services.models import Service
# Create your views here.

def home(request):
    return render(request, 'tiendaOnlineApp/home.html')



def shop(request):
    return render(request, 'tiendaOnlineApp/shop.html')

def blog(request):
    return render(request, 'tiendaOnlineApp/blog.html')

def contact(request):
    return render(request, 'tiendaOnlineApp/contact.html')