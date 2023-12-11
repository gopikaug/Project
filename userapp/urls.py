from django.urls import path

from userapp import views


urlpatterns = [
    path('user',views.index,name='user'),
    path('booking/<int:id>',views.booking,name='booking'),
    path('cancel/<int:id>',views.cancel,name='cancel'),

    path('bookservice',views.mybooking,name='bookservice'),
    path('payment/<int:id>',views.payment,name='payment'),


    
  
 
]
