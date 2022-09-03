from django.contrib import admin
from .models import Permission


# Re-register GroupAdmin
admin.site.register(Permission)


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
