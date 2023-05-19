from django.db import models

class Autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=50)
    activo=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


#Modelo libro byGus
class Libro(models.Model):
    titulo=models.CharField(max_length=80) 
    descripcion=models.CharField(max_length=180) 
    isbn=models.IntegerField(default=0)
    autor=models.ForeignKey(
        Autor,
        related_name="libros",
        on_delete=models.CASCADE,
    activo=models.BooleanField(default=True)

    )
    def __str__(self):
        return f"{self.titulo} - {self.autor}"



# Tarea de Kev
class PrestamoLibro(models.Model):
    fecha_prestamos = models.DateField()
    fecha_devolucion = models.DateField()
    socio = models.ForeignKey(
        Socio,
        on_delete=models.CASCADE
    )
    empleado: models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE
    )
    libro: models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.fecha_prestamos} - {self.fecha_devolucion}'
