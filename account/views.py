from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from track.models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def account_create(request):
    
    context = {}

    if request.method == "POST":
      print(request.POST.keys())  # Debugging line to print all POST keys
      if (len(request.POST['name']) > 0 and len(request.POST['name']) <= 300):
        accountobj = Account()
        accountobj.name = request.POST['name']
        accountobj.email = request.POST['email']
        accountobj.phone = request.POST['phone']
        accountobj.address = request.POST['address']
        accountobj.password = request.POST['password']
        accountobj.trackobj = Track.objects.get(pk=request.POST['trackid'])
        accountobj.save()
    else:
        context['error_message'] = 'Invalid name length!'

    
    context['tracks'] = Track.objects.all()

    return render(request, 'account/create.html', context)
    
def account_update(request, id):
    context = {}
    account = get_object_or_404(Account, pk=id)
    context['account'] = account
    context['tracks'] = Track.objects.all()

    if request.method == "POST":
        # Ensure that the keys exist in request.POST before accessing them
        if 'name' in request.POST and 'email' in request.POST and 'trackid' in request.POST:
            account.name = request.POST['name']
            account.email = request.POST['email']
            account.phone = request.POST['phone']
            account.address = request.POST['address']
            account.password = request.POST['password']
            account.trackobg = Track.objects.get(pk=request.POST['trackid'])
            account.save()
        else:
            context['error_message'] = "Missing required fields."

    return render(request, 'account/update.html', context)
def account_delete(request, id):  
    context = {}
    try:
       Account.objects.filter(pk=id).delete()
       context['msg'] = "Account deleted"
       return redirect('list')
    except:
        import sys
        context['error'] = sys.exc_info()[1]
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