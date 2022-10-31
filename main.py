# 모듈 임포트 - 김경호
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# 메인페이지 출력 - 김경호
@app.route('/')
def sessions():
    return render_template('index.html')

# 소켓IO 코드 작성 - 오유빈
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event : ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)