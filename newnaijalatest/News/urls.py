from django.urls import path
from . import views

app_name = 'News'

urlpatterns = [
    path('politics', views.politics, name='politics'),
    path('sport', views.sport, name='sport'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('all_news', views.all_news, name='all_news'),
    path('display_news/<slug>/', views.display_news, name='display_news'),
    path('addnews', views.add_news, name='addnews'),
    path('review_new', views.unpublished_news, name='review_news'),
    path('edit_news/<int:pk>/', views.edit_news, name='Detailview')
    ]
