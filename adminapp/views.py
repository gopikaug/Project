from django.shortcuts import render,redirect
from stationapp.models import Station_Reg, user_Reg
from django.contrib.auth.models import User
from django.contrib import messages

from userapp.models import book

# Create your views here.

def index(request):
    return render(request,'admin/index.html')


def station(request):
    shop = Station_Reg.objects.filter(station__last_name='0')
  
    return render(request,'admin/approve.html',{'shop':shop})

def view_station(request):
    shop = Station_Reg.objects.all()
  
    return render(request,'admin/view_station.html',{'shop':shop})
def view_user(request):
    shop = user_Reg.objects.all()
  
    return render(request,'admin/user.html',{'shop':shop})

def view_Booking(request):
    ch = book.objects.all()
  
    return render(request,'admin/view_booking.html',{'ch':ch})

def approve(request,id):
    user = User.objects.get(pk=id)
    user.last_name='1'
    user.save()
    messages.success(request, 'Approved')
    return redirect('stationv')
def reject(request,id):
    user = User.objects.get(pk=id)
    user.last_name='0'
    user.is_active='0'
    user.save()
    messages.success(request, 'Rejected')

    return redirect('stationv')

