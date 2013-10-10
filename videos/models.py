from django.db import models


class Video(models.Model):
	video_id = models.CharField(max_length=20)
	thumbnail = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	description = models.TextField()
	date = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return unicode(self.title)

	class Meta:
		ordering = ['-date']
