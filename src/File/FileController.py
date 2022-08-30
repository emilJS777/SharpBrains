from src.__Parents.Controller import Controller
from .FileService import FileService
from .FileRepository import FileRepository


class FileController(Controller):
    file_service: FileService = FileService(FileRepository())

    def get(self):
        res = self.file_service.download_by_id(self.id)
        return res
