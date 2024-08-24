from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from track.models import *
def account_create(request):
    
    context = {}

    if request.method == "POST":
        
        if (len(request.POST['name'])>0 and len(request.POST['name'])<=300):
          accountobj = Account()
          accountobj.name = request.POST['name']
          accountobj.email = request.POST['email']
          accountobj.phone = request.POST['phone']
          accountobj.address = request.POST['address']
          accountobj.password = request.POST['password']
          accountobj.trackobj=Track.objects.get(pk=request.POST['trackid'])
          accountobj.save()
        else:
          context['error_message'] = 'Invalid name length!'
    
    context['tracks'] = Track.objects.all()

    return render(request, 'account/create.html', context)
    
def account_update(request, id):  
    context = {'id': id}
    return render(request, 'account/update.html', context)
def account_delete(request, id):  
    context = {'id': id}
    return render(request, 'account/delete.html', context)
def list_account(request):

    context={}
    accc=Account.objects.all()
    context['accounts']=accc
    return render(request, 'account/list.html',context)
    

def show_details(request, id):
    
    account = Account.objects.get(pk=id)
    context = {'account': account}
    return render(request, 'account/show_details.html', context)