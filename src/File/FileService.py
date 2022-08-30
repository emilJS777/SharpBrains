from flask import send_from_directory
from src import app
from src.__Parents.Service import Service
from .IFileRepo import IFileRepo


class FileService(Service):
    def __init__(self, file_repository: IFileRepo):
        self.file_repository: IFileRepo = file_repository

    def download_by_id(self, file_id: int):
        file = self.file_repository.get_by_id(file_id=file_id)
        if not file:
            return self.response_not_found("file not found")

        return send_from_directory("../"+app.config["FILE_PATH"], file.filename, as_attachment=True)
