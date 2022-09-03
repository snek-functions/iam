"""
Setups the django environment.
"""

import sys
import os
import django


def init_django():
    """
    Initializes the django environment.
    """
    sys.dont_write_bytecode = True
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_iam.settings.development')
    django.setup()
    django.core.management.call_command("migrate", no_input=True)

    print('Django environment initialized.')

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
