"""
Setup the proxy handler with `python3 -m django_iam.proxy_handler`
"""

from .init import init_django
from .proxy import ProxyMessage, ProxyServer


def function_handler(message: ProxyMessage):
    from .export import export
    from .user.models import Alias, User

    if message.fnName == 'usersAdd':
        email = message.data.get("email")
        password = message.data.get("password")
        first_name = message.data.get("firstName", "")
        last_name = message.data.get("lastName", "")

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.save()

        # data = {
        #     "id": user.pk,
        #     "name": user.email
        # }

        return {
            "userId": user.pk,
            "email": user.email,
            "firstName": user.details.first_name,
            "lastName": user.details.first_name,
            "isActive": user.is_active,
            "createdAt": str(user.date_joined)
        }

    elif message.fnName == 'usersDelete':
        user_id = message.data.get("userId")

        if (User.objects.get(pk=user_id).delete()):
            return f"Successfully deleted user {user_id}"

    elif message.fnName == 'aliasAvailable':
        user_alias = message.data.get("alias")

        if (Alias.objects.filter(alias=user_alias).exists()):
            return False

        return True

    elif message.fnName == 'usersUpdate':
        user_id = message.data.get("userId")
        first_name = message.data.get("firstName")
        last_name = message.data.get("lastName")
        is_active = message.data.get("isActive") == "true"

        print(last_name)
        user = User.objects.get(pk=user_id)
        # user.is_active=True,
        # user.save()

        user.details.first_name = first_name or ""
        user.details.last_name = last_name or ""
        user.details.save()

        return {
            "userId": user.pk,
            "email": user.email,
            "firstName": user.details.first_name,
            "lastName": user.details.last_name,
            "isActive": user.is_active,
            "createdAt": str(user.date_joined)
        }

    elif message.fnName == 'usersGet':
        qs = User.objects.all()

        return [{
            "userId": user.pk,
            "email": user.email,
            "firstName": user.details.first_name,
            "lastName": user.details.last_name,
            "isActive": user.is_active,
            "createdAt": str(user.date_joined)
        } for user in qs]

    elif message.fnName == 'publishAuth':
        return export()

    elif message.fnName == 'userGet':
        user = User.objects.get(pk=message.data.get("userId"))
        alias = Alias.objects.get(user=user)

        return {
            "userId": user.pk,
            "email": user.email,
            "firstName": user.details.first_name,
            "lastName": user.details.last_name,
            "isActive": user.is_active,
            "createdAt": str(user.date_joined)
        }
    return 'Unknown function'


ProxyServer(setup_fn=init_django).handle(function_handler)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
