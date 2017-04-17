''' QProgressBar '''
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal


class TutorialThread(QThread):
        set_max = pyqtSignal(int)
        update = pyqtSignal(int)

        def __init__(self):
                QThread.__init__(self)

        def run(self):
                self.update.emit(100)
                for index in range(1, 101):
                        self.update.emit(index)
                        time.sleep(0.01)


class MainWindow(QWidget):

        def __init__(self):
                super(self.__class__, self).__init__()
                self.setupUi()
                self.tutorial_thread = TutorialThread()
                self.tutorial_thread.set_max.connect(self.set_max)
                self.tutorial_thread.update.connect(self.set_value)
                self.show()

        def setupUi(self):
                self.setGeometry(300, 300, 250, 250)
                self.setWindowTitle("ProgressBar")

                self.button_start = QPushButton('Start', self)
                self.button_start.resize(150, 40)
                self.button_start.move(50,50)
                self.button_stop = QPushButton(self)
                self.button_stop.setText("End")
                self.button_stop.resize(150, 40)
                self.button_stop.move(50,90)

                self.progress_bar = QProgressBar(self)
                self.progress_bar.resize(150, 5)
                self.progress_bar.move(50,130)

                self.button_start.clicked.connect(self.start)
                self.button_stop.clicked.connect(self.stop)
                self.show()

        def start(self):
                self.tutorial_thread.start()

        def stop(self):
                self.tutorial_thread.terminate()

        def set_max(self, data):
                self.progress_bar.setMaximum(data)

        def set_value(self, data):
                self.progress_bar.setValue(data)


app = QApplication(sys.argv)
MainWindow = MainWindow()
sys.exit(app.exec_())
