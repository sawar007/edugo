from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('logout/',views.logout,name="logout"  ),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    
]