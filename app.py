from src import app
from src.__Parents.WSocket import socketio
from src.__Parents.Initializer import Initializer
from src.User.UserRepository import UserRepository
from src.Role.RoleRepository import RoleRepository
from src.Permission.PermissionRepository import PermissionRepository

Initializer(UserRepository(), RoleRepository(), PermissionRepository())
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
