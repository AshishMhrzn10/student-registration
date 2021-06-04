from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student
# Create your views here.

def student_list(request):
    context = {'student_list':Student.objects.all() }
    return render(request, "student_registration/student_list.html", context)


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_registration/student_form.html",{'form':form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/student/list')


def student_delete(request):
    return