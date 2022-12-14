# Generated by Django 4.1.1 on 2022-09-29 10:39

from django.db import migrations, models
import django_iam.group.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("permission", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                            "unique": "A group with that name already exists."
                        },
                        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=36,
                        unique=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="280 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=280,
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
            options={
                "verbose_name": "group",
                "verbose_name_plural": "groups",
            },
            managers=[
                ("objects", django_iam.group.models.GroupManager()),
            ],
        ),
    ]
