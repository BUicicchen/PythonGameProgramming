import sys
from PyQt5.QtWidgets import QApplication, QDialog
from findandreplace import Ui_Form as dlg

# --- Create an QT application
app = QApplication(sys.argv)
# --- Create a dialog window
window = QDialog()
# --- Create a findandreplace dialog (object)
ui = dlg()
# --- add the findandreplace dialog to the main window
ui.setupUi(window)

window.show()
sys.exit(app.exec_())

