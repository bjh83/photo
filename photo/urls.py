from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photo.views.home', name='home'),
    # url(r'^photo/', include('photo.foo.urls')),
	url(r'^home/$', 'photo.handler.views.index'),
	url(r'^$', 'photo.handler.views.index'),
	url(r'^bio/$', 'photo.handler.views.bio'),
	url(r'^photos/$', 'photo.handler.views.photos'),
	url(r'^photos/(?P<album_id>\d+)/$', 'photo.handler.views.photos'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :
	urlpatterns += patterns('', 
			(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
			)
