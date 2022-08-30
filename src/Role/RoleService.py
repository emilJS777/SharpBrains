from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IRoleRepo import IRoleRepo
from ..Permission.IPermissionRepo import IPermissionRepo
from flask import g


class RoleService(Service, Repository):
    def __init__(self, role_repository: IRoleRepo, permission_repository: IPermissionRepo):
        self.role_repository: IRoleRepo = role_repository
        self.permission_repository: IPermissionRepo = permission_repository

    @staticmethod
    def allowed_user_permissions(permission_ids: list[int]) -> list[int]:
        allowed_permissions: list = []
        for permission_id in permission_ids:
            for user_permission in g.user.role.permissions:
                if user_permission.id == permission_id:
                    allowed_permissions.append(user_permission)
        return allowed_permissions

    def create(self, body: dict) -> dict:
        if self.role_repository.get_by_name(body['name']):
            return self.response_conflict('role by this name exist')
        print(self.allowed_user_permissions(body['permission_ids']))
        self.role_repository.create(
            name=body['name'],
            description=body['description'],
            permissions=self.allowed_user_permissions(body['permission_ids']),
            creator_id=g.user.id
        )

        return self.response_created('role successfully created')

    def update(self, role_id: int, body: dict) -> dict:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return self.response_not_found('role not found')

        if self.role_repository.get_by_name_exclude_id(role_id=role_id, name=body['name']):
            return self.response_conflict('role by this name exist')

        self.role_repository.update(role=role,
                                    name=body['name'],
                                    description=body['description'],
                                    permissions=self.allowed_user_permissions(body['permission_ids']))
        return self.response_updated('role successfully updated')

    def delete(self, role_id: int) -> dict:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return self.response_not_found('role not found')

        self.role_repository.delete_role_permission_binds_by_role_id(role.id)
        self.role_repository.delete(role)
        return self.response_deleted('role successfully deleted')

    def get_by_id(self, role_id: int) -> dict:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return self.response_not_found('role not found')

        return self.response_ok({
            'id': role.id,
            'name': role.name,
            'description': role.description,
            'permissions': self.get_array_items(role.permissions)})

    def get_all(self) -> dict:
        roles = self.role_repository.get_all()
        return self.response_ok(self.get_array_items(roles))
