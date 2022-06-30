# from winreg import QueryReflectionKey
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from django.http import HttpResponse


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
    return render(request, 'votenow.html', c)


def like(request, pk):
    Q = Quest.objects.get(id=pk)
    if request.method == 'GET':
        c = {
            'form': Q
        }

    # if request.method == 'POST':
        Q.likes = Q.likes + 1 
        Q.save()
        return redirect('/')  

    return render(request, 'votenow.html', c)

def dislike(request, pk):
    Q = Quest.objects.get(id=pk)
    if request.method == 'GET':
        c = {
            'form': Q
        }

    # if request.method == 'POST':
        Q.dislikes = Q.dislikes + 1 
        Q.save()
        return redirect('home')  

    return render(request, 'votenow.html', c)

# def votenow(request, pk):
#     Q = Quest.objects.get(id=pk)
#     if 'Like' in request.POST:
#         Q.likes = Q.likes + 1 
#         Q.save()
#         return redirect('/') 

#     if 'DisLike' in request.POST:
#         Q.dislikes = Q.dislikes + 1 
#         Q.save()
#         return redirect('/') 

#     c = {
#         'form': Q
#     } 

#     return render(request, 'votenow.html', c)
    
def results(request, pk):  
    if request.method == 'GET':
        Q = Quest.objects.get(id=pk) 
        c = {
            'form': Q
        }

    return render(request, 'results.html', c)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u = Login.objects.all()
        if Login:
            request.session['u'] = username
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.') 
    else:
        return render(request,'login.html')

def logout(request):
    del request.session['u']
    return redirect('login')