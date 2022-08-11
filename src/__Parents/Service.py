from flask import make_response, jsonify
from src import app
from datetime import datetime
import os, base64


class Service:
    # IMAGE LOGIC ***
    @staticmethod
    def get_encode_image(image_path, dir_path):
        with open(os.path.join(dir_path, image_path), 'rb') as binary_file:
            base64_encoded_data = base64.b64encode(binary_file.read())
            return str(base64_encoded_data.decode('utf-8'))

    @staticmethod
    def save_image(image_path: str, image):
        filename = f"{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}"
        image.save(os.path.join(image_path, filename))
        return filename

    @staticmethod
    def delete_image(image_path, dir_path):
        os.remove(dir_path + '/' + image_path)

    # RESPONSES ***
    @staticmethod
    def response(success, obj, status_code) -> make_response:
        return make_response(jsonify(success=success, obj=obj), status_code)

    @staticmethod
    def response_conflict(msg=None):
        return Service.response(False, {'msg': msg or 'exist'}, 409)

    @staticmethod
    def response_not_found(msg=None):
        return Service.response(False, {'msg': msg or 'not found'}, 404)

    @staticmethod
    def response_invalid_password():
        return Service.response(False, {'msg': 'incorrect password'}, 403)

    @staticmethod
    def response_created(msg=None):
        return Service.response(True, {'msg': msg or 'successfully created'}, 201)

    @staticmethod
    def response_err_msg(msg):
        return Service.response(False, {'msg': msg}, 200)

    @staticmethod
    def response_updated(msg=None):
        return Service.response(True, {'msg': msg or 'successfully updated'}, 200)

    @staticmethod
    def response_ok(obj):
        return Service.response(True, obj, 200)

    @staticmethod
    def response_deleted(msg=None):
        return Service.response(True, {'msg': msg or 'successfully deleted'}, 200)

    @staticmethod
    def response_invalid_login():
        return Service.response(False, {'msg': 'invalid username and/or password'}, 401)

    @staticmethod
    def response_forbidden(msg=None):
        return Service.response(False, {'msg': msg or 'forbidden'}, 403)