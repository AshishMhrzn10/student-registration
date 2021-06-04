from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def student_list(request):
    return render(request, "student_registration/student_list.html")


def student_form(request):
    form = StudentForm()
    return render(request, "student_registration/student_form.html",{'form':form})


def student_delete(request):
    return