from django.db import models

class Files_up(models.Model):
	Nombre_archivo = models.CharField(max_length = 100)
	Descarga_archivo = models.FileField(upload_to = 'media/files/')

	def __str__(self):
		return self.Nombre_archivo