'''
If a form has too many fields to be displayed simultaneously, they can be arranged in different pages placed under each tab of a Tabbed Widget.
The QTabWidget provides a tab bar and a page area.
The page under the first tab is displayed and others are hidden.
The user can view any page by clicking on the desired tab.
'''

'''
METHODS:
currentChanged()
tabCloseRequested()
'''


import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QHBoxLayout, QWidget, QFormLayout, QLineEdit, QRadioButton, \
    QLabel, QCheckBox


class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()




        self.addTab(self.tab1, "Contact Details")
        self.addTab(self.tab2, "Personal Details")
        self.addTab(self.tab3, "Education Details")
        self.addTab(self.tab4, "Family Details")

        #self.tab1.currentChanged.connect(self.tab_1)


        self.tab_1()
        self.tab_2()
        self.tab_3()
        self.tab_4()
        self.setWindowTitle("Let us know more about you!")
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)



    def closeTab(self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def tab_1(self):
        layout = QFormLayout()
        layout.addRow("First name", QLineEdit())
        layout.addRow("Last name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        layout.addRow("Phone number", QLineEdit())
        self.tab1.setLayout(layout)

    def tab_2(self):
        layout = QFormLayout()
        gender = QHBoxLayout()
        gender.addWidget(QRadioButton("Male"))
        gender.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Gender"), gender)
        layout.addRow("Date of Birth", QLineEdit())
        self.tab2.setLayout(layout)

    def tab_3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Majors"))
        layout.addWidget(QCheckBox("Literature"))
        layout.addWidget(QCheckBox("Engineering"))
        layout.addWidget(QCheckBox("History"))
        layout.addWidget(QCheckBox("Psychology"))
        self.tab3.setLayout(layout)

    def tab_4(self):
        layout = QFormLayout()
        layout.addRow("Female guardian:", QLineEdit())
        layout.addRow("Male guardian:", QLineEdit())
        self.tab4.setLayout(layout)
'''
    def removeTab(self, index):
        #remove tab from widget
        widget = self.tabs.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.tab4.removeTab(index)
'''

app = QApplication(sys.argv)
ex = Tab()
ex.show()
sys.exit(app.exec_())

'''
    Button_01 = QtGui.QPushButton("What Tab?")
    ButtonsLayout.addWidget(Button_01)
    Button_01.clicked.connect(self.whatTab)
'''
