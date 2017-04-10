import sys
from PyQt5.QtWidgets import QLineEdit, QApplication, QWidget
from PyQt5.QtGui import QIntValidator

class Grade(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 550, 250)
        self.setStyleSheet("background-color:white;")
        self.setWindowTitle('Grade Converter')


        self.text1 = QLineEdit(self)
        self.text1.resize(200, 40)
        self.text1.move(50, 40)
        self.text1.textChanged.connect(self.convert)
        self.text1.setPlaceholderText("Enter grade 0-100")
        self.text1.setValidator(QIntValidator(0, 100, self))

        self.text2 = QLineEdit(self)
        self.text2.resize(200, 40)
        self.text2.move(50, 150)


        self.show()


    def convert(self):
        gradeDictionary = {'A+':range(97, 100), 'A':range(93, 96), 'A-':range(90,92), 'B+':range(87,89), 'B':range(83, 86), 'B-':range(80,82), 'C+':range(77,79), 'C':range(73, 76), 'C-':range(70,72), 'D+':range(67,69), 'D':range(63, 66), 'D-':range(60,62), 'F':range(0, 59)}
        grade = int(self.text1.text())

        if self.text1.text() is not "":
            for i, j in gradeDictionary.items():
                if grade in j:
                    self.text2.setText(i)
        else:
            self.text2.setText('')


# -- main program
app = QApplication(sys.argv)
gr = Grade()
sys.exit(app.exec_())
