from .UserService import UserService
from .UserRepository import UserRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask import g
from flask_expects_json import expects_json
from .UserValidator import user_schema


class UserController(Controller):
    user_service: UserService = UserService(UserRepository())

    @expects_json(user_schema)
    def post(self) -> dict:
        res: dict = self.user_service.create(self.request.get_json())
        return res

    @expects_json(user_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.user_service.update(user_id=g.user.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.user_service.delete(g.user.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.user_service.get_by_id(self.id)
        else:
            res: dict = self.user_service.get_all(page=self.page, per_page=self.per_page)
        return res
