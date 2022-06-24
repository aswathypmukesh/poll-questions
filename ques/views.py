from winreg import QueryReflectionKey
from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.

def home(request):
    if request.method == 'GET':
        Q = Quest.objects.all()
        c = {
        'Quests': Q,
        }
        return render(request, 'home.html',c)
    

def votenow(request, pk):
    Q = Quest.objects.get(id=pk)
    if request.method == 'GET':
        c = {
            'form': Q
        }

    if request.method == 'POST':
        Q.likes = Q.likes + 1 
        Q.save()
        return redirect('/')

    elif request.method == 'POST':
        Q.dislikes = Q.dislikes + 1 
        Q.save()
        return redirect('/')  

    return render(request, 'votenow.html', c)

def votenow(request, pk):
    Q = Quest.objects.get(id=pk)
    if request.method == 'GET':
        c = {
            'form': Q
        }

    elif request.method == 'POST':
        Q.dislikes = Q.dislikes + 1 
        Q.save()
        return redirect('/')  

    return render(request, 'votenow.html', c)
    
def results(request, pk):  
    if request.method == 'GET':
        Q = Quest.objects.get(id=pk) 
        c = {
            'form': Q
        }

    return render(request, 'results.html', c)