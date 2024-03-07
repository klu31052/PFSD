from django.urls import path
from . import views

urlpatterns = [
    path("home", views.ttmhome, name="home"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration", views.checkregistration, name="checkregistration"),
    path("checkdetails", views.checkdetails, name="checkdetails"),
]
