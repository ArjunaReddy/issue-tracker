from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('details/<int:ticket_id>', views.details, name='details')
]
