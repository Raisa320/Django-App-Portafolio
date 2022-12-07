from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    """Model definition for usuario."""
    # TODO: Define fields here
    nombre = models.CharField(max_length=100)
    user = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=100)
    profile = models.CharField(max_length=254)
    phone = models.CharField(max_length=9)
    about = models.TextField()
    foto = models.CharField(max_length=500)
    servicios=models.CharField(max_length=500)
    class Meta:
        """Meta definition for usuario."""
        db_table = "usuarios"
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        """Unicode representation of usuario."""
        return self.user

class Proyecto(models.Model):
    """Model definition for Poyecto."""

    # TODO: Define fields here
    title = models.CharField( max_length=100)
    descripcion = models.TextField()
    foto = models.CharField(max_length=500)
    git = models.CharField( max_length=500)
    tags=models.CharField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        """Meta definition for Poyecto."""
        db_table = "proyectos"
        verbose_name = 'Poyecto'
        verbose_name_plural = 'Poyectos'

    def __str__(self):
        """Unicode representation of Poyecto."""
        return self.title
