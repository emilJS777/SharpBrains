from src.__Parents.Controller import Controller
from .ChatRepository import ChatRepository
from .ChatService import ChatService
from src.Auth.AuthMiddleware import AuthMiddleware


class ChatController(Controller):
    chat_service: ChatService = ChatService(ChatRepository())

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.chat_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.chat_service.get_all(page=self.page, per_page=self.per_page)
        return res
