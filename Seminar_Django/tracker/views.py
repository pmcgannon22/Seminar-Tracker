# Create your views here.
from django.shortcuts import render_to_response
from models import *
from django.core import serializers
from django.http import HttpResponse

students = Student.objects.all()

def index(request):
    return render_to_response('home.html', {'student_list':students})


def all_students_json(request):
    data = serializers.serialize("json",students)
    return HttpResponse(data,"application/javascript")
    
    
