from django.db import models
from django.contrib.auth.models import User



class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)


class Station_Reg(models.Model):
    station = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    License=models.CharField(max_length=200, null=True)

   

    
class user_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
