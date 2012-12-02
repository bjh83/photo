from django.db import models

class Album(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Picture(models.Model):
	album = models.ForeignKey(Album)
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="pictures", max_length=200)

	def __unicode__(self):
		return self.name

