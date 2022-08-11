from abc import ABC, abstractmethod
from .MeetingModel import Meeting


class IMeetingRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, meeting: Meeting, body: dict):
        pass

    @abstractmethod
    def delete(self, meeting: Meeting):
        pass

    @abstractmethod
    def get_by_id(self, meeting_id: int, user_id: int or None = None) -> Meeting:
        pass

    @abstractmethod
    def get_all(self, date_from, date_to) -> list[Meeting]:
        pass
