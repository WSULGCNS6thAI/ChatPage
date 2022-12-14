# 모듈 임포트 - 김경호 22.10.26
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# 메인페이지 출력 - 김경호 22.10.26
@app.route('/')
def sessions():
    return render_template('index.html')

# 소켓IO 코드 작성 - 오유빈
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json_msg, methods=['GET', 'POST']):
    print('received my event : ' + str(json_msg))
    socketio.emit('my response', json_msg, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)