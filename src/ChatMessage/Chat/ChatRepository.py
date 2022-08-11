from .IChatRepo import IChatRepo
from .ChatModel import Chat
from flask import g
from sqlalchemy import or_, and_
from ..Message.MessageModel import Message
from ...__Parents.Repository import Repository
import time


class ChatRepository(IChatRepo, Repository):
    def create(self, user_id: int):
        chat: Chat = Chat()
        chat.user1_id = g.user.id
        chat.user2_id = user_id
        chat.last_update = time.localtime()
        chat.save_db()
        return chat

    def update(self, chat: Chat):
        chat.last_update = time.localtime()
        chat.update_db()

    def delete(self, chat: Chat):
        chat.delete_db()

    def get_by_id(self, chat_id: int) -> Chat:
        chat: Chat = Chat.query.filter_by(id=chat_id).first()
        return chat

    def get_by_user_id(self, user_id: int) -> Chat:
        chat: Chat = Chat.query.filter(or_(
            and_(Chat.user1_id == g.user.id, Chat.user2_id == user_id),
            and_(Chat.user1_id == user_id, Chat.user2_id == g.user.id)
        )).first()
        return chat

    def get_all(self, page: int, per_page: int) -> dict:
        chats: Chat = Chat.query.filter(or_(Chat.user1_id == g.user.id, Chat.user2_id == g.user.id)).order_by(-Chat.last_update)\
            .paginate(page=page, per_page=per_page)
        return self.get_page_items(chats)
