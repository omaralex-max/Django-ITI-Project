from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from track.models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def trianee_create(request):
    context = {}
    context['tracks'] = Track.objects.all()

    if (request.method == "POST"):
        # print(request.POST)
        # print(request.FILES)  # Print all files
        # print(request.POST.keys())

        if (len(request.POST['name']) > 0 and len(request.POST['name']) <= 300):
            Trainee.create(request.POST['name'],
                           request.FILES['image'],
                           request.POST['trackid'] )
        else:
            context['error_message'] = 'Invalid name length!'

    return render(request, 'trianee/create.html', context)

def trianee_update(request, id):
    trianee = get_object_or_404(Trainee, id=id)
    if request.method == "POST":
        name = request.POST.get('name', '')
        trackid = request.POST.get('trackid')
        if len(name) > 0 and len(name) <= 300:
            trianee.name = name
            try:
                trianee.trackobj = Track.objects.get(pk=trackid)
            except Track.DoesNotExist:
                return HttpResponse("Track not found!", status=400)
            trianee.save()
            return redirect('trianee:list')  # Redirect to the list or details page after update
        else:
            return HttpResponse("Invalid name length!", status=400)

    context = {
        'trianee': trianee,
        'tracks': Track.objects.all()
    }
    return render(request, 'trianee/update.html', context)

def trianee_delete(request, id):
    
    context = {}
    try:
       Trainee.objects.filter(pk=id).delete()
       context['msg'] = "Trianee deleted"
       return redirect('list')
    except:
        import sys
        context['error'] = sys.exc_info()[1]
    return render(request, 'trianee/delete.html', context)

def list_trianee(request):
    context={}
    trian=Trainee.objects.all()
    context['trianees']=trian
    return render(request, 'trianee/list.html',context)

def show_details(request, id):
    # trianee = get_object_or_404(Trainee, id=id)
    # context = {'trianee': trianee}
    # return render(request, 'trianee/show_details.html', context)

     context = {'trianee':Trainee.objects.get(pk=id)}
     return render(request,'trianee/show_details.html',context)

from .forms import *
def trianee_create_form(request):
    context = {}
    form=addTrianee()
    context['form'] = form
    if request.method == "POST":
        form=addTrianee(request,request.POST,request.FILES)
        if form.is_valid():
            print('valid')
        else:
            print(form.errors)
            context['error'] = form.errors
    return render(request, 'trianee/createform.html',context)