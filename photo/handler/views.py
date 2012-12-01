from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	return HttpResponse("Home")

def bio(request):
	return HttpResponse("Bio")

def photos(request):
	return HttpResponse("Pictures")

