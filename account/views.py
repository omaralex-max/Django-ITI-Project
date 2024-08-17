from django.http import HttpResponse
from django.shortcuts import render

def account_create(request):
    return HttpResponse("Create account!")
def account_update(request, id):  
    return HttpResponse(f"Update account {id}!")

def account_delete(request, id):  
    return HttpResponse(f"Delete account {id}!")

def list_account(request):
    account=[]
    acc1={'id':1,'name':'omar'}
    acc2={'id':2,'name':'ali'}
    acc3={'id':3,'name':'sara'}
    account.append(acc1)
    account.append(acc2)
    account.append(acc3)
    context={}
    context['accounts']=account
    return render(request, 'account/list.html',context)
    

def show_details(request, id):  
    return HttpResponse(f"Show details for account {id}!")
