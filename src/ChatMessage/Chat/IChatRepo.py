from abc import ABC, abstractmethod
from .ChatModel import Chat


class IChatRepo(ABC):
    @abstractmethod
    def create(self, user_id: int):
        pass

    @abstractmethod
    def update(self, chat: Chat):
        pass

    @abstractmethod
    def delete(self, chat: Chat):
        pass

    @abstractmethod
    def get_by_id(self, chat_id: int) -> Chat:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Chat:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int) -> dict:
        pass
