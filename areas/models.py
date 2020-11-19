from django.db import models

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10)

    # editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    # autores = models.ManyToManyField(Autor, related_name="autores")
    def __str__(self):
        self.nombre
