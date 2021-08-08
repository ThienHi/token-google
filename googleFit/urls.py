"""googleFit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from google_api.views import GetAccount, AuthAccount, Activity

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/google/get-auth/", GetAccount.as_view()),
    path("api/google/auth/", AuthAccount.as_view()),
    path("api/google/activity/", Activity.as_view()),
]
