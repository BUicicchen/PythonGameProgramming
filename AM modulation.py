import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDockWidget,  QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time


class CosGraph(QDockWidget):
    def __init__(self, parent = None):
        super(CosGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # -- container for histogram (same as graph)
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("Cosine Graph")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(500, 200)
        # -- define the histogram
        self.graph = PlotWidget(self)
        # -- horizontal, vertical lines, and thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("cos_graph")
        self.graph.raise_()
        # -- add graph container to layout
        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, cos_data):
        X = cos_data['X']
        Y = cos_data['Y']
        colorLine = cos_data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)


    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9 * e.size().height())

class SinGraph(QDockWidget):
    def __init__(self, parent = None):
        super(SinGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # -- container for graph
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("Sine Graph")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(500, 200)
        # -- define the graph
        self.graph = PlotWidget(self)
        # -- horizontal, vertical lines, and thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("sin_graph")
        self.graph.raise_()
        # -- add graph container to layout
        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, sin_data):
        '''
        :param sin data: dictionary with X, Y sin data
        :return: None
        '''
        X = sin_data['X']
        Y = sin_data['Y']
        colorLine = sin_data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9 * e.size().height())


class RadioGraph(QDockWidget):
    def __init__(self, parent = None):
        super(RadioGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # -- container for histogram (same as graph)
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("Radio Graph")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(500, 200)
        # -- define the histogram
        self.graph = PlotWidget(self)
        # -- horizontal, vertical lines, and thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("radio_graph")
        self.graph.raise_()
        # -- add graph container to layout
        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, radio_data):
        X = radio_data['X']
        Y = radio_data['Y']
        colorLine = radio_data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)


    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9 * e.size().height())


class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Mainwindow, self).__init__(parent=parent)
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        # -- create docks
        self.cos_dockGraph = CosGraph()
        self.sin_dockGraph = SinGraph()
        self.radio_dockGraph = RadioGraph()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.cos_dockGraph)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sin_dockGraph)
        self.addDockWidget(Qt.RightDockWidgetArea, self.radio_dockGraph)
        self.update()

    def update(self):
        Npoints = 2000
        f_m = 0.1
        X = np.arange(0, 20, 20/Npoints)
        cos_Y = np.cos(2 * np.pi * f_m * X)

        A = 5
        f_c = 1
        sin_Y = A * np.sin(2 * np.pi * f_c * X)
        # -- every second we change color with this command
        C = pt.hsvColor(time.time() / 5 % 1, alpha = 0.5)

        M = 1
        radio_Y = (1 + M * np.cos(2* np.pi * f_m * X)) * A * np.sin(2 * np.pi * f_c * X)

        # -- Pyqtgraph wrapper for the line.
        pen = pt.mkPen(color = C, width = 2)
        cos_data = {'X':X, 'Y':cos_Y, 'pen':pen}
        self.cos_dockGraph.plot(cos_data)
        sin_data = {'X':X, 'Y':sin_Y, 'pen':pen}
        self.sin_dockGraph.plot(sin_data)
        radio_data = {'X':X, 'Y':radio_Y, 'pen':pen}
        self.radio_dockGraph.plot(radio_data)
        # -- refresh rate of 100 ms
        QtCore.QTimer.singleShot(100, self.update)


class SandBoxApp(QtWidgets.QApplication):
    # -- define class constructor
    def __init__(self, *args, **kwargs):
        super(SandBoxApp, self).__init__(*args)
        self.mainwindow = Mainwindow()
        self.mainwindow.setGeometry(50, 100, 1200, 600)
        self.mainwindow.show()
        # -- disable contextual menu (right click mouse)
        self.mainwindow.setContextMenuPolicy(Qt.NoContextMenu)

# -- entry point for the Python program
def main():
    app = SandBoxApp(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
