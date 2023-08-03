from django.shortcuts import render,redirect
from . forms import *
from . models import *
from django.db.models import F
from django.contrib import messages


def create_deposite(request):
    profile = Profile.objects.get(nickname = request.user)
    form = CreateDeposite()
    if request.method =="POST":
        form = CreateDeposite(request.POST)
        amount = request.POST.get('amount')
        payment_type = request.POST.get('payment_type')
        deposite = Deposite.objects.create(
            profile = profile,
            amount =amount,
            payment_type=payment_type
        )
        if form.is_valid():
            deposite.save()
            address = Wallet_Address.objects.filter(name=payment_type).first()
            messages.info(request,f'Your deposite request was submitted successfully, Kindly copy this and addrsss   {address.address}')
        return redirect('/deposite')    
            
    context ={'form':form}
    return render(request,'dashbaord/form.html',context)


def update_deposite(request,pk):
    profile = Profile.objects.get(nickname = request.user)
    deposite = Deposite.objects.get(id=pk)
    form = UpdateDeposite(instance=deposite)
    if request.method =="POST":
        form = UpdateDeposite(request.POST,instance=deposite)
        status = request.POST.get('status')
        amount = deposite.amount
        payment_type = deposite.payment_type
        Deposite.objects.filter(id=pk).update(
            profile = profile,
            amount =amount,
            payment_type=payment_type,
            status = status
        )
        # deposite.save()
        
        if status == 'Successful':
            Profile.objects.filter(nickname=profile).update(balance=F('balance') + float(deposite.amount))
            return redirect('/deposite')
    context ={'form':form}
    return render(request,'dashbaord/update_form.html',context)


def create_withdraw(request):
    profile = Profile.objects.get(nickname = request.user)
    form = CreateWithdraw()
    if request.method =="POST":
        form = CreateWithdraw(request.POST)
        amount = request.POST.get('amount')
        payment_type = request.POST.get('payment_type')
        wallet_address = request.POST.get('wallet_address')
        withdraw = Withdraw.objects.create(
            Profile = profile,
            amount =amount,
            payment_type=payment_type,
            wallet_address = wallet_address
        )
        if form.is_valid():
            withdraw.save()
        if withdraw.status == 'Pending':
            Profile.objects.filter(nickname=profile).update(balance=F('balance') - float(withdraw.amount))    
        messages.info(request,f'Your withdraw request was submitted successfully')
        return redirect('/withdraw')    
    context ={'form':form}
    return render(request,'dashbaord/form.html',context)


def update_withdraw(request,pk):
    profile = Profile.objects.get(nickname = request.user)
    withdraw = Withdraw.objects.get(id=pk)
    form = UpdateDeposite(instance=withdraw)
    if request.method =="POST":
        form = updateWithdraw(request.POST,instance=withdraw)
        amount = withdraw.amount
        payment_type = withdraw.payment_type
        status = request.POST.get('status')
        Withdraw.objects.filter(id=pk).update(
            Profile = profile,
            amount =amount,
            payment_type=payment_type,
            status = status
        )
        if status == 'Failed':
            Profile.objects.filter(nickname=profile).update(balance=F('balance') +float(withdraw.amount))
        return redirect('/withdraw')
    context ={'form':form}
    return render(request,'dashbaord/form.html',context)