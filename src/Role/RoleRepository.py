from .IRoleRepo import IRoleRepo
from .RoleModel import Role, RolePermission


class RoleRepository(IRoleRepo):

    def create(self, name: str, description: str, permissions: list, creator_id: int or None):
        role: Role = Role()
        role.name = name
        role.description = description
        role.permissions = permissions
        role.creator_id = creator_id
        role.save_db()

    def update(self, role: Role, name: str, description: str, permissions: list):
        role.name = name
        role.description = description
        role.permissions = permissions
        role.update_db()

    def delete(self, role: Role):
        role.delete_db()

    def get_by_id(self, role_id: int) -> Role:
        role: Role = Role.query.filter_by(id=role_id).first()
        return role

    def get_by_name(self, name: str) -> Role:
        role: Role = Role.query.filter_by(name=name).first()
        return role

    def get_by_name_exclude_id(self, role_id: int, name: str) -> Role:
        role: Role = Role.query.filter(Role.name == name, Role.id != role_id).first()
        return role

    def get_all(self) -> list[Role]:
        roles: list[Role] = Role.query.filter(Role.creator_id.isnot(None)).all()
        return roles

    def delete_role_permission_binds_by_role_id(self, role_id: int):
        RolePermission.query.filter_by(role_id=role_id).delete()
