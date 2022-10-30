from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/<username>/')
# def username(username):
#     return 'username = '+username

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

#소켓아이오로 받기
@socketio.on('message')
def handle_message(msg):
    print('message: ' + str(msg))
    socketio.emit('my response', msg, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)

app.run(debug=True)