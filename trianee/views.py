from django.http import HttpResponse
from django.shortcuts import render

def trianee_create(request):
    return HttpResponse("Create trianee!")

def trianee_update(request, id):
    return HttpResponse(f"Update trianee {id}!")

def trianee_delete(request, id):
    return HttpResponse(f"Delete trianee {id}!")

def list_trianee(request):
    trinees = []
    trianee1 = {'id': 1, 'name': 'omar'}
    trianee2 = {'id': 2, 'name': 'ali'}
    trianee3 = {'id': 3, 'name': 'sara'}
    trinees.append(trianee1)
    trinees.append(trianee2)
    trinees.append(trianee3)
    context = {'trinees': trinees}
    return render(request, 'trianee/list.html', context)

def show_details(request, id):
    return HttpResponse(f"Show details for trianee {id}!")
