from django.urls import path
from . import views

app_name = 'Music'

urlpatterns = [
    path('newsticker', views.newsticker, name='newsticker'),
    path('home', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('testing', views.testing, name='testing'),
    path('songs', views.songs, name='songs'),
    path('gospel', views.gospel, name='gospel'),
    path('hip_hop_rap', views.hip_hop_rap, name='hip_hop_rap'),
    path('hiphop_pop', views.hiphop_pop, name='hiphop_pop'),
    path('others', views.others, name='others'),
    path('video', views.video, name='video'),
    path('video_gospel', views.video_gospel, name='video_gospel'),
    path('video_hiphop_rap', views.video_hiphop_rap, name='video_hiphop_rap'),
    path('video_hiphop_pop', views.video_hiphop_pop, name='video_hiphop_pop'),
    path('video_others', views.video_others, name='video_others'),
    path('song_download/<slug>/', views.song_download, name='song_download'),
    path('video_download/<slug>/', views.video_download, name='video_download'),
    path('video_download/<slug>/', views.video_download, name='video_download'),
    path('add_music', views.add_music, name='add-music'),
    path('add_audio/<music_id>', views.add_audio, name='add-audio'),
    path('Add Video/<music_id>', views.add_video, name='add-video'),
    path('add_mixtape', views.add_mixtape, name='add_mixtape'),
    path('mixtape', views.mixtape, name='mixtape'),
    path('music_mixtape/<slug>/', views.play_mixtape, name='music_mixtape'),
    path('save_commment', views.save_comment, name='save_comment'),
    path('commment', views.display_comment, name='display_comment'),
    path('unplished_mixtape', views.unpublished_mixtape, name='unpublished_mixtape'),
    path('edit_news/<int:pk>/', views.edit_mixtape, name='Detailview'),
    path('unpublished_music', views.unpublished_music, name='unpublished_music'),
    path('edti_music/<int:pk>/', views.edit_music, name='edit_music'),
    path('unpublished_audio', views.unpublished_audio, name='unpublished_audio'),
    path('edti_audio/<int:pk>/', views.edit_audio, name='edit_audio'),
    path('unpublished_video', views.unpublished_video, name='unpublished_video'),
    path('edit_video/<int:pk>/+', views.edit_video, name='edit_video'),
    path('audiocount', views.audiocount, name='audiocount'),
    path('testes', views.debf.as_view(), name='debf')


]

