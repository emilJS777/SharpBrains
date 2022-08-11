from src import api
from .User.UserController import UserController
from .Auth.AuthController import AuthController
from .Sphere.SphereController import SphereController
from .Project.ProjectController import ProjectController
from .Image.ImageController import ImageController
from .UserImage.UserImageController import UserImageController
from .ProjectStatus.ProjectStatusController import ProjectStatusController
from .Meeting.MeetingController import MeetingController
from .ChatMessage.Chat.ChatController import ChatController
from .ChatMessage.Message.MessageController import MessageController

api.add_resource(AuthController, "/auth")
api.add_resource(UserController, "/user")
api.add_resource(SphereController, "/sphere")
api.add_resource(ProjectController, "/project")
api.add_resource(ProjectStatusController, "/project_status")
api.add_resource(ImageController, "/image")
api.add_resource(UserImageController, "/user_image")
api.add_resource(MeetingController, "/meeting")
api.add_resource(ChatController, "/chat")
api.add_resource(MessageController, "/message")
