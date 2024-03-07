from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")


def login(request):
    return render(request, "login.html")

def registrationPage(request):
    return render(request, "register.html")