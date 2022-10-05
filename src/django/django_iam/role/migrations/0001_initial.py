# Generated by Django 4.1.1 on 2022-09-29 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("permission", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        error_messages={
                            "unique": "A role with that name already exists."
                        },
                        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=36,
                        null=True,
                        unique=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="280 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=280,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        to="permission.permission",
                        verbose_name="permissions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accesstoken",
            fields=[
                (
                    "jti",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=32,
                        primary_key=True,
                        serialize=False,
                        verbose_name="jwt id",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        error_messages={
                            "unique": "A access token with that name already exists."
                        },
                        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=36,
                        null=True,
                        unique=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="280 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=280,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "date_issued",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "date_expired",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="roles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
