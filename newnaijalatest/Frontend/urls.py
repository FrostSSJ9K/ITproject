from django.urls import path
from . import views

app_name = 'Frontend'

urlpatterns = [
    path('base', views.base, name='base'),
    path('search', views.search, name='search'),
    path('contact-us', views.add_contact, name='contact-us'),
    path('advertisement', views.advertisement, name='advertisement')
]