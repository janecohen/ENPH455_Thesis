# gui_main.py
# Date: February 2024
# Author: Jane Cohen

## This code is for a GUI to control PicoScope data acquisition and display collected data
## gui_main.py defines the superclass MainWindow to control all windows in the GUI

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from scope_control_v16 import Ui_ScopeControlWindow
from main_display_v17 import Ui_MainWindow  
from PyQt5.QtCore import QSettings

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect the scope_control_pushButton to open_scope_control_window method
        self.ui.scope_control_pushButton.clicked.connect(self.open_scope_control_window)

    def open_scope_control_window(self):
        # create an instance of the scope control window
        self.scope_control_window = QtWidgets.QMainWindow()

        # set up the UI for the scope control window
        self.scope_control_ui = Ui_ScopeControlWindow()
        self.scope_control_ui.setupUi(self.scope_control_window)

        # show the scope control window
        self.scope_control_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
