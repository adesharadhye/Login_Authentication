from django.shortcuts import render, redirect
from mango.forms import Data, ProfileData
from mango.models import User_Prod, Profile
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def del_profile(request, id):    
        u = User.objects.get(id = id)
        u.delete()
        return redirect("/login_show")

def edit_profile(request, id):
    us = User.objects.get(id = id)
    return render(request,"edit_profile.html",{'us':us})

def update_profile(request,user_id):
    user = User.objects.get(pk=user_id)
    custom_user = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileData(request.POST, instance=custom_user)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()
            custom_user.bio = form.cleaned_data['bio']
            custom_user.phone_no = form.cleaned_data['phone_no']
            custom_user.save()
            return redirect('/login_show')
    else:
        form = ProfileData(instance=custom_user)
    return render(request, 'login_show.html', {'form': form})

def userLogin(request):
    if request.method == 'POST':
        name = request.POST['usname']
        passw = request.POST['uspass']
        norm = authenticate(request, username=name, password=passw)
        if norm:  
            login(request,norm)  
            return redirect('/insert')
        else:
            return HttpResponse("Invalid Username or Password")
    else:
        return render(request,"login.html")

@login_required(login_url="/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def insert(request):
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid:
           form.save()
           return redirect('/show')
    form=Data()
    return render(request,"cube.html",{"form":form})

def signup(request):
    us = request.POST['user_name_log']
    pa = request.POST['user_password'] 
    use= User.objects.create_user(username=us ,password=pa)
    Profile.objects.filter(user=use).update(bio=request.POST['bio'],phone_no=request.POST['phone_no'])
    return render(request, "login.html")

def update(request,id):
    us = User_Prod.objects.get(id=id)
    form = Data(request.POST, instance=us)
    if form.is_valid():
      form.save()
      return redirect('/show')
    return render(request,"edit.html",{'us':us})

def delete(request,id):
    us = User_Prod.objects.get(id=id)
    us.delete()
    return redirect('/show')

def edit(request,id):
    us=User_Prod.objects.get(id=id)
    return render(request,"edit.html",{'us':us})

def logout_view(request):
    logout(request)
    return render(request,"login.html")

def login_show(request):
    login_log= Profile.objects.all()
    
    return render(request,"login_show.html",{"login_log":login_log})

def show(request):
    users=User_Prod.objects.all()
    return render(request,"data.html",{"user":users})

def login_page(request):
    return render(request,"login.html")

def signup_page(request):
    return render(request,"signup.html")