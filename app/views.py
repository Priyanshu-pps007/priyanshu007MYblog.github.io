from operator import imod
from tkinter import PhotoImage
from django.http import HttpResponse,request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from app.models import diary
from django.contrib import messages
import datetime
# from .forms import Imageform

 
# uname=""


def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        global uname
        uname=username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            content=diary.objects.filter(username=username)
            print(diary.objects.filter(username=username))
            # for c in content:
            #     if c.username==uname:
            return render(request,'blog.html',{'content':content})
            # else:
            #     return redirect('home')
                # Redirect to a success page.

        else:
            return HttpResponse('Invalid Credentials')
            # Return an 'invalid login' error message.
    return render(request,'login.html')


def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        global uname
        uname=username
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request,'homepage.html')
    return render(request,'signup.html')

def home(request):
    if request.user.is_authenticated:
        
        if request.method=='POST':
            # form=Imageform(request.POST,request.FILES)
            # if form.is_valid():
                # form.save()
                # print(uname)
            items=diary()
            items.displaytime=datetime.datetime.now()
            items.username=uname
            items.text=request.POST.get('text')
            if len(request.FILES)!=0:
                items.photo=request.FILES['photo']
            # user=User.objects.all()
            
            items.save()
            messages.success(request,"Your data is saved")
        # form=Imageform()
        return render(request,'homepage.html')
        
    else:
        return redirect('loginuser')

def blog(request):
    
    if request.method=='POST':
        return redirect("/home")
    content=diary.objects.filter(username=uname)
    return render(request,'blog.html',{'content':content})

        
def logout_view(request):
    logout(request)
    return redirect('/')

    # Redirect to a success page.
    