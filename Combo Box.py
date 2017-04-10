'''
This is a program that displays a text file contains the names and prices available at a certain store.
Read the text file in Python and show the items using a Widget QTComboBox.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox


class comboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 130)
        self.setWindowTitle('Combo Box Examples')

        self.comboBox1 = QComboBox(self)
        self.comboBox1.addItem("Blue")
        self.comboBox1.addItem("Green")
        self.comboBox1.move(50, 50)

        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItem("Blue")
        self.comboBox2.addItem("Green")
        self.comboBox2.move(200, 50)

        self.comboBox3 = QComboBox(self)
        self.comboBox3.addItem("Blue")
        self.comboBox3.addItem("Green")
        self.comboBox3.addItem("Red")
        self.comboBox3.move(350, 50)

        self.show()


app = QApplication(sys.argv)
cb = comboBox()
sys.exit(app.exec_())
