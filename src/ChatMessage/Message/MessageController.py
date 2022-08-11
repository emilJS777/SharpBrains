from src.__Parents.Controller import Controller
from .MessageService import MessageService
from .MessageRepository import MessageRepository
from ..Chat.ChatRepository import ChatRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class MessageController(Controller):
    message_service: MessageService = MessageService(MessageRepository(), ChatRepository())

    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.message_service.create(self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.message_service.update(message_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.message_service.delete(message_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.message_service.get_all(
            page=self.page,
            per_page=self.per_page,
            chat_id=self.arguments.get('chat_id'))
        return res
