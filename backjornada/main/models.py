from django.db import models

class Jornada(models.Model):
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)    

    def __str__(self):
        return self.nombre