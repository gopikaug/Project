from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages
from stationapp.models import Station_Reg, user_Reg
from userapp.models import book


# Create your views here.
def index(request):
    ser=Station_Reg.objects.all()
    return render(request,'user/index.html',{'ser':ser})

def booking(request,id):
    if request.method=='POST':
        ser=Station_Reg.objects.get(id=id)
        us=user_Reg.objects.get(user_id=request.user.id)
        b=book()
        b.station_id=ser.id
        b.user_id=us.id
        b.type=request.POST['type']
        b.date=request.POST['date']
        b.quantity=request.POST['qty']
        b.status='book'
        b.payment='not Paid'
        b.save()
        return redirect('bookservice')

    return render(request,'user/book.html')


def payment(request,id):
    if request.method=='POST':
        ch=book.objects.get(id=id)
        ch.payment='paid'
        ch.save()
        return redirect('/user')
        
    return render(request,'user/payment.html')

       

    
def mybooking(request):
    us=user_Reg.objects.get(user_id=request.user.id)
    ch=book.objects.filter(user_id=us)
    return render(request,'user/mybooking.html',{'ch':ch})



def cancel(request,id):
    user = book.objects.get(id=id)

    if request.method == 'POST':
        user.status='cancel'
        return redirect('bookservice')

    return render(request,'user/delete.html',{'user':user})
