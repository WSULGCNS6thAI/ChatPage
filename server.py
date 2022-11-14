# #[11/07] 오유빈 코드 작성

from socket  import *
import threading
import time

userInput = '' # 22.11.14 김경호

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        global userInput # 22.11.14 김경호
        userInput = recvData.decode('utf-8') # 22.11.14 김경호
        print('상대방 :', userInput) # 22.11.14 김경호

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,)) #send함수를 인자를 넣어 쓰레드 생성
receiver = threading.Thread(target=receive, args=(connectionSock,)) #receive함수를 인자를 넣어 쓰레드 생성

sender.start()
receiver.start()

while True: #프로그램을 계속 실행한다
    time.sleep(1) #1초 쉰다
    pass