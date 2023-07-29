from django.shortcuts import render
from .models import Student
import PIL
# Create your views here.

def home(request):
    return render(request,'pages/home.html')
def about(request):
    return render(request,'pages/about.html')
def student(request):
    # students=Student.objects.all()
    # student=[]
    # for st in students:
    #     student.append({'sit':st})
    # context={'student':student}
    return render (request,'parts/student.html',{'stu':Student.objects.all()})