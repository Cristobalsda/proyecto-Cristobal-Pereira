from django.db import models

# Create your models here.

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    fechaIncorporacion = models.DateField()
    anoNacimiento = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField()
    sexo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
