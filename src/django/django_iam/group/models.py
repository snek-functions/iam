from django.db import models

class GroupManager(models.Manager):
    """
    The manager for the auth's Group model.
    """

    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)

class Group(models.Model):
    """
    Groups are a generic way of categorizing users to apply permissions, or
    some other label, to those users. A user can belong to any number of
    groups.
    A user in a group automatically has all the permissions granted to that
    group. For example, if the group 'Site editors' has the permission
    can_edit_home_page, any user in that group will have that permission.
    Beyond permissions, groups are a convenient way to categorize users to
    apply some label, or extended functionality, to them. For example, you
    could create a group 'Special users', and you could write code that would
    do special things to those users -- such as giving them access to a
    members-only portion of your site, or sending them members-only email
    messages.
    """

    name = models.CharField(
        "name",
        blank=False,
        error_messages={"unique": "A group with that name already exists."},
        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=36,
        unique=True,
    )
    description = models.CharField(
        "description",
        blank=True,
        help_text="280 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=280,
    )
    permissions = models.ManyToManyField(
        "permission.Permission",
        verbose_name="permissions",
        blank=True,
    )

    objects = GroupManager()

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"

    # Custom save function
    def save(self, *args, **kwargs):
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
