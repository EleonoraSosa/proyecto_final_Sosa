from django.db import models

# Create your models here.


class Registro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} --  Apellido:{self.apellido} --  Email:{self.email} -- Edad:{self.edad} "
   

class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=40)
    capital = models.CharField(max_length=40)
    codigo_postal = models.IntegerField()

    def __str__(self):
        return f"Ciudad: {self.ciudad} --  Capital:{self.capital} --  Codigo Postal:{self.codigo_postal} "

class Musica(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    año = models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.nombre} --  Genero:{self.genero} --  Año:{self.año} "
    
