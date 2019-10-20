from django.db import models



class Evento(models.Model):
    """
    Un clase que representa un evento del sistema
    ...

    Atributos
    ----------
    titulo: str
        El titulo del evento
    fecha_de_inicio : date
        fecha de inicio del evento
    hora_de_inicio : time
        hora de inicio del evento
    fecha_final : date
        fecha del fin,cierre o clausura del evento
    hora_final : time
        hora del fin,cierre o clausura del evento
    decripcion: Text
        una breve descripcion del evento
    ubicacion: str
        recinto o lugar donde se realiza el evento. 
        Ejemplo: Universum, Torre mayor, Facultad de ciencias, etc.
    duracion: 
        duracion total del evento en horas:minutos:segundos

    Subclases
    -------
    Meta
        Representa al evento en la base de datos
    """
    titulo = models.CharField(max_length=100)
    fecha_de_inicio = models.DateField()
    hora_de_inicio = models.TimeField()
    fecha_final = models.DateField()
    hora_final = models.TimeField()
    cupo_maximo = models.IntegerField()
    descripcion = models.TextField(blank=False, null=False)
    ubicacion = models.CharField(max_length=100, null=False)
    #duracion = hora_final - hora_de_inicio
    
    class Meta:
        db_table = 'evento'


class Direccion(models.Model):
    """
    Un clase que representa la direccion fisica de un evento
    ...

    Atributos
    ----------
    evento: Evento (llave foranea)
        Es el evento al que pertence la direccion
    calle: str
        calle de la direccion
    numero: str
        numero exterior de la calle donde se ubica el evento
    cp: str
        codigo postal de la ubicacion del evento
    edo: str
        estado de la republica donde se realiza el evento
    colonia:
        colonia o barrio donde se realiza el evento

    Subclases
    -------
    Meta
        Representa la direccion en la base de datos
    """
    evento = models.OneToOneField(
        Evento,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    edo = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)

    class Meta:
        db_table = 'direccion'


class Etiquetas(models.Model):
    """
    Un clase que representa las etiquetas con las que se 
    identifica un evento
    ...

    Atributos
    ----------
    evento: Evento
        evento al que pertenece la etiqueta
    etiqueta: str
        etiqueta del evento, sirve para categorizar los eventos.
        Ejemplos de etiquetas: cultura, deporte, sexualidad, musica, etc. 
    """
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    lista = models.CharField(max_length=400)


    class Meta:
        db_table = 'Etiquetas'




