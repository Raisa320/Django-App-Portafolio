from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
        #db_table = "proyectos"
        verbose_name = 'Poyecto'
        verbose_name_plural = 'Poyectos'

    def __str__(self):
        """Unicode representation of Poyecto."""
        return self.title
