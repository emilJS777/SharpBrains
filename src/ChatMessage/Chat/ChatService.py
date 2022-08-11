from src.__Parents.Service import Service
from .IChatRepo import IChatRepo


class ChatService(Service):
    def __init__(self, chat_repository: IChatRepo):
        self.chat_repository: IChatRepo = chat_repository

    def delete(self, chat_id: int) -> dict:
        chat = self.chat_repository.get_by_id(chat_id)
        if not chat:
            return self.response_not_found('chat not found')

        self.chat_repository.delete(chat)
        return self.response_deleted('chat successfully deleted')

    def get_all(self, page: int, per_page: int) -> dict:
        chats = self.chat_repository.get_all(page=page, per_page=per_page)
        return self.response_ok(chats)
