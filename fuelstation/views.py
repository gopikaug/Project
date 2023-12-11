from django.shortcuts import redirect, render

from stationapp.models import Station_Reg
from userapp.models import book
from django.contrib import messages

# Create your views here.
    
def index(request):
    return render(request,'station/index.html')  
  
def viewBooking(request):
    us=Station_Reg.objects.get(station_id=request.user.id)
    ch=book.objects.filter(station_id=us)
    
    if request.method=='POST':
        id=request.POST['id']
        reply=request.POST['reply']

        ch=book.objects.get(id=id)
        ch.status=reply
        ch.save()
        messages.success(request, 'status Updated')
        return redirect('/viewBooking')

    return render(request,'station/view_booking.html',{'ch':ch})