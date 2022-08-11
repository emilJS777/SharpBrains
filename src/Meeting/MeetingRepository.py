from .MeetingModel import Meeting
from .IMeetingRepo import IMeetingRepo
from flask import g
from datetime import date
from sqlalchemy import and_, func


class MeetingRepository(IMeetingRepo):

    def create(self, body: dict):
        meeting: Meeting = Meeting()
        meeting.title = body['title']
        meeting.description = body['description']
        meeting.date = body['date']
        meeting.user_id = g.user.id
        meeting.save_db()

    def update(self, meeting: Meeting, body: dict):
        meeting.title = body['title']
        meeting.description = body['description']
        meeting.date = body['date']
        meeting.update_db()

    def delete(self, meeting: Meeting):
        meeting.delete_db()

    def get_by_id(self, meeting_id: int, user_id: int or None = None) -> Meeting:
        meeting: Meeting = Meeting.query.filter(Meeting.id == meeting_id,
                                                Meeting.user_id == user_id if user_id else Meeting.user_id.isnot(None)).first()
        return meeting

    def get_all(self, date_from: date, date_to: date) -> list[Meeting]:
        meetings: list[Meeting] = Meeting.query.filter(Meeting.date >= date_from, Meeting.date <= date_to).all()
        return meetings
