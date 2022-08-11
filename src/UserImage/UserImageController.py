from src.__Parents.Controller import Controller
from .UserImageRepository import UserImageRepository
from .UserImageService import UserImageService
from flask import request
from src.Auth.AuthMiddleware import AuthMiddleware


class UserImageController(Controller):
    user_image_service: UserImageService = UserImageService(UserImageRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.user_image_service.create(image=request.files['image'], main=bool(self.arguments.get('main')))
        return res

    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.user_image_service.update(image_id=self.id, main=bool(self.arguments.get('main') == 'true'))
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.user_image_service.delete(image_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.user_image_service.get_all()
        return res
