import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 550, 250)
        self.setStyleSheet("background-color:white;")


        # add a push button
        self.btn1 = QPushButton('Button A', self)
        self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn1.resize(200, 20)
        self.btn1.move(50, 50)
        self.btn1.clicked.connect(self.Button_A)

        # add a push button
        self.btn2 = QPushButton('Button B', self)
        self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn2.resize(200, 20)
        self.btn2.move(50, 100)
        self.setWindowTitle('Button B Clicked')
        self.btn2.clicked.connect(self.Button_B)

        self.show()


    def Button_A(self):
        self.setWindowTitle('Button A Clicked')

    def Button_B(self):
        self.setWindowTitle('Button B Clicked')



app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
