from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IMessageRepo import IMessageRepo
from ..Chat.IChatRepo import IChatRepo
from src.__Parents.WSocket import WSocket
from src.__Parents.File import File
from flask import g
from src import app
from src.File.IFileRepo import IFileRepo


class MessageService(Service, Repository, File, WSocket):
    def __init__(self, message_repository: IMessageRepo, chat_repository: IChatRepo, file_repository: IFileRepo):
        self.message_repository: IMessageRepo = message_repository
        self.chat_repository: IChatRepo = chat_repository
        self.file_repository: IFileRepo = file_repository

    def create(self, body: dict, file) -> dict:
        chat = self.chat_repository.get_by_user_id(body['user_id']) \
               or self.chat_repository.create(body['user_id'])

        file_id = None
        if file:
            filename = self.save_file(file_path=app.config['FILE_PATH'], file=file)
            file = self.file_repository.create(filename)
            file_id = file.id

        message = self.message_repository.create(chat_id=chat.id,
                                                 body=body,
                                                 addressee_id=body['user_id'],
                                                 file_id=file_id)
        self.chat_repository.update(chat)

        message_dict: dict = {'id': message.id,
                              'sender_id': message.sender_id,
                              'addressee_id': message.addressee_id,
                              'text': message.text,
                              'file_id': message.file_id,
                              'file': self.get_dict_items(message.file),
                              'reading': message.reading}

        self.on_emit(emit_name="message", data=message_dict, user_id=body['user_id'])
        return self.response_ok(message_dict)

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

        if message.file_id:
            file = self.file_repository.get_by_id(file_id=message.file_id)
            self.file_repository.delete(file)
            self.delete_file(file_path=file.filename, dir_path=app.config['FILE_PATH'])
        return self.response_deleted('message successfully deleted')

    def get_all(self, page: int, per_page: int, chat_id: int) -> dict:
        messages = self.message_repository.get_all(page=page, per_page=per_page, chat_id=chat_id)
        for message in messages.items:
            message.file = message.file
        return self.response_ok(self.get_page_items(messages))

    def reading(self, body: dict) -> dict:
        messages = self.message_repository.read_messages_by_ids_by_addressee_id(message_ids=body['message_ids'], addressee_id=g.user.id)
        self.on_emit(emit_name="read_message", data=body, user_id=messages[0].sender_id)
        return self.response_updated('messages successfully reading')
