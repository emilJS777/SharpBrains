from .MeetingService import MeetingService
from ..__Parents.Controller import Controller
from .MeetingRepository import MeetingRepository
from flask_expects_json import expects_json
from .MeetingValidator import meeting_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware


class MeetingController(Controller):
    meeting_service: MeetingService = MeetingService(MeetingRepository())

    @expects_json(meeting_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("meeting_edit")
    def post(self) -> dict:
        res: dict = self.meeting_service.create(self.request.get_json())
        return res

    @expects_json(meeting_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("meeting_edit")
    def put(self) -> dict:
        res: dict = self.meeting_service.update(meeting_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("meeting_edit")
    def delete(self) -> dict:
        res: dict = self.meeting_service.delete(meeting_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission("meeting_get")
    def get(self) -> dict:
        if self.id:
            res: dict = self.meeting_service.get_by_id(self.id)
        else:
            res: dict = self.meeting_service.get_all(date_from=self.arguments.get('date_from'),
                                                     date_to=self.arguments.get('date_to'))
        return res
