import uuid
from django.utils import timezone
from django.db import models


class Role(models.Model):
    name = models.CharField(
        "name",
        null=True,
        blank=False,
        error_messages={"unique": "A role with that name already exists."},
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
    permissions = models.ManyToManyField(
        "permission.Permission",
        verbose_name="permissions",
        blank=True,
    )


    # Custom save function
    def save(self, *args, **kwargs):
        super(Role, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Accesstoken(models.Model):
    jti = models.CharField("jwt id", primary_key=True, max_length=32, default=uuid.uuid4, editable=False)
    name = models.CharField(
        "name",
        null=True,
        blank=False,
        error_messages={"unique": "A access token with that name already exists."},
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
    subject = models.ForeignKey("user.User", related_name="roles", on_delete=models.CASCADE)
    date_issued  = models.DateTimeField("date joined", default=timezone.now)
    date_expired = models.DateTimeField("date joined", default=timezone.now)


    # Custom save function
    def save(self, *args, **kwargs):
        super(Accesstoken, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
