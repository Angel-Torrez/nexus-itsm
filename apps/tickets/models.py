from django.db import models
from django.conf import settings
from apps.organizations.models import Organization
from apps.sla.models import SLAPolicy

class Ticket(models.Model):
    """Representa un ticket de soporte o incidente dentro de NEXUS ITSM."""

    STATUS_CHOICES = [
        ('OPEN', 'Abierto'),
        ('IN_PROGRESS', 'En Progreso'),
        ('PENDING', 'Pendiente'),
        ('RESOLVED', 'Resuelto'),
        ('CLOSED', 'Cerrado'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Baja'),
        ('MEDIUM', 'Media'),
        ('HIGH', 'Alta'),
        ('CRITICAL', 'Crítica'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='OPEN', 
        verbose_name="Estado"
    )
    priority = models.CharField(
        max_length=20, 
        choices=PRIORITY_CHOICES, 
        default='MEDIUM', 
        verbose_name="Prioridad"
    )

    # Relaciones principales del sistema
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name="Organización"
    )
    sla_policy = models.ForeignKey(
        SLAPolicy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tickets',
        verbose_name="Política SLA"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tickets',
        verbose_name="Creado por"
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
        verbose_name="Asignado a"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    resolved_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de resolución")

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ['-created_at']

    def __str__(self):
        status_display = dict(self.STATUS_CHOICES).get(self.status, self.status)
        return f"#{self.pk} - {self.title} ({status_display})"