from django.shortcuts import render, redirect
from mango.forms import Data, profileData
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

   
# def update_profile(request,id):
#     us = User.objects.get(id=id)
#     us1 = Profile.objects.get(id=id)
#     form = User(request.POST, instance=us)
#     form1 = Profile(request.POST, instance=us1)
#     if form.is_valid() and form1.is_valid():
#       form.save()
#       form1.save()
#       return HttpResponse("Data Updated")
#     return render(request,"login_show.html",{'us':us})

















def update_profile(request,id):
    us, created = Profile.objects.get_or_create(user=request.user)
    form = profileData(request.POST, instance=us)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
            return redirect("/login_show")
    return render(request,"login_show.html",{'us':us})

# This function can only update the user field data (Bio, Phone No.) not username and password from auth_user table.
#It can only update that data through which user has entered.












# def update_profile(request, id):
#     profile_instance, created = Profile.objects.get_or_create(user=request.user)
#     user_instance = profile_instance.user

#     if request.method == "POST":
#         form = profileData(request.POST, instance=profile_instance)
#         if form.is_valid():
#             # Update custom profile fields
#             form.save()
#             # Update username and password if provided in the form
#             new_username = form.cleaned_data.get('new_username')
#             new_password = form.cleaned_data.get('new_password')
#             if new_username:
#                 user_instance.username = new_username
#             if new_password:
#                 user_instance.set_password(new_password)
#             user_instance.save()
#             return redirect("/login_show")
#     else:
#         form = profileData(instance=profile_instance)

#     return render(request, "login_show.html", {'form': form})

# def update_profile(request,id):
#     if request.method == "POST":
#         form = User(request.POST, instance=request.user) 
#         obj = Profile.objects.get(user_id=request.user.id)
#         form1 = profileData(request.POST or None, instance=obj) 

#         if form.is_valid() and form1.is_valid():
#             obj.bio = form1.cleaned_data['bio']
#             obj.phone_no= form1.cleaned_data['phone_no']
#             form.save()
#             form1.save()
#             print('updated successfully')
#             return redirect('/login_show')
#         else:
#             print('Please correct the error below.')
#     else:
#         form = Data(instance=request.user)
#         form1 = profileData(instance=request.user)
#     return render(request, "edit_profile.html", {'form': form, 'form1': form1})


# def update_profile(request, id):
#     user_instance = request.user
#     profile_instance = Profile.objects.get(user_id=request.user.id)

#     if request.method == "POST":
#         user_form = User(request.POST, instance=user_instance)
#         profile_form = Profile(request.POST, instance=profile_instance)

#         if user_form.is_valid() and profile_form.is_valid():
#             profile_instance.bio = profile_form.cleaned_data['bio']
#             profile_instance.phone_no = profile_form.cleaned_data['phone_no']
#             user_form.save()
#             profile_form.save()
#             print('Updated successfully')
#             return redirect('/login_show')
#         else:
#             print('Please correct the errors below.')
#     else:
#         user_form = User(instance=user_instance)
#         profile_form = Profile(instance=profile_instance)
    
#     return render(request, "edit_profile.html", {'user_form': user_form, 'profile_form': profile_form})


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
    login_log= Profile.objects.select_related('user').all()
    for login_dta in login_log:
        print(login_dta.user.username)
    return render(request,"login_show.html",{"login_log":login_log})

def show(request):
    users=User_Prod.objects.all()
    return render(request,"data.html",{"user":users})

def login_page(request):
    return render(request,"login.html")

def signup_page(request):
    return render(request,"signup.html")