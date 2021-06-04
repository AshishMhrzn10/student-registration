from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student
# Create your views here.

def student_list(request):
    context = {'student_list':Student.objects.all() }
    return render(request, "student_registration/student_list.html", context)


def student_form(request, id=0):
    if request.method == "GET":
        if id==0:       #Insert operation
            form = StudentForm()
        else:       #Update operation
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student_registration/student_form.html",{'form':form})
    else:
        if id == 0:     #Insert operation
            form = StudentForm(request.POST)
        else:           #Update operation
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
        return redirect('/student/list')


def student_delete(request):
    return