from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photo.views.home', name='home'),
    # url(r'^photo/', include('photo.foo.urls')),
	url(r'^home/', 'handler.views.index'),
	url(r'^$', 'handler.views.index'),
	url(r'^bio/$', 'handler.views.bio'),
	url(r'^photos/$', 'handler.views.photos'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
