"""NaijaLatest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('Frontend/', include('Frontend.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('', include('Music.urls')),
    path('Gist/', include('Gist.urls')),
    path('News/', include('News.urls')),
    path('Profile/', include('Profile.urls')),
    path('oauth', include('social_django.urls', namespace='social')),
    path('TalkZone', include('TalkZone.urls')),
    path('Mysteries', include('Mysteries.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('ads/', include('ads.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ]+ urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

