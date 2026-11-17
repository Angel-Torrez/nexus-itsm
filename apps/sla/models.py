from django.db import models
from apps.organizations.models import Organization

class SLAPolicy(models.Model):
    """Represents an SLA policy for a given priority and organization."""

    PRIORITY_CHOICES = [
        ('LOW', 'Baja'),
        ('MEDIUM', 'Media'),
        ('HIGH', 'Alta'),
        ('CRITICAL', 'Crítica'),
    ]

    name = models.CharField(max_length=150, verbose_name="Nombre del SLA")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, unique=True, verbose_name="Prioridad")
    response_time_hours = models.PositiveIntegerField(verbose_name="Tiempo máx. de respuesta (horas)")
    resolution_time_hours = models.PositiveIntegerField(verbose_name="Tiempo máx. de resolución (horas)")
    organization = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='sla_policies',
        verbose_name="Organización (Opcional)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:  # pylint: disable=too-few-public-methods
        """Define metadata for SLA policies."""
        verbose_name = "Política de SLA"
        verbose_name_plural = "Políticas de SLA"
        ordering = ['priority']

    def get_priority_display(self):
        """Return the display label for this policy's priority."""
        return dict(self.PRIORITY_CHOICES).get(self.priority, self.priority)

    def __str__(self):
        return f"{self.name} ({self.get_priority_display()})"