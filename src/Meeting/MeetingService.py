from src.__Parents.Service import Service
from .IMeetingRepo import IMeetingRepo
from ..__Parents.Repository import Repository
from flask import g
from datetime import datetime


class MeetingService(Service, Repository):
    def __init__(self, meeting_repository: IMeetingRepo):
        self.meeting_repository: IMeetingRepo = meeting_repository

    def create(self, body: dict) -> dict:
        self.meeting_repository.create(body)
        return self.response_created('meeting successfully created')

    def update(self, meeting_id: int, body: dict) -> dict:
        meeting = self.meeting_repository.get_by_id(meeting_id=meeting_id, user_id=g.user.id)

        if not meeting:
            return self.response_not_found('meeting not found')

        self.meeting_repository.update(meeting=meeting, body=body)
        return self.response_updated('meeting successfully updated')

    def delete(self, meeting_id: int) -> dict:
        meeting = self.meeting_repository.get_by_id(meeting_id=meeting_id, user_id=g.user.id)

        if not meeting:
            return self.response_not_found('meeting not found')

        self.meeting_repository.delete(meeting)
        return self.response_deleted('meeting successfully deleted')

    def get_by_id(self, meeting_id: int) -> dict:
        meeting = self.meeting_repository.get_by_id(meeting_id)
        if not meeting:
            return self.response_not_found('meeting not found')
        meeting.date = datetime.strftime(meeting.date, "%Y-%m-%d")
        return self.response_ok(self.get_dict_items(meeting))

    def get_all(self, date_from: str, date_to: str) -> dict:
        meetings = self.meeting_repository.get_all(date_from=date_from, date_to=date_to)
        for meeting in meetings:
            meeting.date = datetime.strftime(meeting.date, "%Y-%m-%d")
        return self.response_ok(self.get_array_items(meetings))
