from django.db import models

class Slide(models.Model):
	name = models.CharField(max_length=250,default='slide')
	dataX = models.IntegerField()
	dataY = models.IntegerField()
	dataY = models.IntegerField()
	dataZ = models.IntegerField()
	dataRotateX = models.IntegerField()
	dataRotateY = models.IntegerField()
	dataRotateZ = models.IntegerField()
	dataScale = models.IntegerField()
	message = models.TextField()

	def __str__(self):
		return self.name + ' - ' + str(self.id)
