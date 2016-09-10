from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
	GENEROS=(
		('Hombre','Hombre'),
		('Mujer','Mujer')
		)
	TIPO=(
		('Maestro', 'Maestro'),
		('Alumno', 'Alumno')
		)
	fecha_nacimiento=models.DateField(null=True,blank=True)
	sexo=models.CharField(max_length=140,choices=GENEROS,default="Hombre")
	bio = models.TextField(null=True,blank=True)
	is_user=models.CharField(max_length=140,choices=TIPO,default="Alumno")
	def __str__(self):
		return 'Este perfil pertenece a {}'.format(self.user)