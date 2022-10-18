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
        first_name = message.data.get("firstName", "").upper()
        last_name = message.data.get("lastName", "").upper()
        permissionsmixin_id = message.data.get("userId", "")
        
        user = User.objects.create_user(
            email=email,
            password=password,
            permissionsmixin_id=permissionsmixin_id,
            first_name=first_name,
            last_name=last_name
        )

        user.save()

        # data = {
        #     "id": str(user.pk),
        #     "name": user.email
        # }

        return {
            "userId": str(user.pk),
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
        email = message.data.get("email")
        password = message.data.get("password")
        first_name = message.data.get("firstName").upper()
        last_name = message.data.get("lastName").upper()
        is_active = message.data.get("isActive") == True

        print(f"Is Active test: {message.data.get('isActive')}")
        print(f"2 {is_active}")
        
        user = User.objects.get(pk=user_id)
        # user.is_active=True,
        # user.save()

        # This may not be the best way to do this but it works for now
        # Update values if they are not None
        if email is not None:
            user.email = email
        if first_name is not None:
            user.details.first_name = first_name
        if last_name is not None:
            user.details.last_name = last_name
        if is_active is not None:
            user.is_active = is_active

        # Update password if it is not None
        if password is not None:
            user.set_password(password)
        
        
        user.save()
        user.details.save()

        return {
            "userId": str(user.pk),
            "email": user.email,
            "firstName": user.details.first_name,
            "lastName": user.details.last_name,
            "isActive": user.is_active,
            "createdAt": str(user.date_joined)
        }

    elif message.fnName == 'usersGet':
        qs = User.objects.all()

        return [{
            "userId": str(user.pk),
            "email": user.email,
            "firstName": user.details.first_name,
            "lastName": user.details.last_name,
            "isActive": user.is_active,
            "createdAt": str(user.date_joined)
        } for user in qs]

    elif message.fnName == 'publishAuth':
        return export()

    elif message.fnName == 'userGet':

        user_id = message.data.get("userId")
        alias = message.data.get("alias")

        if user_id is not None:
            user = User.objects.get(pk=user_id)
        elif alias is not None:
            alias = Alias.objects.get(alias=alias)
            user = alias.user
        else:
            raise 'No user id or alias provided'

        return {
            "userId": str(user.pk),
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
