from django.db import models
from django_iam.ressource.models import Ressource


class Permission(models.Model):
    name = models.CharField(
        "name",
        null=True,
        blank=False,
        error_messages={"unique": "A permission with that name already exists."},
        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=36,
        unique=True,
    )
    description = models.CharField(
        "description",
        null=True,
        blank=False,
        help_text="280 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=280,
    )
    codename = models.CharField("codename", max_length=100)
    ressources = models.ForeignKey("ressource.Ressource", related_name="permissions", on_delete=models.CASCADE)

    # Custom save function
    def save(self, *args, **kwargs):
        super(Permission, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
