# #[11/07] 오유빈 코드 작성
from socket import *
import threading
import time
import logic # 22.11.21 김경호
import answer_query # 22.11.21 김경호

# 22.11.21 김경호
global currentLevel
currentLevel = 1
db_search = []
global output

def send(sock):
    while True:
        sendData = input()
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        userInput = recvData.decode('utf-8') # 22.11.14 김경호
        #print('상대방 :', userInput) # 22.11.14 김경호
        # 22.11.21 김경호
        global currentLevel
        global output
        if currentLevel == 1:
            db_search.append(logic.logic1(userInput))
            if db_search[0] == 1:
                output = '학과 관련 질문입니까 학사 관련 질문입니까??'
            elif db_search[0] == 2:
                output = '건물 위치, 대중 교통, 주요 시설 중 궁금한 내용은 무엇입니까?'
            sock.send(output.encode('utf-8'))
            currentLevel += 1
            #print(db_search, currentLevel)
        elif currentLevel == 2:
            db_search.append(logic.logic2(userInput))
            if db_search[1] == 3:
                output = '위치를 찾고 싶은 건물 번호? ex) w2'
            elif  db_search[1]==4:
                output='대전 복합 터미널에서 오십니까? 대전역에서 오십니까?'
            elif db_search[1]==5:
                output='학교 내 알고싶은 시설은?'
            elif db_search[1]==1:
                output='궁금하신 학과가 있으신가요?'
            elif db_search[1]==2:
                output='입학 졸업 등 학교 관련 질문이 있으신가요?'
            sock.send(output.encode('utf-8'))
            #print(db_search, currentLevel)
            currentLevel += 1
        elif currentLevel == 3:
            db_search.append(logic.logic3(userInput))
            print(db_search, currentLevel)
            result = str(answer_query.search(db_search)) # 22.11.24 김경호
            output = result.replace('(', '').replace(')', '').replace(',', '').replace("'", '') # 22.11.24 김경호
            sock.send(output.encode('utf-8'))
            output = '학교 관련? 시설 관련?'
            sock.send(output.encode('utf-8'))
            currentLevel = 1
            db_search.clear() # 22.11.24 김경호

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