import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QHBoxLayout, QWidget, QFormLayout, QLineEdit, QRadioButton, \
    QLabel, QCheckBox, QCalendarWidget, QPushButton, QDockWidget, QProgressBar, QComboBox
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap



class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()
        self.initGUI()

    def initGUI(self):

        self.setGeometry(500, 300, 800, 650)
        self.setWindowTitle("CollegeBoard")

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, "Personal information")
        self.addTab(self.tab2, "Choose a major")
        self.addTab(self.tab3, "Personal statement")
        self.addTab(self.tab4, "Register for a test")
        self.addTab(self.tab5, "Registration completed!")


        self.tab_1()
        self.tab_2()
        self.tab_3()
        self.tab_4()
        self.tab_5()

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

        self.show()



    def closeTab(self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def tab_1(self):
        layout = QFormLayout()
        self.tab1.setLayout(layout)

        self.progressbar = QProgressBar(self)
        self.progressbar.setValue(0)
        layout.addRow(self.progressbar)

        self.btn1 = QPushButton('Next Page', self)
        self.btn1.clicked.connect(self.nextPage)
        self.btn1.move(650,600)

        self.txt1 = QLineEdit(self)
        self.txt1.setPlaceholderText("Cici")
        layout.addRow("First name", self.txt1)
        self.txt2 = QLineEdit(self)
        self.txt2.setPlaceholderText("Chen")
        layout.addRow("Last name", self.txt2)
        self.txt3 = QLineEdit(self)
        self.txt3.setPlaceholderText("")
        layout.addRow("Address", self.txt3)
        self.txt4 = QLineEdit(self)
        self.txt4.setPlaceholderText("")
        layout.addRow("Phone number", self.txt4)
        layout.addWidget(QLabel("Gender"))
        layout.addWidget(QCheckBox("Male"))
        layout.addWidget(QCheckBox("Female"))
        self.txt5 = QLineEdit(self)
        self.txt5.setPlaceholderText("")
        layout.addRow("Student ID", self.txt5)
        self.txt6 = QLineEdit(self)
        self.txt6.setPlaceholderText("mm/dd/yyyy")
        layout.addRow("Birthday", self.txt6)
        self.txt7 = QLineEdit(self)
        self.txt7.setPlaceholderText("Pacific American School")
        layout.addRow("High School", self.txt7)

        self.comboBox1 = QComboBox(self)
        self.comboBox1.addItem("January")
        self.comboBox1.addItem("February")
        self.comboBox1.addItem("March")
        self.comboBox1.addItem("April")
        self.comboBox1.addItem("May")
        self.comboBox1.addItem("June")
        self.comboBox1.addItem("July")
        self.comboBox1.addItem("August")
        self.comboBox1.addItem("September")
        self.comboBox1.addItem("October")
        self.comboBox1.addItem("November")
        self.comboBox1.addItem("December")
        layout.addRow("Graduation month", self.comboBox1)
        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItem("2016")
        self.comboBox2.addItem("2017")
        self.comboBox2.addItem("2018")
        self.comboBox2.addItem("2019")
        self.comboBox2.addItem("2020")
        self.comboBox2.addItem("2021")
        self.comboBox2.addItem("2022")
        layout.addRow("Graduation year", self.comboBox2)

        self.btn2 = QPushButton('Change a photo', self)
        layout.addRow("", self.btn2)
        self.label1 = QLabel(self)
        layout.addRow(self.label1)
        self.label1.move(300, 60)
        self.label1.setPixmap(QPixmap('picture.jpg'))
        self.label1.resize(430, 60)



    def tab_2(self):
        layout = QFormLayout()
        self.tab2.setLayout(layout)

        self.btn1 = QPushButton('Next Page', self)
        self.btn1.clicked.connect(self.nextPage)
        self.btn1.move(650,600)

        self.progressbar = QProgressBar(self)
        self.progressbar.setValue(25)
        layout.addRow(self.progressbar)

        # -- add a checkbox
        self.check = QCheckBox('Biology', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Chemistry', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Computer science', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Engineering', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Arts & design', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Literature', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('History', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Language', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Media', self)
        self.check.setTristate(True) # allowing tristate
        layout.addRow(self.check)
        self.check = QCheckBox('Philosophy', self)
        self.check.setTristate(True) # allowing tristate
        self.check.stateChanged.connect(self.dosth)
        layout.addRow(self.check)


    def dosth(self):
        state = self.check.checkState()
        if state == 0:
            self.setWindowTitle('You have deselected this major')
        elif state == 1:
            self.setWindowTitle('You are unsure of this major')
        elif state == 2:
            self.setWindowTitle('You have selected this major')


    def tab_3(self):
        layout = QFormLayout()
        self.tab3.setLayout(layout)

        self.btn1 = QPushButton('Next Page', self)
        self.btn1.clicked.connect(self.nextPage)
        self.btn1.move(650,600)

        self.progressbar = QProgressBar(self)
        self.progressbar.setValue(50)
        layout.addRow(self.progressbar)

        self.txt1 = QLineEdit('', self)
        self.txt2 = QLineEdit('', self)
        self.txt3 = QLineEdit('', self)
        self.txt4 = QLineEdit('', self)
        self.txt5 = QLineEdit('', self)

        self.dock1 = QDockWidget('Personal statement', self)
        self.dock1.move(20, 20)
        self.dock1.setWidget(self.txt1)

        self.dock1.setFloating(False)
        self.dock1.setFeatures(self.dock1.DockWidgetMovable)

        layout.addRow(self.dock1)
        layout.addRow('Please write a short statement about yourself.', self.txt1)
        layout.addRow(self.txt1)
        layout.addRow('What is your hobby?', self.txt2)
        layout.addRow(self.txt2)
        layout.addRow('What characteristics do you have that differs from others?', self.txt3)
        layout.addRow(self.txt3)
        layout.addRow('Which college do you want to go to and why?', self.txt4)
        layout.addRow(self.txt4)
        layout.addRow('Which after school activities did you attend in high school?', self.txt5)
        layout.addRow(self.txt5)



    def tab_4(self):
        layout = QFormLayout()
        self.tab4.setLayout(layout)

        self.btn1 = QPushButton('Next Page', self)
        self.btn1.clicked.connect(self.nextPage)
        self.btn1.move(650,600)

        self.progressbar = QProgressBar(self)
        self.progressbar.setValue(75)
        layout.addRow(self.progressbar)

        self.cal = QCalendarWidget(self)
        self.cal.setWindowTitle('Calendar')
        self.cal.setGridVisible(True) #one of the function
        self.cal.move(20, 100)
        self.cal.clicked[QDate].connect(self.showDate)
        self.label = QLabel(self)
        self.date = self.cal.selectedDate() #another function
        self.label.setText(self.date.toString())
        self.label.move(100, 500)
        layout.addRow(self.cal)
        layout.addRow(self.label)


        # -- add a checkbox
        self.check1 = QCheckBox('SAT w/ essay', self)
        layout.addRow(self.check1)
        self.check2 = QCheckBox('Chinese w/ listening', self)
        layout.addRow(self.check2)
        self.check3 = QCheckBox('Physics', self)
        layout.addRow(self.check3)
        self.check4 = QCheckBox('Math I', self)
        layout.addRow(self.check4)
        self.check5 = QCheckBox('Math II', self)
        layout.addRow(self.check5)
        self.check6 = QCheckBox('Biology', self)
        layout.addRow(self.check6)
        self.check7 = QCheckBox('US History', self)
        layout.addRow(self.check7)
        self.check8 = QCheckBox('Literature', self)
        layout.addRow(self.check8)
        self.check9 = QCheckBox('Spanish', self)
        layout.addRow(self.check9)
        self.check10 = QCheckBox('French', self)
        layout.addRow(self.check10)

        # add a button
        self.btn1 = QPushButton('Reset', self)
        self.btn1.setToolTip('This button resets the checkbox!')
        self.btn1.resize(250, 90)
        self.btn1.move(100, 100)
        self.btn1.clicked.connect(self.reset)
        layout.addRow(self.btn1)




    def reset(self):
        self.check1.setChecked(False)
        self.check2.setChecked(False)
        self.check3.setChecked(False)
        self.check4.setChecked(False)
        self.check5.setChecked(False)
        self.check6.setChecked(False)
        self.check7.setChecked(False)
        self.check8.setChecked(False)
        self.check9.setChecked(False)
        self.check10.setChecked(False)



    def tab_5(self):
        layout = QFormLayout()
        self.tab5.setLayout(layout)

        self.label1 = QLabel(self)
        layout.addRow("Your registration have been successfully recorded. ☑️", self.label1)

    def showDate(self, date):
        self.label.setText(date.toString())

    def nextPage(self):
        self.setCurrentIndex(self.currentIndex() + 1)


app = QApplication(sys.argv)
ex = Tab()
ex.show()
sys.exit(app.exec_())
