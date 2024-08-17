from django.urls import path
from . import views

app_name = 'trianee'

urlpatterns = [
    path('create/', views.trianee_create, name='create'),
    path('update/<int:id>/', views.trianee_update, name='update'),
    path('delete/<int:id>/', views.trianee_delete, name='delete'),
    path('list/', views.list_trianee, name='list'),
    path('details/<int:id>/', views.show_details, name='details'),
]
