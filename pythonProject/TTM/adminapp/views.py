from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from.models import Admin,Register,Packages
def ttmhome(request):
    return render(request, "home.html")

def loginfail(request):
    return render(request, "loginfail.html")

def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        flag=Register.objects.filter(username=name,password=pwdd).values()
        if flag: #flag is not null or not empty
            if name=="adminname":
                messages.info(request,"This is admin's student page")
                return render(request,"adminhome.html")
        if flag:
            messages.info(request, "This is user's student page")
            return render(request, "home.html")
        else:
            messages.info(request,"Invalid Credentials!!")
            return render(request, "loginfail.html")
def checkregistration(request):
    if request.method  == "POST":
         name = request.POST["name"]
         addr = request.POST["addr"]
         email = request.POST["email"]
         phno = request.POST["phno"]
         uname = request.POST["uname"]
         pwd = request.POST["pwd"]
         cpwd = request.POST["cpwd"]
         if pwd==cpwd:
             if Register.objects.filter(username=uname).exists():
                 messages.info(request,"username existing..!!")
                 return render(request,"register.html")
             elif Register.objects.filter(email=email).exists():
                 messages.info(request,"email existing..!!")
                 return render(request,"register.html")
             else:
                 user=Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                 user.save()
                 messages.info(request,"user created")
                 return render(request,"login.html")
         else:
             messages.info(request,"password not matching..!!")
             return render(request,"register.html")

def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode, tourname=tname, tourpackage=tpack, desc=tdesc)
        pack.save()
        messages.info(request, "Data Inserted Sucessfully")
        return render(request, "details.html")
    else:
        messages.info(request, "Data Not Inserted!!")
        return render(request, "details.html")