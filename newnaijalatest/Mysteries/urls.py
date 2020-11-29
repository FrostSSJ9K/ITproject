from django.urls import path
from . import views

app_name = 'Mysteries'

urlpatterns = [
    path('quotes', views.quotes, name='quotes'),
    path('letters', views.letter, name='letters'),
    path('poem', views.poem, name='poem'),
    path('soul-awakening', views.soul_awakening, name='soul-awakening'),
    path('add_mysteries', views.add_mysteries, name='add_mysteries'),
    path('unpublished', views.unpublished_mystery, name='unpublished'),
    path('edit_mystery/<int:pk>/', views.edit_mystery, name='Detailview')
    ]
