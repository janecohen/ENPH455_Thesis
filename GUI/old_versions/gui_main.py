# gui_main.py
# February 2024
# Jane Cohen

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from scope_control_v4 import Ui_ScopeControlWindow
from main_display_v4 import Ui_MainWindow  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect the scope_control_pushButton to open_scope_control_window method
        self.ui.scope_control_pushButton.clicked.connect(self.open_scope_control_window)

    def open_scope_control_window(self):
        # create an instance of QtWidgets.QMainWindow for the scope control window
        self.scope_control_window = QtWidgets.QMainWindow()

        # set up the UI for the scope control window
        self.scope_control_ui = Ui_ScopeControlWindow()
        self.scope_control_ui.setupUi(self.scope_control_window)

        # show the scope control window
        self.scope_control_window.show()

    def set_var1(self, var):
        self.ui.variable_1 = var

    def get_var1(self):
        return self.ui.variable_1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
