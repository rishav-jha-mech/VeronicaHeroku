from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('Veronica', views.veronica, name="veronica"),
    path('MediaScrap', views.mediascrap, name="mediascrap"),
    path('Founder', views.founder, name="Rishabh Jain"),
]
