'''QCheckBox'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon

class CheckDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(400, 400, 450, 350)
        self.setWindowTitle('CheckBox Demonstration')

        # -- add a checkbox
        self.check = QCheckBox('This is a checkbox', self)
        self.check.setTristate(True) # allowing tristate
        self.check.resize(250, 30)
        self.check.move(150, 30)
        self.check.stateChanged.connect(self.dosth)
        self.check.setIcon(QIcon('MyIcon.png'))

        # add a button
        self.btn1 = QPushButton('Reset', self)
        self.btn1.setToolTip('This button resets the checkbox!')
        self.btn1.resize(250, 90)
        self.btn1.move(100, 100)
        self.btn1.clicked.connect(self.reset)

        # -- add a button for disabling/enabling
        self.btn2 = QPushButton('Disable/Enable', self)
        self.btn2.setToolTip('This button disables/enables the checkbox!')
        self.btn2.resize(250, 90)
        self.btn2.move(100, 200)
        self.btn2.clicked.connect(self.toggle)

        self.show()

    def dosth(self):
        state = self.check.checkState()

        if state == 0:
            self.setWindowTitle('The checkbox was unchecked')
        elif state == 1:
            self.setWindowTitle('The checkbox was unchanged')
        elif state == 2:
            self.setWindowTitle('The checkbox was checked')

    def reset(self):
        self.check.setChecked(False)
        self.setWindowTitle('CheckBox Demonstration')

    def toggle(self):
        if self.check.isEnabled():
            self.check.setEnabled(False)
            self.setWindowTitle('The checkbox has been disabled')
        else:
            self.check.setEnabled(True)
            self.setWindowTitle('The checkbox has been enabled')


'''
        if self.check.isEnabled():
            self.check.setCheckable(False)
            self.setWindowTitle('The checkbox has been disabled')
        else:
            self.check.setCheckable(True)
            self.setWindowTitle('The checkbox has been enabled')
'''


'''
        if self.check.isChecked():
            self.setWindowTitle('The checkbox was checked')
        else:
            self.setWindowTitle('The checkbox was unchecked')
'''

# -- main program
app = QApplication(sys.argv)
ex = CheckDemo()
sys.exit(app.exec_())
