from src.__Parents.Controller import Controller
from .RoleRepository import RoleRepository
from ..Permission.PermissionMiddleware import PermissionMiddleware
from ..Permission.PermissionRepository import PermissionRepository
from .RoleService import RoleService
from flask_expects_json import expects_json
from .RoleValidator import role_schema
from src.Auth.AuthMiddleware import AuthMiddleware


class RoleController(Controller):
    role_service: RoleService = RoleService(RoleRepository(), PermissionRepository())

    @expects_json(role_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("role_edit")
    def post(self) -> dict:
        res: dict = self.role_service.create(self.request.get_json())
        return res

    @expects_json(role_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("role_edit")
    def put(self) -> dict:
        res: dict = self.role_service.update(role_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("role_edit")
    def delete(self) -> dict:
        res: dict = self.role_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.role_service.get_by_id(self.id)
        else:
            res: dict = self.role_service.get_all()
        return res
