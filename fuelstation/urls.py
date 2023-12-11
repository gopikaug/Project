from django.urls import path

from adminapp import views



urlpatterns = [
    path('admin',views.index,name='admin'),
    path('stationv',views.station,name='stationv'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('view_station',views.view_station,name='view_station'),
    path('view_user',views.view_user,name='view_user'),
    path('view_Booking',views.view_Booking,name='view_Booking')





    
  
 
]
