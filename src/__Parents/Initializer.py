from src.User.IUserRepo import IUserRepo
from src.Role.IRoleRepo import IRoleRepo
from src.Permission.IPermissionRepo import IPermissionRepo
from src.__Parents.Service import Service


class Initializer(Service):
    user: dict = {'first_name': 'admin', 'last_name': 'adminyan', 'email_address': 'admin123@mail.ru', 'password': 'admin123'}
    role: dict = {'name': 'Admin', 'description': ''}
    permissions: list[dict] = [
        {'name': 'user_edit', 'description': 'user edit'},
        {'name': 'about_us_edit', 'description': 'about us edit'},
        {'name': 'meeting_edit', 'description': 'meeting edit'}, {'name': 'meeting_get', 'description': 'meeting get'},
        {'name': 'project_edit', 'description': 'project edit'},
        {'name': 'project_status_edit', 'description': 'project status edit'},
        {'name': 'sphere_edit', 'description': 'sphere edit'},
        {'name': 'role_edit', 'description': 'role edit'}]

    def __init__(self, user_repository: IUserRepo, role_repository: IRoleRepo, permission_repository: IPermissionRepo):
        self.user_repository: IUserRepo = user_repository
        self.role_repository: IRoleRepo = role_repository
        self.permission_repository: IPermissionRepo = permission_repository

        self.permissions_init()
        self.role_init()
        self.user_init()

    def permissions_init(self):
        for self_permission in self.permissions:
            if not self.permission_repository.get_by_name(self_permission['name']):
                self.permission_repository.create(name=self_permission['name'], description=self_permission['description'])

    def role_init(self):
        role = self.role_repository.get_by_name(self.role['name'])
        if not role:
            role = self.role_repository.create(
                name=self.role['name'],
                description=self.role['description'],
                permissions=self.permission_repository.get_all(),
                creator_id=None)
        return role

    def user_init(self):
        user = self.user_repository.get_by_email_address(self.user['email_address'])
        if not user:
            self.user['role_id'] = self.role_repository.get_by_name(self.role['name']).id
            user = self.user_repository.create(body=self.user, ticket=self.generate_ticket_code(), projects=[])
            print(f"new admin user created, ticket={user.ticket}")
