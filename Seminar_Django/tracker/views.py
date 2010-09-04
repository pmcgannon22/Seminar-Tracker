# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response
from Seminar_Django.tracker.models import *

def test_veiw(request):
	return render_to_response('test.dhtml')
	
def roster(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	else:
		students = Student.objects.filter(seminar=request.user.get_profile())
		return render_to_response('home.dhtml',{'student_list' : students})
		
def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	else:
		return HttpResponseRedirect('/accounts/profile/')