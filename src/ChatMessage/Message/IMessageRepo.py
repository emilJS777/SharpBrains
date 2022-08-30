from abc import ABC, abstractmethod
from .MessageModel import Message


class IMessageRepo(ABC):
    @abstractmethod
    def create(self, chat_id: int, addressee_id: int, body: dict, file_id: int or None) -> Message:
        pass

    @abstractmethod
    def update(self, message: Message, body: dict):
        pass

    @abstractmethod
    def delete(self, message: Message):
        pass

    @abstractmethod
    def get_by_id(self, message_id: int) -> Message:
        pass

    @abstractmethod
    def read_messages_by_ids_by_addressee_id(self, message_ids: list[int], addressee_id: int) -> list[Message]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Message:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, chat_id: int):
        pass
