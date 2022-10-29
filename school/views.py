from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers')
    student_list = [student for student in students]
    context = {'students': student_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

def teachers_list(request):
    template = 'school/teachers_list.html'
    teachers = [teacher for teacher in Teacher.objects.all()]
    context = {'teachers': teachers}

    return render(request, template, context)

def index_view(request):
    template = 'school/base.html'
    context = {}
    return render(request, template, context)