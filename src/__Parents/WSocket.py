from src import socketio
from flask import request
from src.Auth.AuthMiddleware import AuthMiddleware
from flask import g
from flask_socketio import emit


class WSocket:
    sids: list[dict] = []

    # DELETE SID
    def delete_sid(self, disconnect_sid):
        for index in range(len(self.sids)):
            if self.sids[index]['sid'] == disconnect_sid:
                del self.sids[index]
                break

    @staticmethod
    @socketio.on('connect')
    @AuthMiddleware.check_authorize
    def connect():
        sid_user: dict = {'sid': request.sid, 'user_id': g.user.id}
        WSocket.sids.append(sid_user)
        print(WSocket.sids)

    @staticmethod
    @socketio.on('disconnect')
    def disconnect():
        WSocket().delete_sid(disconnect_sid=request.sid)

    def on_emit(self, emit_name: str, data: dict, user_id: int):
        sid = self.get_sid_by_user_id(user_id)
        if sid:
            emit(emit_name, data, namespace=False, room=sid)

    @staticmethod
    def get_sid_by_user_id(user_id: int) -> str or None:
        for sid in WSocket.sids:
            if str(sid['user_id']) == str(user_id):
                return sid['sid']
        return None
