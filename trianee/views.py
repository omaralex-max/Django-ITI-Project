from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from track.models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView , UpdateView , DeleteView
from django.shortcuts import reverse 
from django.urls import reverse_lazy

class TrianeeUpdateG(UpdateView):
    model = Trainee
    template_name = 'trianee/update.html'
    fields = ['name', 'image', 'trackobj']
    success_url = reverse_lazy('trianee:list')


class TrianeeDeleteG(DeleteView):
    model = Trainee
    template_name = 'trianee/delete.html'
    success_url = reverse_lazy('trianee:list')


class TraineeCreateFormG(ListView):
    model = Trainee
    template_name = 'trianee/list.html'
    context_object_name = 'trianees'

class TraineeCreateForm(View):
    context = {}
    context['tracks'] = Track.objects.all()

    def get(self,request):
        
        return render(request, 'trianee/create.html',TraineeCreateForm.context)

    def post(self,request):
       

       if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        track = request.POST.get('track')

        if name and len(name) <= 300:
            if track and Track.objects.filter(pk=track).exists():
                Trainee.create(name=name, image=image, track=track)
                return redirect('trianee:list')  # Redirect to list view after creation
            else:
                TraineeCreateForm.context['error_message'] = 'Invalid Track ID!'
       else:
            TraineeCreateForm.context['error_message'] = 'Invalid name length!'

       return render(request, 'trianee/create.html', TraineeCreateForm.context)


    


def trianee_create(request):
    context = {}
    context['tracks'] = Track.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        track = request.POST.get('track')

        if name and len(name) <= 300:
            if track and Track.objects.filter(pk=track).exists():
                Trainee.create(name=name, image=image, track=track)
                return redirect('trianee:list')  # Redirect to list view after creation
            else:
                context['error_message'] = 'Invalid Track ID!'
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

# ---------------------------------> Forms
def trianee_create_model(request):
    form = AddTraineeModel()
    context = {'form': form} 
    if (request.method == 'POST'):
          form = AddTraineeModel(request.POST, request.FILES)
          if form.is_valid():
              form.save(commit=True)
              
    return render(request, 'trianee/addFormModel.html', context)


def trianee_create_form(request):
    context = {}
    form = addTrianee()

    if request.method == "POST":
        form = addTrianee(request.POST, request.FILES)

        if form.is_valid():
            print("Form is valid")  # Debug print
            track = Track.objects.get(id=form.cleaned_data['track'])
            trianeeobj = Trainee(
                name=form.cleaned_data['name'],
                image=request.FILES.get('imag'),
                trackobj=track,
            )
            trianeeobj.save()
            print("Trainee saved:", trianeeobj)
            return redirect('trianee:list')
        else:
            print("Form errors:", form.errors)
            context['error'] = form.errors

    context['form'] = form
    context['tracks'] = Track.objects.all()
    return render(request, 'trianee/createform.html', context)
