from src.__Parents.Controller import Controller
from .AboutUsService import AboutUsService
from .AboutUsRepository import AboutUsRepository
from flask_expects_json import expects_json
from .AboutUsValidator import about_us_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware


class AboutUsController(Controller):
    about_us_service: AboutUsService = AboutUsService(AboutUsRepository())

    @expects_json(about_us_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("about_us_edit")
    def post(self) -> dict:
        res: dict = self.about_us_service.create(self.request.get_json())
        return res

    @expects_json(about_us_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("about_us_edit")
    def put(self) -> dict:
        res: dict = self.about_us_service.update(about_us_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("about_us_edit")
    def delete(self) -> dict:
        res: dict = self.about_us_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.about_us_service.get_by_id(self.id)
        else:
            res: dict = self.about_us_service.get_all()
        return res
