import os
import sys
from django.core.handlers.wsgi import WSGIHandler

photopath = '/home/brendan/web/'

if photopath not in sys.path:
	sys.path.append(photopath)

handlerpath = '/home/brendan/web/photo/'

if handlerpath not in sys.path:
	sys.path.append(handlerpath)

os.environ['DJANGO_SETTINGS_MODULE'] = 'photo.settings'

application = WSGIHandler()

