from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from handler.models import Album

links = [
		{'name': 'Home', 'url': '/home/'},
		{'name': 'Biography', 'url': '/bio/'},
		{'name': 'Photos', 'url': '/photos/'}
		]

def index(request):
	return render_to_response('main.html', {'title': 'Home', 'links': links, 'content_var': 'This is the home page'})

def bio(request):
	return render_to_response('main.html', {'title': 'Biography', 'links': links, 'content_var': 'This is the bio page'})

def photos(request, album_id='1'):
	picture_list = []
	try:
		album = Album.objects.get(pk='1')
		picture_list = album.picture_set.all()
	except Album.DoesNotExist:
		raise Http404
	return render_to_response('main.html', {'title': 'Photos', 'links': links, 'content_var': 'This is the photo page'})

