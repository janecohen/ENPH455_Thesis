# main_display.py
# February 2024
# Jane Cohen

# Form implementation generated from reading ui file 'main_display.ui'
# Created by: PyQt5 UI code generator 5.15.9

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        variable_1 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2500, 1500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_window_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.main_window_groupBox.setObjectName("main_window_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_window_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.controls_groupBox = QtWidgets.QGroupBox(self.main_window_groupBox)
        self.controls_groupBox.setObjectName("controls_groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controls_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.controls_groupBox)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.label = QtWidgets.QLabel(self.controls_groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.scope_control_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.scope_control_pushButton.setObjectName("scope_control_pushButton")
        self.horizontalLayout.addWidget(self.scope_control_pushButton)
        self.scope_control_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.scope_control_pushButton.setObjectName("scope_control_pushButton")
        self.horizontalLayout.addWidget(self.scope_control_pushButton)
        self.extra_2_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.extra_2_pushButton.setObjectName("extra_2_pushButton")
        self.horizontalLayout.addWidget(self.extra_2_pushButton)
        self.extra_1_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.extra_1_pushButton.setObjectName("extra_1_pushButton")
        self.horizontalLayout.addWidget(self.extra_1_pushButton)
        self.verticalLayout_2.addWidget(self.controls_groupBox)
        self.plots_groupBox = QtWidgets.QGroupBox(self.main_window_groupBox)
        self.plots_groupBox.setObjectName("plots_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.plots_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.plot_1_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_1_groupBox.setObjectName("plot_1_groupBox")
        self.label_2 = QtWidgets.QLabel(self.plot_1_groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_2.setObjectName("label_2")
        self.groupBox_12 = QtWidgets.QGroupBox(self.plot_1_groupBox)
        self.groupBox_12.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_12.setObjectName("groupBox_12")
        self.frame_8 = QtWidgets.QFrame(self.plot_1_groupBox)
        self.frame_8.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_3 = QtWidgets.QLabel(self.plot_1_groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_3.setObjectName("label_3")
        self.groupBox_13 = QtWidgets.QGroupBox(self.plot_1_groupBox)
        self.groupBox_13.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout.addWidget(self.plot_1_groupBox, 0, 0, 1, 1)
        self.plot_8_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_8_groupBox.setObjectName("plot_8_groupBox")
        self.label_16 = QtWidgets.QLabel(self.plot_8_groupBox)
        self.label_16.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_16.setObjectName("label_16")
        self.groupBox_26 = QtWidgets.QGroupBox(self.plot_8_groupBox)
        self.groupBox_26.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_26.setObjectName("groupBox_26")
        self.frame_15 = QtWidgets.QFrame(self.plot_8_groupBox)
        self.frame_15.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_17 = QtWidgets.QLabel(self.plot_8_groupBox)
        self.label_17.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_17.setObjectName("label_17")
        self.groupBox_27 = QtWidgets.QGroupBox(self.plot_8_groupBox)
        self.groupBox_27.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_27.setObjectName("groupBox_27")
        self.gridLayout.addWidget(self.plot_8_groupBox, 1, 3, 1, 1)
        self.plot_3_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_3_groupBox.setObjectName("plot_3_groupBox")
        self.label_6 = QtWidgets.QLabel(self.plot_3_groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_6.setObjectName("label_6")
        self.groupBox_16 = QtWidgets.QGroupBox(self.plot_3_groupBox)
        self.groupBox_16.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_16.setObjectName("groupBox_16")
        self.frame_10 = QtWidgets.QFrame(self.plot_3_groupBox)
        self.frame_10.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_7 = QtWidgets.QLabel(self.plot_3_groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_7.setObjectName("label_7")
        self.groupBox_17 = QtWidgets.QGroupBox(self.plot_3_groupBox)
        self.groupBox_17.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout.addWidget(self.plot_3_groupBox, 0, 2, 1, 1)
        self.plot_6_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_6_groupBox.setObjectName("plot_6_groupBox")
        self.label_12 = QtWidgets.QLabel(self.plot_6_groupBox)
        self.label_12.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_12.setObjectName("label_12")
        self.groupBox_22 = QtWidgets.QGroupBox(self.plot_6_groupBox)
        self.groupBox_22.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_22.setObjectName("groupBox_22")
        self.frame_13 = QtWidgets.QFrame(self.plot_6_groupBox)
        self.frame_13.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_13 = QtWidgets.QLabel(self.plot_6_groupBox)
        self.label_13.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_13.setObjectName("label_13")
        self.groupBox_23 = QtWidgets.QGroupBox(self.plot_6_groupBox)
        self.groupBox_23.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout.addWidget(self.plot_6_groupBox, 1, 1, 1, 1)
        self.plot_5_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_5_groupBox.setObjectName("plot_5_groupBox")
        self.label_10 = QtWidgets.QLabel(self.plot_5_groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_10.setObjectName("label_10")
        self.groupBox_20 = QtWidgets.QGroupBox(self.plot_5_groupBox)
        self.groupBox_20.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_20.setObjectName("groupBox_20")
        self.frame_12 = QtWidgets.QFrame(self.plot_5_groupBox)
        self.frame_12.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_11 = QtWidgets.QLabel(self.plot_5_groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_11.setObjectName("label_11")
        self.groupBox_21 = QtWidgets.QGroupBox(self.plot_5_groupBox)
        self.groupBox_21.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout.addWidget(self.plot_5_groupBox, 1, 0, 1, 1)
        self.plot_2_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_2_groupBox.setObjectName("plot_2_groupBox")
        self.label_4 = QtWidgets.QLabel(self.plot_2_groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_4.setObjectName("label_4")
        self.groupBox_14 = QtWidgets.QGroupBox(self.plot_2_groupBox)
        self.groupBox_14.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_14.setObjectName("groupBox_14")
        self.frame_9 = QtWidgets.QFrame(self.plot_2_groupBox)
        self.frame_9.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_5 = QtWidgets.QLabel(self.plot_2_groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_5.setObjectName("label_5")
        self.groupBox_15 = QtWidgets.QGroupBox(self.plot_2_groupBox)
        self.groupBox_15.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout.addWidget(self.plot_2_groupBox, 0, 1, 1, 1)
        self.plot_4_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_4_groupBox.setObjectName("plot_4_groupBox")
        self.label_8 = QtWidgets.QLabel(self.plot_4_groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_8.setObjectName("label_8")
        self.groupBox_18 = QtWidgets.QGroupBox(self.plot_4_groupBox)
        self.groupBox_18.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_18.setObjectName("groupBox_18")
        self.frame_11 = QtWidgets.QFrame(self.plot_4_groupBox)
        self.frame_11.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_9 = QtWidgets.QLabel(self.plot_4_groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_9.setObjectName("label_9")
        self.groupBox_19 = QtWidgets.QGroupBox(self.plot_4_groupBox)
        self.groupBox_19.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout.addWidget(self.plot_4_groupBox, 0, 3, 1, 1)
        self.plot_7_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_7_groupBox.setObjectName("plot_7_groupBox")
        self.label_14 = QtWidgets.QLabel(self.plot_7_groupBox)
        self.label_14.setGeometry(QtCore.QRect(30, 220, 47, 14))
        self.label_14.setObjectName("label_14")
        self.groupBox_24 = QtWidgets.QGroupBox(self.plot_7_groupBox)
        self.groupBox_24.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.groupBox_24.setObjectName("groupBox_24")
        self.frame_14 = QtWidgets.QFrame(self.plot_7_groupBox)
        self.frame_14.setGeometry(QtCore.QRect(30, 20, 171, 171))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_15 = QtWidgets.QLabel(self.plot_7_groupBox)
        self.label_15.setGeometry(QtCore.QRect(30, 200, 47, 14))
        self.label_15.setObjectName("label_15")
        self.groupBox_25 = QtWidgets.QGroupBox(self.plot_7_groupBox)
        self.groupBox_25.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.groupBox_25.setObjectName("groupBox_25")
        self.gridLayout.addWidget(self.plot_7_groupBox, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.plots_groupBox)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.gridLayout_2.addWidget(self.main_window_groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.main_window_groupBox.setTitle(_translate("MainWindow", "Main Display"))
        self.controls_groupBox.setTitle(_translate("MainWindow", "Controls"))
        self.label.setText(_translate("MainWindow", "Shot Counter: "))
        self.scope_control_pushButton.setText(_translate("MainWindow", "Scope control"))
        self.extra_2_pushButton.setText(_translate("MainWindow", "Extra button 2"))
        self.extra_1_pushButton.setText(_translate("MainWindow", "Extra button 1"))
        self.plots_groupBox.setTitle(_translate("MainWindow", "Plots"))
        self.plot_1_groupBox.setTitle(_translate("MainWindow", "Plot 1"))
        self.label_2.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_12.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_3.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_13.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_8_groupBox.setTitle(_translate("MainWindow", "Plot 8"))
        self.label_16.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_26.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_17.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_27.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_3_groupBox.setTitle(_translate("MainWindow", "Plot 3"))
        self.label_6.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_16.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_7.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_17.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_6_groupBox.setTitle(_translate("MainWindow", "Plot 6"))
        self.label_12.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_22.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_13.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_23.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_5_groupBox.setTitle(_translate("MainWindow", "Plot 5"))
        self.label_10.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_20.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_11.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_21.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_2_groupBox.setTitle(_translate("MainWindow", "Plot 2"))
        self.label_4.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_14.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_5.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_15.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_4_groupBox.setTitle(_translate("MainWindow", "Plot 4"))
        self.label_8.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_18.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_9.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_19.setTitle(_translate("MainWindow", "GroupBox"))
        self.plot_7_groupBox.setTitle(_translate("MainWindow", "Plot 7"))
        self.label_14.setText(_translate("MainWindow", "Channel:"))
        self.groupBox_24.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_15.setText(_translate("MainWindow", "Scope:"))
        self.groupBox_25.setTitle(_translate("MainWindow", "GroupBox"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
