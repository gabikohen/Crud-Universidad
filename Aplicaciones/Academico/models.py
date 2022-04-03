from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True,max_length=8)
    name = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

""" Me deja mostrar el nombre del curso """

def __str__(self):
        text = "{0} ({1})"
        return text.format(self,codigo,self.name, self.creditos)