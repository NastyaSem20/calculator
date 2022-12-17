import sys
import socket
from PyQt6.QtWidgets import QLineEdit, QLabel
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from client import user_send




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.button1 = QPushButton("Посчитать")
        self.button2 = QPushButton("История")
        self.button1.clicked.connect(self.find_ans)
        self.button2.clicked.connect(self.show_history)
        self.input = QLineEdit()
        self.answer = QLabel()
        self.history = QLabel()
        self.setFixedSize(QSize(400, 500))


    def find_ans(self):
        str = self.input.text()
        ans = user_send(sock, str)
        self.answer.setText(ans)

    def show_history(self):
        ans = '\n'.join(history)
        self.history.setText(ans)


if name == "main":
    app = QApplication(sys.argv)
    sock = socket.socket()
    window = MainWindow()
    window.show()
    sock.bind(('', 5050))
    sock.listen(1)
    conn, addr = sock.accept()
    history = []
    while True:
        digits = []
        signs = []
        data = conn.recv(1024)
        print(data)
        if not data:
            break
        elif data == '':
            conn.send(history)
        else:
            str = f'{data} = {eval(data)}'
            history.append(str)
            conn.send(eval(data))
    app.exec()