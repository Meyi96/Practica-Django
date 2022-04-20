from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Client, BankAccount

def index(request):
    clients = Client.objects.all()
    return render(request,"manage_banks/index.html",{'client_list':clients})


def detail(request, client_id):
    client = get_object_or_404(Client,pk=client_id)
    return render(request,"manage_banks/detail.html",{
        'client':client
    })

def detail_bankAccount(request, bankaccount_id):
    bankaccount = get_object_or_404(BankAccount,pk=bankaccount_id)
    return render(request,"manage_banks/detail_bankAccount.html",{
        'bankAccount':bankaccount
    })

def charge_money(request, bankaccount_id):
    bankaccount = get_object_or_404(BankAccount,pk=bankaccount_id)
    try:
        bankaccount.balance+= float(request.POST['charge']) 
    except(ValueError, KeyError):
        return render(request,"manage_banks/detail_bankAccount.html",{
        'bankAccount':bankaccount,
        'error_message_c': 'Enter an amount'
        })
    else:
        bankaccount.save()
        return HttpResponseRedirect(reverse("manage_banks:detail", args=(bankaccount.client.id,)))

def transfer_money(request, bankaccount_id):
    bankaccount = get_object_or_404(BankAccount,pk=bankaccount_id)
    try:
        account_to_transfer= get_object_or_404(BankAccount,pk=int(request.POST['account']))
        amount= float(request.POST['amount']) 
    except(ValueError, KeyError):
        return render(request,"manage_banks/detail_bankAccount.html",{
        'bankAccount':bankaccount,
        'error_message_t': 'some of the data is uncompleted'
        })
    bankaccount.balance-=amount
    account_to_transfer.balance+=amount
    bankaccount.save()
    account_to_transfer.save()
    return HttpResponseRedirect(reverse("manage_banks:detail", args=(bankaccount.client.id,)))
