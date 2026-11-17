from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre de la Organización")
    code = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name="Código / NIT")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    is_active = models.BooleanField(default=True, verbose_name="Activa")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"
        ordering = ["name"]

    def __str__(self):
        return str(self.name)