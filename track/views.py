from django.http import HttpResponse
from django.shortcuts import render

def track_create(request):
    return HttpResponse("Create track!")

def track_update(request, id):  
    return HttpResponse(f"Update track {id}!")

def track_delete(request, id):  
    return HttpResponse(f"Delete track {id}!")

def list_track(request):
    tracks = []
    track1 = {'id': 1, 'name': 'full-stack'}
    track2 = {'id': 2, 'name': 'front-end'}
    track3 = {'id': 3, 'name': 'back-end'}
    tracks.append(track1)
    tracks.append(track2)
    tracks.append(track3)
    context = {}
    context['tracks'] = tracks
    return render(request, 'track/list.html', context)
    

def show_details(request, id):  
    return HttpResponse(f"Show details for track {id}!")
