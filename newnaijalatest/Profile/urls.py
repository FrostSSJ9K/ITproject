from django.urls import path, include, re_path
from . import views
from social_django.urls import app_name as name
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from social_core.utils import setting_name
app_name = 'Profile'
NAMESPACE = getattr(settings, setting_name('URL_NAMESPACE'), None) or 'social'

urlpatterns = [
    #path('login', auth_views.login, name='login'),
    path('oauth', include('social_django.urls', namespace='social')),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('sign_up_with_confirmation_mail', views.sign_up_with_confirmation_mail, name='sign_up_with_confirmation_mail'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
            name='activate'),
    path('account_activation_invalid', views.account_activation_invalid, name='account_activation_invalid'),
    path('account_activation_sent', views.account_activation_sent, name='account_activation_sent'),
    path('login', views.login, name='login'),
    path('loginn', views.loginn, name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('test', views.text, name='test'),
    path('status/search_status/', views.search_status, name='search'),
    path('ajax_calls/search/', views.autocomplete, name='autocomplete'),
    path('profile/', views.choose_profile, name='choose_profile'),
    #path('user-dashboard', views.user_dashboard, name='user-dashboard'),
    path('superuser', views.superuser, name='superuser'),
    path('special_user', views.special_user, name='special_user'),
    path('viewers', views.viewers, name='viewers'),
    path('permission', views.permission, name='permission'),
    path('access', views.display_user_type, name='access'),
    path('add_user', views.add_user, name='add_user'),
    path('user_type', views.change_user_type, name='change_user_type'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('password_reset_form', views.password_forgot, name='password_reset_form'),
    path('password_reset', views.password_reset, name='reset_password'),
    path('password_reset_email', views.password_reset_email, name='password_reset_email'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.change_password, name='change_password'),
    path('edit_user_profile', views.edit_user_profile, name='edit_user_profile')
    ]
