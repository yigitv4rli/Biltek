"""biltekk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hakkimizda/',article_views.about, name="about"),
    path('bilim/',article_views.bilim, name="bilim"),
    path('teknoloji/',article_views.teknoloji, name="teknoloji"),
    path('biltek-nostalji/',article_views.biltek_nostalji, name="bilteknostalji"),
    path('makaleler/',article_views.all, name="all"),
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),
    path('',article_views.article_list, name="article_list"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ratings/', include('star_ratings.urls',namespace='ratings')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
