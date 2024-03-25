# main_display.py
# February 2024
# Jane Cohen

# Form implementation generated from reading ui file 'main_display.ui'
# Created by: PyQt5 UI code generator 5.15.9

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import pandas as pd

class Ui_MainWindow(object):
    def __init__(self):
        self.variable_1 = None

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
        self.shot_counter_label = QtWidgets.QLabel(self.controls_groupBox)
        self.shot_counter_label.setObjectName("shot_counter_label")
        self.horizontalLayout.addWidget(self.shot_counter_label)
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
        
        # Adding Plot 1
        self.plot_1_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_1_groupBox.setObjectName("plot_1_groupBox")
        self.gridLayout.addWidget(self.plot_1_groupBox, 0, 0, 1, 1)
        self.plot_1_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_1_groupBox)
        self.plot_1_groupBoxLayout.setObjectName("plot_1_groupBoxLayout")
        self.plot_1_widget = pg.PlotWidget()
        self.plot_1_groupBoxLayout.addWidget(self.plot_1_widget)
        self.plot_1_channel_label = QtWidgets.QLabel(self.plot_1_groupBox)
        self.plot_1_channel_label.setObjectName("plot_1_channel_label")
        self.plot_1_channel_label.setText("Channel:")
        self.plot_1_groupBoxLayout.addWidget(self.plot_1_channel_label)
        self.plot_1_channel_comboBox = QtWidgets.QComboBox(self.plot_1_groupBox)
        self.plot_1_channel_comboBox.setObjectName("plot_1_channel_comboBox")
        self.plot_1_groupBoxLayout.addWidget(self.plot_1_channel_comboBox)
        self.plot_1_scope_label = QtWidgets.QLabel(self.plot_1_groupBox)
        self.plot_1_scope_label.setObjectName("plot_1_scope_label")
        self.plot_1_scope_label.setText("Scope:")
        self.plot_1_groupBoxLayout.addWidget(self.plot_1_scope_label)
        self.plot_1_scope_comboBox = QtWidgets.QComboBox(self.plot_1_groupBox)
        self.plot_1_scope_comboBox.setObjectName("plot_1_scope_comboBox")
        self.plot_1_groupBoxLayout.addWidget(self.plot_1_scope_comboBox)

        self.plot_1_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_1_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])


        # Adding Plot 2
        self.plot_2_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_2_groupBox.setObjectName("plot_2_groupBox")
        self.gridLayout.addWidget(self.plot_2_groupBox, 0, 1, 1, 1)
        self.plot_2_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_2_groupBox)
        self.plot_2_groupBoxLayout.setObjectName("plot_2_groupBoxLayout")
        self.plot_2_widget = pg.PlotWidget()
        self.plot_2_groupBoxLayout.addWidget(self.plot_2_widget)
        self.plot_2_channel_label = QtWidgets.QLabel(self.plot_2_groupBox)
        self.plot_2_channel_label.setObjectName("plot_2_channel_label")
        self.plot_2_channel_label.setText("Channel:")
        self.plot_2_groupBoxLayout.addWidget(self.plot_2_channel_label)
        self.plot_2_channel_comboBox = QtWidgets.QComboBox(self.plot_2_groupBox)
        self.plot_2_channel_comboBox.setObjectName("plot_2_channel_comboBox")
        self.plot_2_groupBoxLayout.addWidget(self.plot_2_channel_comboBox)
        self.plot_2_scope_label = QtWidgets.QLabel(self.plot_2_groupBox)
        self.plot_2_scope_label.setObjectName("plot_2_scope_label")
        self.plot_2_scope_label.setText("Scope:")
        self.plot_2_groupBoxLayout.addWidget(self.plot_2_scope_label)
        self.plot_2_scope_comboBox = QtWidgets.QComboBox(self.plot_2_groupBox)
        self.plot_2_scope_comboBox.setObjectName("plot_2_scope_comboBox")
        self.plot_2_groupBoxLayout.addWidget(self.plot_2_scope_comboBox)

        self.plot_2_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_2_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Adding Plot 3
        self.plot_3_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_3_groupBox.setObjectName("plot_3_groupBox")
        self.gridLayout.addWidget(self.plot_3_groupBox, 0, 2, 1, 1)
        self.plot_3_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_3_groupBox)
        self.plot_3_groupBoxLayout.setObjectName("plot_3_groupBoxLayout")
        self.plot_3_widget = pg.PlotWidget()
        self.plot_3_groupBoxLayout.addWidget(self.plot_3_widget)
        self.plot_3_channel_label = QtWidgets.QLabel(self.plot_3_groupBox)
        self.plot_3_channel_label.setObjectName("plot_3_channel_label")
        self.plot_3_channel_label.setText("Channel:")
        self.plot_3_groupBoxLayout.addWidget(self.plot_3_channel_label)
        self.plot_3_channel_comboBox = QtWidgets.QComboBox(self.plot_3_groupBox)
        self.plot_3_channel_comboBox.setObjectName("plot_3_channel_comboBox")
        self.plot_3_groupBoxLayout.addWidget(self.plot_3_channel_comboBox)
        self.plot_3_scope_label = QtWidgets.QLabel(self.plot_3_groupBox)
        self.plot_3_scope_label.setObjectName("plot_3_scope_label")
        self.plot_3_scope_label.setText("Scope:")
        self.plot_3_groupBoxLayout.addWidget(self.plot_3_scope_label)
        self.plot_3_scope_comboBox = QtWidgets.QComboBox(self.plot_3_groupBox)
        self.plot_3_scope_comboBox.setObjectName("plot_3_scope_comboBox")
        self.plot_3_groupBoxLayout.addWidget(self.plot_3_scope_comboBox)

        self.plot_3_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_3_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Adding Plot 4
        self.plot_4_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_4_groupBox.setObjectName("plot_4_groupBox")
        self.gridLayout.addWidget(self.plot_4_groupBox, 0, 3, 1, 1)
        self.plot_4_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_4_groupBox)
        self.plot_4_groupBoxLayout.setObjectName("plot_4_groupBoxLayout")
        self.plot_4_widget = pg.PlotWidget()
        self.plot_4_groupBoxLayout.addWidget(self.plot_4_widget)
        self.plot_4_channel_label = QtWidgets.QLabel(self.plot_4_groupBox)
        self.plot_4_channel_label.setObjectName("plot_4_channel_label")
        self.plot_4_channel_label.setText("Channel:")
        self.plot_4_groupBoxLayout.addWidget(self.plot_4_channel_label)
        self.plot_4_channel_comboBox = QtWidgets.QComboBox(self.plot_4_groupBox)
        self.plot_4_channel_comboBox.setObjectName("plot_4_channel_comboBox")
        self.plot_4_groupBoxLayout.addWidget(self.plot_4_channel_comboBox)
        self.plot_4_scope_label = QtWidgets.QLabel(self.plot_4_groupBox)
        self.plot_4_scope_label.setObjectName("plot_4_scope_label")
        self.plot_4_scope_label.setText("Scope:")
        self.plot_4_groupBoxLayout.addWidget(self.plot_4_scope_label)
        self.plot_4_scope_comboBox = QtWidgets.QComboBox(self.plot_4_groupBox)
        self.plot_4_scope_comboBox.setObjectName("plot_4_scope_comboBox")
        self.plot_4_groupBoxLayout.addWidget(self.plot_4_scope_comboBox)

        self.plot_4_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_4_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Adding Plot 5
        self.plot_5_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_5_groupBox.setObjectName("plot_5_groupBox")
        self.gridLayout.addWidget(self.plot_5_groupBox, 1, 0, 1, 1)
        self.plot_5_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_5_groupBox)
        self.plot_5_groupBoxLayout.setObjectName("plot_5_groupBoxLayout")
        self.plot_5_widget = pg.PlotWidget()
        self.plot_5_groupBoxLayout.addWidget(self.plot_5_widget)
        self.plot_5_channel_label = QtWidgets.QLabel(self.plot_5_groupBox)
        self.plot_5_channel_label.setObjectName("plot_5_channel_label")
        self.plot_5_channel_label.setText("Channel:")
        self.plot_5_groupBoxLayout.addWidget(self.plot_5_channel_label)
        self.plot_5_channel_comboBox = QtWidgets.QComboBox(self.plot_5_groupBox)
        self.plot_5_channel_comboBox.setObjectName("plot_5_channel_comboBox")
        self.plot_5_groupBoxLayout.addWidget(self.plot_5_channel_comboBox)
        self.plot_5_scope_label = QtWidgets.QLabel(self.plot_5_groupBox)
        self.plot_5_scope_label.setObjectName("plot_5_scope_label")
        self.plot_5_scope_label.setText("Scope:")
        self.plot_5_groupBoxLayout.addWidget(self.plot_5_scope_label)
        self.plot_5_scope_comboBox = QtWidgets.QComboBox(self.plot_5_groupBox)
        self.plot_5_scope_comboBox.setObjectName("plot_5_scope_comboBox")
        self.plot_5_groupBoxLayout.addWidget(self.plot_5_scope_comboBox)

        self.plot_5_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_5_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Adding Plot 6
        self.plot_6_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_6_groupBox.setObjectName("plot_6_groupBox")
        self.gridLayout.addWidget(self.plot_6_groupBox, 1, 1, 1, 1)
        self.plot_6_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_6_groupBox)
        self.plot_6_groupBoxLayout.setObjectName("plot_6_groupBoxLayout")
        self.plot_6_widget = pg.PlotWidget()
        self.plot_6_groupBoxLayout.addWidget(self.plot_6_widget)
        self.plot_6_channel_label = QtWidgets.QLabel(self.plot_6_groupBox)
        self.plot_6_channel_label.setObjectName("plot_6_channel_label")
        self.plot_6_channel_label.setText("Channel:")
        self.plot_6_groupBoxLayout.addWidget(self.plot_6_channel_label)
        self.plot_6_channel_comboBox = QtWidgets.QComboBox(self.plot_6_groupBox)
        self.plot_6_channel_comboBox.setObjectName("plot_6_channel_comboBox")
        self.plot_6_groupBoxLayout.addWidget(self.plot_6_channel_comboBox)
        self.plot_6_scope_label = QtWidgets.QLabel(self.plot_6_groupBox)
        self.plot_6_scope_label.setObjectName("plot_6_scope_label")
        self.plot_6_scope_label.setText("Scope:")
        self.plot_6_groupBoxLayout.addWidget(self.plot_6_scope_label)
        self.plot_6_scope_comboBox = QtWidgets.QComboBox(self.plot_6_groupBox)
        self.plot_6_scope_comboBox.setObjectName("plot_6_scope_comboBox")
        self.plot_6_groupBoxLayout.addWidget(self.plot_6_scope_comboBox)

        self.plot_6_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_6_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Adding Plot 7
        self.plot_7_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_7_groupBox.setObjectName("plot_7_groupBox")
        self.gridLayout.addWidget(self.plot_7_groupBox, 1, 2, 1, 1)
        self.plot_7_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_7_groupBox)
        self.plot_7_groupBoxLayout.setObjectName("plot_7_groupBoxLayout")
        self.plot_7_widget = pg.PlotWidget()
        self.plot_7_groupBoxLayout.addWidget(self.plot_7_widget)
        self.plot_7_channel_label = QtWidgets.QLabel(self.plot_7_groupBox)
        self.plot_7_channel_label.setObjectName("plot_7_channel_label")
        self.plot_7_channel_label.setText("Channel:")
        self.plot_7_groupBoxLayout.addWidget(self.plot_7_channel_label)
        self.plot_7_channel_comboBox = QtWidgets.QComboBox(self.plot_7_groupBox)
        self.plot_7_channel_comboBox.setObjectName("plot_7_channel_comboBox")
        self.plot_7_groupBoxLayout.addWidget(self.plot_7_channel_comboBox)
        self.plot_7_scope_label = QtWidgets.QLabel(self.plot_7_groupBox)
        self.plot_7_scope_label.setObjectName("plot_7_scope_label")
        self.plot_7_scope_label.setText("Scope:")
        self.plot_7_groupBoxLayout.addWidget(self.plot_7_scope_label)
        self.plot_7_scope_comboBox = QtWidgets.QComboBox(self.plot_7_groupBox)
        self.plot_7_scope_comboBox.setObjectName("plot_7_scope_comboBox")
        self.plot_7_groupBoxLayout.addWidget(self.plot_7_scope_comboBox)

        self.plot_7_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_7_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Adding Plot 8
        self.plot_8_groupBox = QtWidgets.QGroupBox(self.plots_groupBox)
        self.plot_8_groupBox.setObjectName("plot_8_groupBox")
        self.gridLayout.addWidget(self.plot_8_groupBox, 1, 3, 1, 1)
        self.plot_8_groupBoxLayout = QtWidgets.QVBoxLayout(self.plot_8_groupBox)
        self.plot_8_groupBoxLayout.setObjectName("plot_8_groupBoxLayout")
        self.plot_8_widget = pg.PlotWidget()
        self.plot_8_groupBoxLayout.addWidget(self.plot_8_widget)
        self.plot_8_channel_label = QtWidgets.QLabel(self.plot_8_groupBox)
        self.plot_8_channel_label.setObjectName("plot_8_channel_label")
        self.plot_8_channel_label.setText("Channel:")
        self.plot_8_groupBoxLayout.addWidget(self.plot_8_channel_label)
        self.plot_8_channel_comboBox = QtWidgets.QComboBox(self.plot_8_groupBox)
        self.plot_8_channel_comboBox.setObjectName("plot_8_channel_comboBox")
        self.plot_8_groupBoxLayout.addWidget(self.plot_8_channel_comboBox)
        self.plot_8_scope_label = QtWidgets.QLabel(self.plot_8_groupBox)
        self.plot_8_scope_label.setObjectName("plot_8_scope_label")
        self.plot_8_scope_label.setText("Scope:")
        self.plot_8_groupBoxLayout.addWidget(self.plot_8_scope_label)
        self.plot_8_scope_comboBox = QtWidgets.QComboBox(self.plot_8_groupBox)
        self.plot_8_scope_comboBox.setObjectName("plot_8_scope_comboBox")
        self.plot_8_groupBoxLayout.addWidget(self.plot_8_scope_comboBox)

        self.plot_8_channel_comboBox.addItems(["Select channel", "Channel A", "Channel B"])
        self.plot_8_scope_comboBox.addItems(["Select scope", "Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        self.verticalLayout_2.addWidget(self.plots_groupBox)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.gridLayout_2.addWidget(self.main_window_groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Example connection for plot 1 (repeat for other plots accordingly)
        self.plot_1_scope_comboBox.currentIndexChanged.connect(
            lambda: self.load_and_plot_data(
                self.plot_1_widget,
                self.plot_1_scope_comboBox.currentText(),
                self.plot_1_channel_comboBox.currentText()
            )
        )
        self.plot_1_channel_comboBox.currentIndexChanged.connect(
            lambda: self.load_and_plot_data(
                self.plot_1_widget,
                self.plot_1_scope_comboBox.currentText(),
                self.plot_1_channel_comboBox.currentText()
            )
        )
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.main_window_groupBox.setTitle(_translate("MainWindow", "Main Display"))
        self.controls_groupBox.setTitle(_translate("MainWindow", "Controls"))
        self.shot_counter_label.setText(_translate("MainWindow", "Shot Counter: "))
        self.scope_control_pushButton.setText(_translate("MainWindow", "Scope control"))
        self.extra_2_pushButton.setText(_translate("MainWindow", "Extra button 2"))
        self.extra_1_pushButton.setText(_translate("MainWindow", "Extra button 1"))
        self.plots_groupBox.setTitle(_translate("MainWindow", "Plots"))

    def load_and_plot_data(self, plot_widget, selected_scope, selected_channel):
        file_path = f"./GUI/collected_data/{selected_scope}/{selected_channel}/data.csv"
        try:
            data = pd.read_csv(file_path)
            plot_widget.clear()
            plot_widget.plot(data['time'], data['V'])  
        except FileNotFoundError:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
