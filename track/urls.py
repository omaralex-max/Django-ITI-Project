from django.urls import path
from . import views

app_name = 'track'

urlpatterns = [
    path('create/', views.track_create, name='create'),
    path('delete/<int:id>/', views.track_delete, name='delete'),
    path('update/<int:id>/', views.track_update, name='update'),
    path('list/', views.list_track, name='list'),
    path('details/<int:id>/', views.show_details, name='details'),
]
