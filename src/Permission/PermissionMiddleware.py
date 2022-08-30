from functools import wraps
from flask import g, request
from src.Permission.PermissionRepository import PermissionRepository
from src.__Parents.Service import Service


class PermissionMiddleware(Service):
    permission_repository = PermissionRepository()

    @staticmethod
    def check_permission(permission_name):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):
                print(g.user)
                if g.user.role:
                    for permission in g.user.role.permissions:
                        if permission.name == permission_name:
                            return f(*args, **kwargs)

                return PermissionMiddleware.response_forbidden('forbidden')
            return decoration_function
        return decoration
