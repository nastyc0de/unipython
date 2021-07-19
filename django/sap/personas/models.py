from django.db import models

# Create your models here.
class Domicilio(models.Model):
    street = models.CharField(max_length=200)
    nro_street = models.IntegerField()
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.street} {self.nro_street}'
        
class Persona(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.lastName}'