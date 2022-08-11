from src.__Parents.Controller import Controller
from .ImageService import ImageService
from .ImageRepository import ImageRepository
from flask import request
from src.Auth.AuthMiddleware import AuthMiddleware


class ImageController(Controller):
    image_service: ImageService = ImageService(ImageRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.image_service.create(image=request.files["image"])
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.image_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.image_service.get_by_id(self.id)
        else:
            res: dict = self.image_service.get_all()
        return res
