from django.shortcuts import render, redirect
from .models import Student

def Home(request):
    all_students = Student.objects.all()
    context = {
        "all_students":all_students
    }
    return render(request, "home.html", context)


def Create_student(request):
    print("in create studenttttttttttt")
    if request.method=="POST":
        post_data = request.POST
        print("post_dataaaaaaaaaaaaa",post_data)

        name = post_data["name"]
        age = post_data["age"]

        # stuOb = Student()
        # stuOb.name = name
        # stuOb.age = age

        stuOb = Student.objects.create(name=name, age=age)
        stuOb.save()

        print("Student created succ")

        return redirect("/")
    

def Update_student(request,id):
    studentOb = Student.objects.get(id=id)
    context = {
        "studentOb":studentOb
    }
    return render(request, "update_student.html", context)


def Save_update_student(request,id):
    if request.method=="POST":
        post_data = request.POST
        print("post_dataaaaaaaaaaaaa",post_data)

        name = post_data["name"]
        age = post_data["age"]

        studentOb = Student.objects.get(id=id)
        print(studentOb)

        studentOb.name = name
        studentOb.age = age

        studentOb.save()

        return redirect("/")
    

def Delete_student(request,id):
    studentOb = Student.objects.get(id=id)
    studentOb.delete()

    return redirect("/")