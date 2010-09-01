# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response

def test_veiw(request):
	return render_to_response('test.dhtml')
	
def roster(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	else:
		return HttpResponse('ok dawg')