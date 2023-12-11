from django.contrib import admin
from django.urls import path
from stationapp import views


urlpatterns = [
   path('',views.home,name='home'),
   path('login',views.loginview,name='login'),
   path('register',views.register,name='register'),
   path('user_registration',views.user_registration,name='user_registration'),



  

]






