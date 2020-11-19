from django.db import models
from areas.models import Area
from managers.models import Manager

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    manager = models.ManyToManyField(Manager, related_name="empleados")

    def __str__(self):
        self.nombre
