from django.shortcuts import render_to_response
from django.http import HttpResponse

links = [
		{'name': 'Home', 'url': '/home/'},
		{'name': 'Biography', 'url': '/bio/'},
		{'name': 'Photos', 'url': '/photos/'}
		]

def index(request):
	return render_to_response('main.html', {'title': 'Home', 'links': links, 'content_var': 'This is the home page'})

def bio(request):
	return render_to_response('main.html', {'title': 'Biography', 'links': links, 'content_var': 'This is the bio page'})

def photos(request):
	return render_to_response('main.html', {'title': 'Photos', 'links': links, 'content_var': 'This is the photo page'})

