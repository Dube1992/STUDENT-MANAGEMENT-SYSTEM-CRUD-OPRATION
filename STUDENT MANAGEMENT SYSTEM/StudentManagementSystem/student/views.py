from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    std=Student.objects.all()
    return render(request,"student/home.html",{'std':std})


def student_add(request):
    if request.method=='POST':
        print("value inserted")
        # Retrive data from user ...
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")
        std_phone=request.POST.get("std_phone")

        #create an object for model class
        s=Student()
        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.address=std_address
        s.phone=std_phone

        s.save()
        return redirect("/student/home")

    return render(request,"student/student_add.html",{})


def student_update(request,roll):
    std=Student.objects.get(pk=roll)
    return render(request,"student/student_update.html",{'std':std})

def do_student_update(request,roll):
    std_roll=request.POST.get("std_roll")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_address=request.POST.get("std_address")
    std_phone=request.POST.get("std_phone")

    std=Student.objects.get(pk=roll)

    std.roll = std_roll
    std.name = std_name
    std.email = std_email
    std.address = std_address
    std.phone = std_phone

    std.save()
    return redirect("/student/home/")


def student_delete(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/student/home/")

