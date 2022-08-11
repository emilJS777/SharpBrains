from .SphereService import SphereService
from .SphereRepository import SphereRepository
from ..__Parents.Controller import Controller
from flask_expects_json import expects_json
from .SphereValidator import sphere_schema
from src.Auth.AuthMiddleware import AuthMiddleware


class SphereController(Controller):
    sphere_service: SphereService = SphereService(SphereRepository())

    @expects_json(sphere_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.sphere_service.create(body=self.request.get_json())
        return res

    @expects_json(sphere_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.sphere_service.update(sphere_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.sphere_service.delete(sphere_id=self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.sphere_service.get_by_id(sphere_id=self.id)
        else:
            res: dict = self.sphere_service.get_all()
        return res
