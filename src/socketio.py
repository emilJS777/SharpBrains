from flask_socketio import Namespace, emit
from src import socketio


class MyCustomNamespace(Namespace):
    def on_connect(self):
        print("connnnnnnneeeeccttt **********")
        pass

    def on_disconnect(self):
        pass

    def on_my_event(self, data):
        emit('my_response', data)


socketio.on_namespace(MyCustomNamespace('/'))
