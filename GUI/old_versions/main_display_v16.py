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
import csv
from PyQt5.QtCore import QSettings
import subprocess

NUM_SCOPE = 4 #number of scopes
chA_attributes = ["chA_name", "chA_collect", "chA_range", "chA_rate", "chA_extra1", "chA_extra2"]

chB_attributes = ["chB_name", "chB_collect", "chB_range", "chB_rate", "chB_extra2", "chB_extra2"]

trigger_attributes = ["autotrigger", "coupling", "threshold", "direction", "delay", "presample", 
                      "postsample", "downsample"]

plot_labels = ["plot_1_title_label", "plot_2_title_label", "plot_3_title_label", "plot_4_title_label",
               "plot_5_title_label", "plot_6_title_label", "plot_7_title_label", "plot_8_title_label"]


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
        self.shot_counter_label = QtWidgets.QLabel(self.controls_groupBox)
        self.shot_counter_label.setObjectName("shot_counter_label")
        self.horizontalLayout.addWidget(self.shot_counter_label)
        self.scope_control_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.scope_control_pushButton.setObjectName("scope_control_pushButton")
        self.horizontalLayout.addWidget(self.scope_control_pushButton)
        self.scope_control_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.scope_control_pushButton.setObjectName("scope_control_pushButton")
        self.horizontalLayout.addWidget(self.scope_control_pushButton)
        self.collect_data_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.collect_data_pushButton.setObjectName("collect_data_pushButton")
        self.horizontalLayout.addWidget(self.collect_data_pushButton)
        self.refresh_pushButton = QtWidgets.QPushButton(self.controls_groupBox)
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.verticalLayout_2.addWidget(self.controls_groupBox)
        self.plots_groupBox = QtWidgets.QGroupBox(self.main_window_groupBox)
        self.plots_groupBox.setObjectName("plots_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.plots_groupBox)
        self.gridLayout.setObjectName("gridLayout")

        self.upload_settings()
        
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

        # title label
        self.plot_1_title_label = QtWidgets.QLabel(self.plot_1_groupBox)
        self.plot_1_title_label.setObjectName(plot_labels[0])
        self.plot_1_title_label.setText("Plot 1 Title")  
        self.plot_1_groupBoxLayout.insertWidget(0, self.plot_1_title_label)  

        # combo boxes for scope and channel selection
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

        # title label
        self.plot_2_title_label = QtWidgets.QLabel(self.plot_2_groupBox)
        self.plot_2_title_label.setObjectName(plot_labels[1])
        self.plot_2_title_label.setText("Plot 2 Title")  
        self.plot_2_groupBoxLayout.insertWidget(0, self.plot_2_title_label)  

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

        # title label
        self.plot_3_title_label = QtWidgets.QLabel(self.plot_3_groupBox)
        self.plot_3_title_label.setObjectName(plot_labels[2])
        self.plot_3_title_label.setText("Plot 3 Title")  
        self.plot_3_groupBoxLayout.insertWidget(0, self.plot_3_title_label)  

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

        # title label
        self.plot_4_title_label = QtWidgets.QLabel(self.plot_4_groupBox)
        self.plot_4_title_label.setObjectName(plot_labels[3])
        self.plot_4_title_label.setText("Plot 4 Title")  
        self.plot_4_groupBoxLayout.insertWidget(0, self.plot_4_title_label)  

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

        # title label
        self.plot_5_title_label = QtWidgets.QLabel(self.plot_5_groupBox)
        self.plot_5_title_label.setObjectName(plot_labels[4])
        self.plot_5_title_label.setText("Plot 5 Title")  
        self.plot_5_groupBoxLayout.insertWidget(0, self.plot_5_title_label)  

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

        # title label
        self.plot_6_title_label = QtWidgets.QLabel(self.plot_6_groupBox)
        self.plot_6_title_label.setObjectName(plot_labels[5])
        self.plot_6_title_label.setText("Plot 6 Title")  
        self.plot_6_groupBoxLayout.insertWidget(0, self.plot_6_title_label)  

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

        # title label
        self.plot_7_title_label = QtWidgets.QLabel(self.plot_7_groupBox)
        self.plot_7_title_label.setObjectName(plot_labels[6])
        self.plot_7_title_label.setText("Plot 7 Title")  
        self.plot_7_groupBoxLayout.insertWidget(0, self.plot_7_title_label)  

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

        # title label
        self.plot_8_title_label = QtWidgets.QLabel(self.plot_8_groupBox)
        self.plot_8_title_label.setObjectName(plot_labels[7])
        self.plot_8_title_label.setText("Plot 8 Title")  
        self.plot_8_groupBoxLayout.insertWidget(0, self.plot_8_title_label)  

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


        # Connections for plot 1 
        self.plot_1_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_1_title_label,
                self.plot_1_widget, self.plot_1_scope_comboBox.currentText(),
                self.plot_1_channel_comboBox.currentText()))
        self.plot_1_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_1_title_label,
                self.plot_1_widget, self.plot_1_scope_comboBox.currentText(), 
                self.plot_1_channel_comboBox.currentText()))
        
        # Connections for plot 2 
        self.plot_2_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_2_title_label,
                self.plot_2_widget, self.plot_2_scope_comboBox.currentText(),
                self.plot_2_channel_comboBox.currentText()))
        self.plot_2_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_2_title_label,
                self.plot_2_widget, self.plot_2_scope_comboBox.currentText(), 
                self.plot_2_channel_comboBox.currentText()))
        
        # Connections for plot 3 
        self.plot_3_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_3_title_label,
                self.plot_3_widget, self.plot_3_scope_comboBox.currentText(),
                self.plot_3_channel_comboBox.currentText()))
        self.plot_3_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_3_title_label,
                self.plot_3_widget, self.plot_3_scope_comboBox.currentText(), 
                self.plot_3_channel_comboBox.currentText()))
        
        # Connections for plot 4 
        self.plot_4_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_4_title_label,
                self.plot_4_widget, self.plot_4_scope_comboBox.currentText(),
                self.plot_4_channel_comboBox.currentText()))
        self.plot_4_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_4_title_label,
                self.plot_4_widget, self.plot_4_scope_comboBox.currentText(), 
                self.plot_4_channel_comboBox.currentText()))
        
        # Connections for plot 5 
        self.plot_5_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_5_title_label,
                self.plot_5_widget, self.plot_5_scope_comboBox.currentText(),
                self.plot_5_channel_comboBox.currentText()))
        self.plot_5_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_5_title_label,
                self.plot_5_widget, self.plot_5_scope_comboBox.currentText(), 
                self.plot_5_channel_comboBox.currentText()))
        
        # Connections for plot 6 
        self.plot_6_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_6_title_label,
                self.plot_6_widget, self.plot_6_scope_comboBox.currentText(),
                self.plot_6_channel_comboBox.currentText()))
        self.plot_6_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_6_title_label,
                self.plot_6_widget, self.plot_6_scope_comboBox.currentText(), 
                self.plot_6_channel_comboBox.currentText()))
        
        # Connections for plot 7 
        self.plot_7_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_7_title_label,
                self.plot_7_widget, self.plot_7_scope_comboBox.currentText(),
                self.plot_7_channel_comboBox.currentText()))
        self.plot_7_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_7_title_label,
                self.plot_7_widget, self.plot_7_scope_comboBox.currentText(), 
                self.plot_7_channel_comboBox.currentText()))
        
        # Connections for plot 8 
        self.plot_8_scope_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_8_title_label,
                self.plot_8_widget, self.plot_8_scope_comboBox.currentText(),
                self.plot_8_channel_comboBox.currentText()))
        self.plot_8_channel_comboBox.currentIndexChanged.connect(
            lambda: self.plot_data(self.plot_8_title_label,
                self.plot_8_widget, self.plot_8_scope_comboBox.currentText(), 
                self.plot_8_channel_comboBox.currentText()))
        
        # connect collect_data_pushButton to run picoScope script
        self.collect_data_pushButton.clicked.connect(self.run_collect_data_script)

        self.refresh_pushButton.clicked.connect(self.upload_settings)
        self.refresh_pushButton.clicked.connect(self.refresh_plots)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def set_plot_title(self, plot_title, selected_scope, selected_channel):
        settings = QSettings("JC", "PlottingBananza") # company, application name       
        if (selected_channel == 'Channel A'):
            name = settings.value(f"{selected_scope}/{chA_attributes[0]}", "")        
        else:
            name = settings.value(f"{selected_scope}/{chB_attributes[0]}", "")
        plot_title.setText(name)
    
    range_mapper = {0:"0.01", 1:"0.02", 2:"0.05", 3:"0.1", 4:"0.2", 5:"0.5",  6:"1", 7:"2", 
                        8:"5", 9:"10", 10:"20", 11:"50", 12:"100"}
    rate_mapper = {0:"4", 1:"8", 2:"16", 3:"32", 4:"64", 5:"128", 6:"256", 7:"512", 8:"1024"}
    direction_mapper = {0:"ABOVE", 1:"BELOW", 2:"RISING", 3:"FALLING", 4:"RISING_OR_FALLING"}
    coupling_mapper = {0:"AC", 1:"DC"}

    range_toindex_mapper = {"0.01":0, "0.02":1, "0.05":2, "0.1":3, "0.2":4, "0.5":5, "1":6, "2":7, 
                        "5":8, "10":9, "20":10, "50":11, "100":12}
    rate_toindex_mapper = {"4":0, "8":1, "16":2, "32":3, "64":4, "128":5, "256":6, "512":7, "1024":8}
    direction_toindex_mapper = {"ABOVE":0, "BELOW":1, "RISING":2, "FALLING":3, "RISING_OR_FALLING":4}
    coupling_toindex_mapper = {"AC":0, "DC":1}
            

    def upload_settings(self):
        settings = QSettings("JC", "PicoScopeBananza")  # company, application name
        for scope_num in range(1, 5):  # For scopes 1 to 4
            csv_file_path = f'./ENPH455_JC-main/GUI/GUI/scope_settings/scope_{scope_num}_settings.csv'
            currentScope = f"Scope {scope_num}"

            # Read the existing content of the CSV file
            with open(csv_file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

            # Channel A settings with scope identifier
            settings.setValue(f"{currentScope}/{chA_attributes[0]}", rows[0][1]) # chA_name
            settings.setValue(f"{currentScope}/{chA_attributes[1]}", rows[1][1]) # chA_collect
            settings.setValue(f"{currentScope}/{chA_attributes[2]}", self.range_toindex_mapper.get(rows[2][1])) # chA_range
            settings.setValue(f"{currentScope}/{chA_attributes[3]}", self.rate_toindex_mapper.get(rows[3][1])) # chA_rate
            settings.setValue(f"{currentScope}/{chA_attributes[4]}", rows[4][1]) # chA_extra1
            settings.setValue(f"{currentScope}/{chA_attributes[5]}", rows[5][1]) # chA_extra2


            # Channel B settings with scope identifier
            settings.setValue(f"{currentScope}/{chB_attributes[0]}", rows[6][1]) # chB_name
            settings.setValue(f"{currentScope}/{chB_attributes[1]}", rows[7][1]) # chB_collect
            settings.setValue(f"{currentScope}/{chB_attributes[2]}", self.range_toindex_mapper.get(rows[8][1])) # chB_range
            settings.setValue(f"{currentScope}/{chB_attributes[3]}", self.rate_toindex_mapper.get(rows[9][1])) # chB_rate
            settings.setValue(f"{currentScope}/{chB_attributes[4]}", rows[10][1]) # chB_extra1
            settings.setValue(f"{currentScope}/{chB_attributes[5]}", rows[11][1]) # chB_extra2

            # Trigger settings with scope identifier
            settings.setValue(f"{currentScope}/{trigger_attributes[0]}", rows[12][1]) # autotrigger
            settings.setValue(f"{currentScope}/{trigger_attributes[1]}", self.coupling_toindex_mapper.get(rows[13][1])) # coupling
            settings.setValue(f"{currentScope}/{trigger_attributes[2]}", rows[14][1]) # threshold
            settings.setValue(f"{currentScope}/{trigger_attributes[3]}", self.direction_toindex_mapper.get(rows[15][1])) # direction
            settings.setValue(f"{currentScope}/{trigger_attributes[4]}", rows[16][1]) # delay
            settings.setValue(f"{currentScope}/{trigger_attributes[5]}", rows[17][1]) # presample
            settings.setValue(f"{currentScope}/{trigger_attributes[6]}", rows[18][1]) # postsample
            settings.setValue(f"{currentScope}/{trigger_attributes[7]}", rows[19][1]) # downsample

    def run_collect_data_script(self):
        try:
            # Replace 'your_script.py' with the path to your Python script
            subprocess.run(["python", "C:/Users/janec/Desktop/pico_main_dir/picoV2/picosdk-python-wrappers-master/ps4000Examples/pico_scope_setup.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running script: {e}")

    def plot_data(self, plot_title, plot_widget, selected_scope, selected_channel):
        # Check if valid selections are made
        if selected_scope != "Select scope" and selected_channel != "Select channel":

            # set plot title
            self.set_plot_title(plot_title, selected_scope, selected_channel)

            # plot data
            file_path = f"./GUI/collected_data/{selected_scope}/{selected_channel}/data.csv"
            try:
                data = pd.read_csv(file_path)
                plot_widget.clear()
                plot_widget.plot(data[ 'Time (ns)'], data['Voltage (mV)'])
                plot_widget.setLabel('left', 'Voltage (mV)')  # Y-axis
                plot_widget.setLabel('bottom', 'Time (ns)')  # X-axis
            except FileNotFoundError:
                print(f"File not found: {file_path}")
        else:
            plot_widget.clear()  # Clear the plot if selections are invalid

    def refresh_plots(self):
        for plot_num in range(1, 9):  # for 8 plots
            plot_title_label = getattr(self, f'plot_{plot_num}_title_label')
            plot_widget = getattr(self, f'plot_{plot_num}_widget')
            scope_comboBox = getattr(self, f'plot_{plot_num}_scope_comboBox')
            channel_comboBox = getattr(self, f'plot_{plot_num}_channel_comboBox')
            
            selected_scope = scope_comboBox.currentText()
            selected_channel = channel_comboBox.currentText()
            
            # Call plot_data to refresh the plot
            self.plot_data(plot_title_label, plot_widget, selected_scope, selected_channel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.main_window_groupBox.setTitle(_translate("MainWindow", "Main Display"))
        self.controls_groupBox.setTitle(_translate("MainWindow", "Controls"))
        self.shot_counter_label.setText(_translate("MainWindow", "Shot Counter: "))
        self.scope_control_pushButton.setText(_translate("MainWindow", "Scope control"))
        self.collect_data_pushButton.setText(_translate("MainWindow", "Begin data collection"))
        self.refresh_pushButton.setText(_translate("MainWindow", "Refresh plots"))
        self.plots_groupBox.setTitle(_translate("MainWindow", "Plots"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())