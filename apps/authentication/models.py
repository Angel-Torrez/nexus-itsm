from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        SUPERVISOR = "SUPERVISOR", "Supervisor"
        TECHNICIAN = "TECHNICIAN", "Técnico"
        REQUESTER = "REQUESTER", "Usuario Solicitante"

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.REQUESTER,
    )

    def __str__(self) -> str:
        role_display = dict(self.Role.choices).get(self.role, self.role)
        return f"{self.username} ({role_display})"