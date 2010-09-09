# Create your views here.
from django.shortcuts import render_to_response
from models import *
from django.core import serializers
from django.http import HttpResponse



def index(request):
    students = Student.objects.all()
    return render_to_response('home.html', {'student_list':students})


def query_students_json(request, query):
    query = str(query)
    students = Student.objects.filter(firstName__startswith=query) | Student.objects.filter(lastName__startswith=query)
    data = serializers.serialize("json",students)
    return HttpResponse(data,"application/json")

def all_students_json(request):
    students = Student.objects.all()
    data = serializers.serialize("json",students)
    return HttpResponse(data,"application/json")
    
    
