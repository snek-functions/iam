import uuid
import django.contrib.auth.validators
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import \
    PermissionsMixin as DjangoPermissionsMixin
from django.db import models
from django.utils import timezone


class PermissionsMixin(DjangoPermissionsMixin):
    """
    Add the fields and methods necessary to support the Group and Permission
    models using the ModelBackend.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_superuser = None
    groups = models.ManyToManyField(
        "group.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions "
        "granted to each of their groups.",
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "permission.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="user_set",
        related_query_name="user",
    )


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, permissionsmixin_id, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        
        if permissionsmixin_id:
            permissionsmixin = PermissionsMixin(id=uuid.UUID(permissionsmixin_id))
            user = self.model(permissionsmixin_ptr=permissionsmixin,email=email, is_active=True)
        else:
            user = self.model(email=email, is_active=True)

        if password.split("$")[0] == "pbkdf2_sha256":
            user.password = password
        else:
            user.password = make_password(password)

        user.save(using=self._db)

        details = Details(user=user, **extra_fields)
        details.save()

        return user

    def create_user(self, permissionsmixin_id=None, email=None, password=None, **extra_fields):
        return self._create_user(permissionsmixin_id, email, password, **extra_fields)

    # def create_superuser(self, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")

    #     return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Email and password are required. Other fields are optional.
    """
    # first_name = models.CharField("first name", max_length=150, blank=True)
    # last_name = models.CharField("last name", max_length=150, blank=True)
    email = models.EmailField("email address",
                              blank=True,
                              unique=True,
                              help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                              error_messages={
                                  "unique": "A user with that email address already exists.",
                              },
                              )
    # is_staff = models.BooleanField(
    #     "staff status",
    #     default=False,
    #     help_text=_("Designates whether the user can log into this admin site."),
    # )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)
    last_login = None

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["email"]

    # first_name = models.CharField("first name", max_length=150, blank=True)
    # last_name = models.CharField("last name", max_length=150, blank=True)
    # email = models.EmailField("email address", blank=True)
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    # permissions = models.ManyToManyField(
    #     "permission.Permission",
    #     verbose_name="permissions",
    #     blank=True,
    # )
    # groups = models.ManyToManyField(
    #     "group.Group",
    #     verbose_name="groups",
    #     blank=True,
    #     help_text="The groups this user belongs to. A user will get all permissions "
    #     "granted to each of their groups.",
    # )

    USERNAME_FIELD = 'email'

    # Custom save function
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        alias = Alias(user=self, alias=self.email)
        alias.save()

    def __str__(self):
        return f"{self.email}"


class Alias(models.Model):
    alias = models.CharField(
        "alias",
        blank=False,
        error_messages={"unique": "A user with that alias already exists."},
        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
        default="",
        max_length=36,
        unique=True,
        primary_key=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
    )
    user = models.ForeignKey(
        User, related_name="aliases", on_delete=models.CASCADE)

    objects = models.Manager()

    # Custom save function
    def save(self, *args, **kwargs):
        super(Alias, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.alias}"


class Details(models.Model):
    user = models.OneToOneField(
        User, related_name="details", on_delete=models.CASCADE)
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
