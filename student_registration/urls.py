from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_form, name='student_insert'),
    path('<int:id>/', views.student_form, name='student_update'),
    path('list/', views.student_list, name='student_list'),
]
