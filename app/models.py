from django.db import models
from django.core.validators import validate_email

# Create your models here.

Sexo = (
    ("F", "Femenino"),
    ("M", "Masculino"),
)
Estado = (
    ("VIG", "Vigente"),
    ("SUS", "Suspendido"),
    ("RET", "Retirado"),
)
class Socio(models.Model):
    nombre = models.CharField(max_length=20)
    fechaIncorporacion = models.DateField()
    anoNacimiento = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField(validators=[validate_email])
    sexo = models.CharField(max_length=20, choices=Sexo, default="F")
    # estado = models.CharField(max_length=20)
    estado = models.CharField(
        max_length = 20,
        choices = Estado,
        default = 'VIG'
    )