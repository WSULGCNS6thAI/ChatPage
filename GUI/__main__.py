# 22.11.20 김경호
# GUI 창 띄우기
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QTextBrowser, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ChatBot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('우송대 챗봇')

        vbox = QVBoxLayout() # Box 레이아웃 설정

        label1 = QLabel('우송대 챗봇', self)
        label1.setAlignment(Qt.AlignLeft)
        label2 = QLabel('나의 채팅', self)
        label2.setAlignment(Qt.AlignLeft)

        bot_chat = QTextBrowser()
        self.tb = QTextBrowser()
        bot_chat.setOpenExternalLinks(True) # 외부 링크 연결 가능

        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text) # 엔터 누르면

        vbox.addWidget(label1)
        vbox.addWidget(bot_chat)
        vbox.addWidget(label2)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.le)

        self.setLayout(vbox) # 윈도우 레이아웃 Box로 지정
        self.resize(380, 640) # 초기 실행 창 크기 (가로, 세로)
        self.center()
        self.show()

    # 초기 실행 창 화면 중앙으로
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center() # 화면의 중앙을 찾음
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 텍스트 브라우저에 텍스트 삽입 위한 함수
    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChatBot()
    sys.exit(app.exec_())