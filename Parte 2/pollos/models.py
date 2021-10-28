from django.db import models

class Pollo(models.Model):
    """Pollo Model"""
    id = models.BigAutoField(primary_key=True)
    lesionTipo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    lesionRango = models.CharField(max_length=20, null=True)
    granja = models.CharField(max_length=100, null=True)
    edadEnDias = models.IntegerField(null=True)
    ciclo = models.IntegerField(null=True)
    noGalpon = models.IntegerField(null=True)
    planVacuna = models.CharField(max_length=100, null=True)
    influenzaVacuna = models.CharField(max_length=100, null=True)
    newcastleVacuna = models.CharField(max_length=100, null=True)
    gumboroVacuna = models.CharField(max_length=100, null=True)
    lesionPromedio = models.IntegerField(null=True)
    nAnimal = models.IntegerField(null=True)
    sexoAnimales = models.CharField(max_length=20, null=True)
    bursometro = models.IntegerField(null=True)
    condicionHigado = models.CharField(max_length=20, null=True)
    integridadIntestinal = models.IntegerField(null=True)

    def __str__(self):
        """Return id"""
        return f"{self.id}-{self.lesionTipo}"
