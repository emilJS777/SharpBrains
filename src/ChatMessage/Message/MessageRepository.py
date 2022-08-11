from .IMessageRepo import IMessageRepo
from .MessageModel import Message
from sqlalchemy import or_, and_
from flask import g


class MessageRepository(IMessageRepo):
    def create(self, chat_id: int, body: dict):
        message: Message = Message()
        message.sender_id = g.user.id
        message.addressee_id = body['user_id']
        message.text = body['text']
        message.chat_id = chat_id
        message.save_db()

    def update(self, message: Message, body: dict):
        message.text = body['text']
        message.update_db()

    def delete(self, message: Message):
        message.delete_db()

    def get_by_id(self, message_id: int) -> Message:
        message: Message = Message.query.filter_by(id=message_id, sender_id=g.user.id).first()
        return message

    def get_by_user_id(self, user_id: int) -> Message:
        message: Message = Message.query.filter(
            or_(and_(Message.sender_id == g.user.id, Message.addressee_id == user_id),
                and_(Message.sender_id == user_id, Message.addressee_id == g.user.id))
        ).first()
        return message

    def get_all(self, page: int, per_page: int, chat_id: int):
        messages: list[Message] = Message.query.filter(Message.chat_id == chat_id)\
            .filter(or_(Message.sender_id == g.user.id, Message.addressee_id == g.user.id))\
            .paginate(page=page, per_page=per_page)
        return messages
