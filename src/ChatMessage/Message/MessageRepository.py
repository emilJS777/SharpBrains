from .IMessageRepo import IMessageRepo
from .MessageModel import Message
from sqlalchemy import or_, and_
from flask import g


class MessageRepository(IMessageRepo):
    def create(self, chat_id: int, addressee_id: int, body: dict, file_id: int or None) -> Message:
        message: Message = Message()
        message.sender_id = g.user.id
        message.addressee_id = addressee_id
        message.text = body['text']
        message.chat_id = chat_id
        message.file_id = file_id
        message.save_db()
        return message

    def update(self, message: Message, body: dict):
        message.text = body['text']
        message.update_db()

    def delete(self, message: Message):
        message.delete_db()

    def get_by_id(self, message_id: int) -> Message:
        message: Message = Message.query.filter_by(id=message_id, sender_id=g.user.id).first()
        return message

    def read_messages_by_ids_by_addressee_id(self, message_ids: list[int], addressee_id: int) -> list[Message]:
        messages = Message.query.filter(Message.id.in_(message_ids), Message.addressee_id == addressee_id).all()
        for message in messages:
            message.reading = True
        Message.update_db()
        return messages

    def get_by_user_id(self, user_id: int) -> Message:
        message: Message = Message.query.filter(
            or_(and_(Message.sender_id == g.user.id, Message.addressee_id == user_id),
                and_(Message.sender_id == user_id, Message.addressee_id == g.user.id))
        ).first()
        return message

    def get_all(self, page: int, per_page: int, chat_id: int):
        messages: list[Message] = Message.query.filter(Message.chat_id == chat_id)\
            .filter(or_(Message.sender_id == g.user.id, Message.addressee_id == g.user.id))\
            .order_by(-Message.creation_date).paginate(page=page, per_page=per_page)
        return messages
