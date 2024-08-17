from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('create/', views.account_create, name='create'),
    path('update/<int:id>', views.account_update, name='update'),
    path('delete/<int:id>', views.account_delete, name='delete'),
    path('list/', views.list_account, name='list'),
    path('details/<int:id>', views.show_details, name='details'),
]