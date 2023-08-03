
from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
# from .helper import generate_referal_code
    

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    referal = models.SlugField(null=True,blank=True)
    nickname = models.CharField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(default='',null='True',blank='True')
    date_created = models.DateTimeField(auto_now_add=True)
    referal_point = models.IntegerField(default=0)
    balance = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.nickname
    

class Deposite(models.Model):
    STATUS = (
        ('Pending','Pending'),('Failed','Failed'),('Successful','Successful')
    )
    D_Pay_TYPE = (('Bitcoin','Bitcoin'),('Ethereum','Ethereum'),('Tron','Tron'),('USDT TRC20','USDT TRC20'))
    profile= models.ForeignKey(Profile,on_delete=models.SET_NULL, null= True)
    amount = models.FloatField()
    payment_type = models.CharField(max_length=100,choices=D_Pay_TYPE)
    status = models.CharField(default=STATUS[0][0],max_length=100, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.created
    
    

class Withdraw(models.Model):
    STATUS = (
        ('Pending','Pending'),('Failed','Failed'),('Successful','Successful')
    )
    W_Pay_TYPE = (('Bitcoin','Bitcoin'),('Ethereum','Ethereum'),('Tron','Tron'),('USDT TRC20','USDT TRC20'))
    Profile= models.ForeignKey(Profile,on_delete=models.SET_NULL, null= True)
    amount = models.FloatField()
    payment_type = models.CharField(max_length=100,choices=W_Pay_TYPE)
    wallet_address = models.CharField(max_length=1000,blank=True,null=True)
    status = models.CharField(default=STATUS[0][0],max_length=100, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Profile.nickname
    
class Wallet_Address(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Plan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,blank=True)
    payout = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name