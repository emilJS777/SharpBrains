from .IPermissionRepo import IPermissionRepo
from .PermissionModel import Permission


class PermissionRepository(IPermissionRepo):

    def create(self, name: str, description: str):
        permission: Permission = Permission()
        permission.name = name
        permission.description = description
        permission.save_db()

    def update(self, permission: Permission, name: str, description: str):
        permission.name = name
        permission.description = description
        permission.update_db()

    def delete(self, permission: Permission):
        permission.delete_db()

    def get_by_id(self, permission_id: int) -> Permission:
        permission: Permission = Permission.query.filter_by(id=permission_id).first()
        return permission

    def get_by_name(self, name: str) -> Permission:
        permission: Permission = Permission.query.filter_by(name=name).first()
        return permission

    def get_all(self) -> list[Permission]:
        permissions: list[Permission] = Permission.query.all()
        return permissions

