# Create your views here.
from django.shortcuts import render_to_response
from models import *

def index(request):
    students = Student.objects.all()
    return render_to_response('home.html', {'student_list':students})
    
