from django.db import models

from stationapp.models import Station_Reg, user_Reg

# Create your models here.
class book(models.Model):
    station = models.ForeignKey(Station_Reg, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user_Reg, on_delete=models.CASCADE, null=True)
    date=models.CharField(max_length=200, null=True)
    status=models.CharField(max_length=200, null=True)
    payment=models.CharField(max_length=200, null=True)
    type=models.CharField(max_length=200, null=True)
    quantity=models.CharField(max_length=200, null=True)
    
    

