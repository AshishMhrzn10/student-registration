from django.shortcuts import render

# Create your views here.

def student_list(request):
    return render(request, "student_registration/student_list.html")


def student_form(request):
    return render(request, "student_registration/student_form.html")


def student_delete(request):
    return