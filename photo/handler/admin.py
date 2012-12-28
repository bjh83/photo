from photo.handler.models import Album, Picture
from django.contrib import admin

class PictureInline(admin.TabularInline):
	model = Picture
	extra = 3

class AlbumAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['name']}),
		]
	inlines = [PictureInline]

admin.site.register(Album, AlbumAdmin)

