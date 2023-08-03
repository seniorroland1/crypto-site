from django.forms import ModelForm
from . models import *

class CreateDeposite(ModelForm):
    class Meta:
        model = Deposite
        fields =['amount','payment_type']
        

class UpdateDeposite(ModelForm):
    class Meta:
        model = Deposite
        fields =['status']
        


class CreateWithdraw(ModelForm):
    class Meta:
        model = Withdraw
        fields =['amount','payment_type','wallet_address']
        
        
class updateWithdraw(ModelForm):
    class Meta:
        model = Withdraw
        fields =['status']