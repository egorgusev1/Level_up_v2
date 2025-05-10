"""
URL configuration for level_up project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from app.views import InternshipCreateView, InternshipListView

from allauth.account.views import SignupView

urlpatterns = [  
   
    path("admin/", admin.site.urls),
    path("articles/",include("app.urls")),
    path("accounts/",include("allauth.urls")),
    
    path("internships/",InternshipListView.as_view(), name="internship"),
    path("internships/create/",InternshipCreateView.as_view(), name="create_internship"),

    path("accounts/signup/",RedirectView.as_view(url="/")),   
    path("", SignupView.as_view(),name="account_signup"),
    path("__debug__/",include("debug_toolbar.urls")),
    path("__reload__/",include("django_browser_reload.urls")),
]
