# #[11/07] 오유빈 코드 작성
from socket import *
import threading
import time
import logic_test # 22.11.21 김경호
import answer_query # 22.11.21 김경호

# 22.11.21 김경호
global currentLevel
currentLevel = 1
db_search = []

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        userInput = recvData.decode('utf-8') # 22.11.14 김경호
        #print('상대방 :', userInput) # 22.11.14 김경호
        # 22.11.21 김경호
        global currentLevel
        if currentLevel == 1:
            db_search.append(logic_test.logic1(userInput))
            currentLevel += 1
            print(db_search)
        elif currentLevel == 2:
            db_search.append(logic_test.logic2(userInput))
            print(db_search, currentLevel)
            currentLevel += 1
        elif currentLevel == 3:
            db_search.append(logic_test.logic3(userInput))
            print(db_search, currentLevel)
            print(answer_query.search(db_search))
            currentLevel = 1

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