# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def test_veiw(request):
	return render_to_response('test.dhtml')