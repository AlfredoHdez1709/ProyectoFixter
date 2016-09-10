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
	fecha_nacimiento=models.DataFiel(null=True,blank=True)
	Nivel=(
		('Maestro','Maestro'),
		('Alumno','Alumno')
		)
	sexo=models.CharField(max_length=140,Choices=GENEROS,default="Hombre")
	bio = models.TexField(null=True,blank=True)
	is_user=models.CharField(max_length=140,Choices=TIPO,default="Alumno")
# Create your models h
