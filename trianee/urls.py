from django.urls import path
from . import views

app_name = 'trianee'

urlpatterns = [
    # path('create/', views.trianee_create, name='create'),
    path('create/', views.TraineeCreateFormG.as_view(), name='create'),
    path('createForm/', views.trianee_create_form, name='create_form'),
    path('addFormModel/', views.trianee_create_model, name='create_form_model'),
    # path('update/<int:id>/', views.trianee_update, name='update'),
    path('update/<int:pk>/', views.TrianeeUpdateG.as_view(), name='update'),
    path('delete/<int:pk>/', views.TrianeeDeleteG.as_view(), name='delete'),
    # path('delete/<int:id>/', views.trianee_delete, name='delete'),
    path('list/', views.list_trianee, name='list'),
    path('details/<int:id>/', views.show_details, name='details'),
]
