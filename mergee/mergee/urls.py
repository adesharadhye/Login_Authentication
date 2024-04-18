"""
URL configuration for merge_ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mergee import views

urlpatterns = [
    path('update_profile/<int:id>', views.update_profile, name="update_profile"),
    path('show', views.show),
    path('', views.login_page),
    path('signup', views.signup),
    path('login', views.userLogin),
    path('admin/', admin.site.urls),
    path('logout',views.logout_view),
    path('login_show', views.login_show),
    path('signup_page', views.signup_page),
    path('accounts/login/',views.userLogin),
    path('insert', views.insert,name="insert"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),  
    path('del_profile/<int:id>', views.del_profile, name="del_profile"),  
    path('edit_profile/<int:id>', views.edit_profile, name="edit_profile"),
]