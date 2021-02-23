"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from store.views import login_page,home,register,buy,buy_not_found,user_logout,about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home'),
    path('login/',login_page,name='login'),
    path('register/',register,name='register'),
    path('buy/<int:P_id>/',buy,name='buy'),
    path('buy/',buy_not_found),
    path('logout',user_logout,name='logout'),
    path('admin/', admin.site.urls),
    path('about/',about,name='about')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
