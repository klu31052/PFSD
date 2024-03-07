from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")


def login(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def registrationPage(request):
    return render(request, "register.html")