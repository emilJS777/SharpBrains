from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IMessageRepo import IMessageRepo
from ..Chat.IChatRepo import IChatRepo


class MessageService(Service, Repository):
    def __init__(self, message_repository: IMessageRepo, chat_repository: IChatRepo):
        self.message_repository: IMessageRepo = message_repository
        self.chat_repository: IChatRepo = chat_repository

    def create(self, body: dict) -> dict:
        chat = self.chat_repository.get_by_user_id(body['user_id']) \
               or self.chat_repository.create(body['user_id'])

        self.message_repository.create(chat_id=chat.id, body=body)
        self.chat_repository.update(chat)
        return self.response_created('message successfully created')

    def update(self, message_id: int, body: dict) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message:
            return self.response_not_found('message not found')

        self.message_repository.update(message=message, body=body)
        return self.response_updated('message successfully updated')

    def delete(self, message_id: int) -> dict:
        message = self.message_repository.get_by_id(message_id)
        if not message:
            return self.response_not_found('message not found')

        self.message_repository.delete(message)
        return self.response_deleted('message successfully deleted')

    def get_all(self, page: int, per_page: int, chat_id: int) -> dict:
        messages = self.message_repository.get_all(page=page, per_page=per_page, chat_id=chat_id)
        return self.response_ok(self.get_page_items(messages))
