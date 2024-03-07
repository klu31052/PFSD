from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homePage,name=""),
    path("login", views.login, name="login"),
    path("contact", views.contact, name="contact"),
    path("register", views.registrationPage, name="register"),
    path("", include("adminapp.urls")),
]