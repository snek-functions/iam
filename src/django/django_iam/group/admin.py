from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group as DjangoGroup
from .models import Group

class GroupInline(admin.StackedInline):
    model = Group
    can_delete = False
    verbose_name_plural = 'custom groups'


class GroupAdmin(BaseGroupAdmin):
    inlines = (GroupInline, )


# Re-register GroupAdmin
admin.site.unregister(DjangoGroup)
admin.site.register(Group)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
