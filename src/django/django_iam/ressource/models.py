import django.contrib.auth.validators
from django.db import models


class Ressource(models.Model):
    name = models.CharField(
        "name",
        null=True,
        blank=False,
        error_messages={"unique": "A ressource with that name already exists."},
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


    # Custom save function
    def save(self, *args, **kwargs):
        super(Ressource, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
