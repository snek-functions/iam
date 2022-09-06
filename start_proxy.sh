#!/usr/bin/env bash

python3 -m venv venv
cd src/django
../../venv/bin/python3 -m django_iam.proxy_handler

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at