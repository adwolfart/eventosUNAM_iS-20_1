from django.db import models

class Evento(models.Model):
    titulo = models.CharField(label= "titulo", max_length=100)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    #numero maximo de asistentes al evento
    n_max = models.IntegerField()
    descripcion = models.CharField(widget=forms.Textarea)
    #recinto del evento
    ubicacion = models.CharField(label= "ubicacion",max_lenght=100)
    #duracion del evento, es valor calculado
    duracion = self.fin - self.inicio
    """
    periodicidad
    """
    class Meta:
        db_table = 'evento'

class Direccion(models.Model):
    evento = models.OneToOneField(
        EventoModelo,
        primary_key = True
    )
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    edo = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)

class Etiquetas(models.Model):
    eventos = models.ManyToManyField(Evento)
    etiqueta = models.CharField(max_lenght=100)

    class Meta:
        db_table = 'etiquetas'
        unique_together = (('eventos', 'etiqueta'),)


