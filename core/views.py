# Create your views here.

from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response

def homepage(request):
	context = RequestContext(request)
	
	return render_to_response('index.html', context)