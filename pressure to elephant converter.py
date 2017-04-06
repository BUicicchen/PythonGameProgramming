import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 550, 250)
        self.setStyleSheet("background-color:white;")
        self.setWindowTitle('Pressure to elephant converter')


        # --- converts from atmospheric pressure to number of elephants ---
        # add a push button
        self.btn1 = QPushButton('Convert', self)
        #self.btn1 = QPushButton('Convert to number of elephants', self)
        self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn1.resize(200, 20)
        self.btn1.move(50, 50)
        self.btn1.clicked.connect(self.convert)

        self.text1 = QTextEdit(self)
        self.text1.resize(200, 40)
        self.text1.move(50, 80)
        self.text1.setPlaceholderText("This is a EditText Widget")
        self.text1.setPlaceholderText("Enter pressure (Pascal)")

        self.num1 = QDoubleSpinBox(self)
        self.num1.setMaximum(200000)
        self.num1.setMinimum(0)
        self.num1.setSuffix(" elephants")
        self.num1.resize(200,30)
        self.num1.move(50,130)



        # --- converts from number of elephants to atmospheric pressure---
        # add a push button
        self.btn2 = QPushButton('Convert', self)
        #self.btn1 = QPushButton('Convert to atmospheric pressure', self)
        self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn2.resize(200, 20)
        self.btn2.move(300, 50)
        self.btn2.clicked.connect(self.convert)

        self.text2 = QTextEdit(self)
        self.text2.resize(200, 40)
        self.text2.move(300, 80)
        self.text2.setPlaceholderText("This is a EditText Widget")
        self.text2.setPlaceholderText("Enter number of elephants")

        self.num2 = QDoubleSpinBox(self)
        self.num2.setMaximum(200000)
        self.num2.setMinimum(0)
        self.num2.setSuffix(" Pascal")
        self.num2.resize(200,30)
        self.num2.move(300,130)



        self.show()


    def convert(self):
        if self.text1.toPlainText() is not "":
            atmospheric_pressure = float(self.text1.toPlainText())
            # set pressure of elephant @ sea level: 40,000 N / 1 m^2 = 40,000 pascal
            self.num1.setValue(atmospheric_pressure / 40000)

        if self.text2.toPlainText() is not "":
            num_elephants = float(self.text2.toPlainText())
            # set pressure of elephant @ sea level: 40,000 N / 1 m^2 = 40,000 pascal
            # atmospheric pressure @ sea level: 101325 Pascal
            self.num2.setValue(num_elephants * 40000)


# -- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
