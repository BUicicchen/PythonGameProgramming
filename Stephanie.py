'''
QLabel
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class Label(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('gui demo')

        self.label1 = QLabel(self)
        self.label1.setText('Python Class!')
        self.label1.move(390, 40)

        self.label2 = QLabel(self)
        self.label2.setToolTip('https://goo.gl/p89kmb')
        self.label2.setText("<a href='https://goo.gl/p89kmb'>Surprise URL</a>")
        self.label2.move(390, 90)
        self.label2.setOpenExternalLinks(True)

        self.label3 = QLabel(self)
        self.label3.move(80, 130)
        self.label3.setPixmap(QPixmap('picture.jpg'))

app = QApplication(sys.argv)
lb = Label()
lb.show()
sys.exit(app.exec_())
