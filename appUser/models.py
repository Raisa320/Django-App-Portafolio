from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=254)
    phone = models.CharField(max_length=9, blank=True)
    about = models.TextField(blank=True)
    pais = models.CharField(max_length=50)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    servicios = models.CharField(max_length=500, blank=True)
    gitPerfil = models.CharField(max_length=500, blank=True)
    linkedPerfil = models.CharField(max_length=500, blank=True)

    class Meta:
        """Meta definition for usuario."""

        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        """Unicode representation of usuario."""
        return f"{self.user.username} Profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
