'''QCalendarWidget'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()

      self.initUI()

   def initUI(self):

      self.setGeometry(100, 100, 400, 300)
      self.setWindowTitle('Calendar Demo')

      cal = QCalendarWidget(self)
      cal.setGridVisible(True) #one of the function
      cal.move(20, 20)
      cal.clicked[QDate].connect(self.showDate)

      self.label = QLabel(self)
      date = cal.selectedDate() #another function
      self.label.setText(date.toString())
      self.label.move(20, 200)

      self.show()

   def showDate(self, date):
      self.label.setText(date.toString())


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
