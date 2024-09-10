from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('response', {'data': 'Message received!'})

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('response', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
