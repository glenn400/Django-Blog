from django.db import models

# Create your models here.
# create table
class Post(models.Model):
	title = models.CharField(max_length=240)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title
