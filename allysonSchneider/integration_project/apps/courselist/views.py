from django.shortcuts import render, redirect
from .models import Course
from ..loginreg.models import User
import bcrypt, re

# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all(),
        "all_users" : User.userManager.all(),
    }
    return render(request, 'courselist/index.html', context)

def addcourse(request):
    Course.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect('courses:index')

def confirm(request, id):
    context = {
        "courses" : Course.objects.filter(id = id),
        "id" : id
    }
    return render(request, 'courselist/delete.html', context, id)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('courses:index')

def addstudent(request):
    print request.POST
    user = User.userManager.get(id = request.POST['user'])
    course = Course.objects.get(id = request.POST['course'])
    course.students.add(user)

    return redirect('courses:index')
