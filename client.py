# 김경호 2022.11.07
# 채팅 프로그램 클라이언트
from socket import *
import threading
import time

def send(socket):
    while True:
        sendData = input('>>> ')
        socket.send(sendData.encode('utf-8'))

def receive(socket):
    while True:
        receiveData = socket.recv(1024) # 1024바이트 사이즈 버퍼
        print('챗봇 : ', receiveData.decode('utf-8'))

port = 8081

# AF_INET == IPv4
# SOCK_STREAM == TCP 패킷 수신
clientSocket = socket(AF_INET, SOCK_STREAM) # 소켓 생성
clientSocket.connect(('127.0.0.1', port))

print('학교 관련? 시설 관련?')

sender = threading.Thread(target=send, args=(clientSocket,))
receiver = threading.Thread(target=receive, args=(clientSocket,))

sender.start()
receiver.start()

# 무한 루프
while True:
    time.sleep(1) 
    pass