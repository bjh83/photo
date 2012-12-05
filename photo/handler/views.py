from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from handler.models import Album

links = [
		{'name': 'Home', 'url': '/home/'},
		{'name': 'Biography', 'url': '/bio/'},
		{'name': 'Photos', 'url': '/photos/'}
		]

class PhotoPair:
	url = ''
	id = ''

	def __init__(self, url, id):
		self.url = url
		self.id = id

def index(request):
	return render_to_response('main.html', {'title': 'Home', 'links': links, 'content_var': 'This is the home page'})

def bio(request):
	return render_to_response('main.html', {'title': 'Biography', 'links': links, 'content_var': 'This is the bio page'})

def photos(request, album_id='1'):
	picture_list = []
	try:
		album = Album.objects.get(pk=album_id)
		album_list = Album.objects.all()
		picture_list = album.picture_set.all()
	except Album.DoesNotExist:
		raise Http404
	return render_to_response('image.html', {'title': 'Photos', 'links': links, 'picture_list': picture_list,
		'album_list': album_list, 'album': album, 'album_prefix': '/photos/'})

def view_photo(request, album_id, photo_id):
	new_picture_list = []
	new_selected = None
	try:
		album = Album.objects.get(pk=album_id)
		picture_list = album.picture_set.all()
		selected = album.picture_set.get(pk=photo_id)
		index = 0
		for picture in picture_list:
			new_picture_list.append(PhotoPair(picture.image.url, 'picture' + str(index)))
			index += 1
			if picture == selected:
				new_selected = new_picture_list[len(new_picture_list) - 1]
	except Album.DoesNotExist:
		raise Http404
	return render_to_response('photo_viewer.html', {'title': album.name, 'picture_list': new_picture_list,
		'selected': new_selected, 'body_style': 'picture_viewing'})

