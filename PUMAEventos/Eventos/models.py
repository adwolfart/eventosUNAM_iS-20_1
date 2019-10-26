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
    entidad = models.CharField(max_length = 150)
    etiqueta1 = models.CharField(max_length = 50, null = True)
    etiqueta2 = models.CharField(max_length = 50, null = True)
    etiqueta3 = models.CharField(max_length = 50, null = True)
    correo = models.EmailField(max_length = 150, null = False, default = 'null@c.com')
    #duracion = hora_final - hora_de_inicio
    
    class Meta:
        db_table = 'evento'


class RegEvento(models.Model):
    id_Evento = models.IntegerField()
    email_Organizador = models.EmailField()
    email_Usuario = models.EmailField()



