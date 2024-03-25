# scope_control.py
# February 2024
# Jane Cohen

# Form implementation generated from reading ui file 'scope_control.ui'
# Created by: PyQt5 UI code generator 5.15.9

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtCore import QSettings
import csv

NUM_SCOPE = 4 #number of scopes
chA_attributes = ["chA_name", "chA_collect", "chA_range", "chA_rate", "chA_autotrigger", 
                  "chA_coupling", "chA_threshold", "chA_direction", "chA_delay", "chA_presample",
                  "chA_postsample", "chA_extra1", "chA_extra2"]

chB_attributes = ["chB_name", "chB_collect", "chB_range", "chB_rate", "chB_autotrigger", 
                  "chB_coupling", "chB_threshold", "chB_direction", "chB_delay", "chB_presample",
                  "chB_postsample", "chB_extra1", "chB_extra2"]


class Ui_ScopeControlWindow(object):
    def setupUi(self, ScopeControlWindow):
        ScopeControlWindow.setObjectName("ScopeControlWindow")
        ScopeControlWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(ScopeControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scope_control_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.scope_control_groupBox.setObjectName("scope_control_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scope_control_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.select_scope_groupBox = QtWidgets.QGroupBox(self.scope_control_groupBox)
        self.select_scope_groupBox.setObjectName("select_scope_groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.select_scope_groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.select_scope_label = QtWidgets.QLabel(self.select_scope_groupBox)
        self.select_scope_label.setObjectName("select_scope_label")
        self.horizontalLayout_3.addWidget(self.select_scope_label)
        self.select_scope_comboBox = QtWidgets.QComboBox(self.select_scope_groupBox)
        self.select_scope_comboBox.setObjectName("select_scope_comboBox")
        self.horizontalLayout_3.addWidget(self.select_scope_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.select_scope_groupBox)
        self.channel_control_groupBox = QtWidgets.QGroupBox(self.scope_control_groupBox)
        self.channel_control_groupBox.setObjectName("channel_control_groupBox")
        #self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.channel_control_groupBox)
        #self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # channel A set up
        self.channel_A_groupBox = QtWidgets.QGroupBox(self.channel_control_groupBox)
        self.channel_A_groupBox.setObjectName("channel_A_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.channel_A_groupBox)
        self.gridLayout.setObjectName("gridLayout")

        self.chA_name_label = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_name_label.setObjectName("chA_name_label")
        self.gridLayout.addWidget(self.chA_name_label, 1, 0, 1, 1)        
        self.chA_collect_checkBox = QtWidgets.QCheckBox(self.channel_A_groupBox)
        self.chA_collect_checkBox.setText("")
        self.chA_collect_checkBox.setObjectName("chA_collect_checkBox")
        self.gridLayout.addWidget(self.chA_collect_checkBox, 2, 2, 1, 2)
        self.chA_extra1_hover = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_extra1_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chA_extra1_hover.setObjectName("chA_extra1_hover")
        self.gridLayout.addWidget(self.chA_extra1_hover, 13, 5, 1, 1)
        self.chA_extra2_hover = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_extra2_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chA_extra2_hover.setObjectName("chA_extra2_hover")
        self.gridLayout.addWidget(self.chA_extra2_hover, 14, 5, 1, 1)
        self.chA_rate_label = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_rate_label.setObjectName("chA_rate_label")
        self.gridLayout.addWidget(self.chA_rate_label, 5, 0, 1, 1)
        self.chA_rate_comboBox = QtWidgets.QComboBox(self.channel_A_groupBox)
        self.chA_rate_comboBox.setObjectName("chA_rate_comboBox")
        self.gridLayout.addWidget(self.chA_rate_comboBox, 5, 3, 1, 1)
        self.chA_reset_pushButton = QtWidgets.QPushButton(self.channel_A_groupBox)
        self.chA_reset_pushButton.setObjectName("chA_reset_pushButton")
        self.gridLayout.addWidget(self.chA_reset_pushButton, 20, 0, 1, 4)
        self.chA_extra2_lineEdit = QtWidgets.QLineEdit(self.channel_A_groupBox)
        self.chA_extra2_lineEdit.setObjectName("chA_extra2_lineEdit")
        self.gridLayout.addWidget(self.chA_extra2_lineEdit, 14, 3, 1, 1)
        self.chA_range_label = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_range_label.setObjectName("chA_range_label")
        self.gridLayout.addWidget(self.chA_range_label, 3, 0, 1, 3)
        self.chA_extra2_label = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_extra2_label.setObjectName("chA_extra2_label")
        self.gridLayout.addWidget(self.chA_extra2_label, 14, 0, 1, 1)
        self.chA_rate_hover = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_rate_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chA_rate_hover.setObjectName("chA_rate_hover")
        self.gridLayout.addWidget(self.chA_rate_hover, 5, 5, 1, 1)
        self.chA_name_lineEdit = QtWidgets.QLineEdit(self.channel_A_groupBox)
        self.chA_name_lineEdit.setObjectName("chA_name_lineEdit")
        self.gridLayout.addWidget(self.chA_name_lineEdit, 1, 3, 1, 1)
        self.chA_collect_label = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_collect_label.setObjectName("chA_collect_label")
        self.gridLayout.addWidget(self.chA_collect_label, 2, 0, 1, 2)
        self.chA_range_hover = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_range_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chA_range_hover.setObjectName("chA_range_hover")
        self.gridLayout.addWidget(self.chA_range_hover, 3, 5, 1, 1)
        self.chA_extra1_lineEdit = QtWidgets.QLineEdit(self.channel_A_groupBox)
        self.chA_extra1_lineEdit.setObjectName("chA_extra1_lineEdit")
        self.gridLayout.addWidget(self.chA_extra1_lineEdit, 13, 3, 1, 1)
        self.chA_range_comboBox = QtWidgets.QComboBox(self.channel_A_groupBox)
        self.chA_range_comboBox.setObjectName("chA_range_comboBox")
        self.gridLayout.addWidget(self.chA_range_comboBox, 3, 3, 1, 2)
        self.chA_extra1_label = QtWidgets.QLabel(self.channel_A_groupBox)
        self.chA_extra1_label.setObjectName("chA_extra1_label")
        self.gridLayout.addWidget(self.chA_extra1_label, 13, 0, 1, 1)

        self.gridLayout.setColumnStretch(4, 6)
        self.gridLayout.setColumnStretch(5, 2)
        #self.horizontalLayout_2.addWidget(self.channel_A_groupBox)


        # channel B set up
        self.channel_B_groupBox = QtWidgets.QGroupBox(self.channel_control_groupBox)
        self.channel_B_groupBox.setObjectName("channel_B_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.channel_B_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chB_rate_comboBox = QtWidgets.QComboBox(self.channel_B_groupBox)
        self.chB_rate_comboBox.setObjectName("chB_rate_comboBox")
        self.gridLayout_2.addWidget(self.chB_rate_comboBox, 5, 3, 1, 1)
        self.chB_collect_label = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_collect_label.setObjectName("chB_collect_label")
        self.gridLayout_2.addWidget(self.chB_collect_label, 2, 0, 1, 2)
        self.chB_range_comboBox = QtWidgets.QComboBox(self.channel_B_groupBox)
        self.chB_range_comboBox.setObjectName("chB_range_comboBox")
        self.gridLayout_2.addWidget(self.chB_range_comboBox, 3, 3, 1, 2)
        self.chB_extra1_lineEdit = QtWidgets.QLineEdit(self.channel_B_groupBox)
        self.chB_extra1_lineEdit.setObjectName("chB_extra1_lineEdit")
        self.gridLayout_2.addWidget(self.chB_extra1_lineEdit, 13, 3, 1, 1)
        self.chB_collect_checkBox = QtWidgets.QCheckBox(self.channel_B_groupBox)
        self.chB_collect_checkBox.setText("")
        self.chB_collect_checkBox.setObjectName("chB_collect_checkBox")
        self.gridLayout_2.addWidget(self.chB_collect_checkBox, 2, 2, 1, 2)
        self.chB_name_lineEdit = QtWidgets.QLineEdit(self.channel_B_groupBox)
        self.chB_name_lineEdit.setObjectName("chB_name_lineEdit")
        self.gridLayout_2.addWidget(self.chB_name_lineEdit, 1, 3, 1, 1)
        
        self.chB_name_label = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_name_label.setObjectName("chB_name_label")
        self.gridLayout_2.addWidget(self.chB_name_label, 1, 0, 1, 1)
        self.chB_range_hover = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_range_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chB_range_hover.setObjectName("chB_range_hover")
        self.gridLayout_2.addWidget(self.chB_range_hover, 3, 5, 1, 1)
        self.chB_extra1_label = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_extra1_label.setObjectName("chB_extra1_label")
        self.gridLayout_2.addWidget(self.chB_extra1_label, 13, 0, 1, 1)
        self.chB_rate_label = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_rate_label.setObjectName("chB_rate_label a")
        self.gridLayout_2.addWidget(self.chB_rate_label, 5, 0, 1, 1)
        self.chB_rate_hover = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_rate_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chB_rate_hover.setObjectName("chB_rate_hover")
        self.gridLayout_2.addWidget(self.chB_rate_hover, 5, 5, 1, 1)
        self.chB_reset_pushButton = QtWidgets.QPushButton(self.channel_B_groupBox)
        self.chB_reset_pushButton.setObjectName("chB_reset_pushButton")
        self.gridLayout_2.addWidget(self.chB_reset_pushButton, 20, 0, 1, 4)
        self.chB_range_label = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_range_label.setObjectName("chB_range_label")
        self.gridLayout_2.addWidget(self.chB_range_label, 3, 0, 1, 3)
        self.chB_extra2_label = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_extra2_label.setObjectName("chB_extra2_label")
        self.gridLayout_2.addWidget(self.chB_extra2_label, 14, 0, 1, 1)
        self.chB_extra2_lineEdit = QtWidgets.QLineEdit(self.channel_B_groupBox)
        self.chB_extra2_lineEdit.setObjectName("chB_extra2_lineEdit")
        self.gridLayout_2.addWidget(self.chB_extra2_lineEdit, 14, 3, 1, 1)
        self.chB_extra1_hover = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_extra1_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chB_extra1_hover.setObjectName("chB_extra1_hover")
        self.gridLayout_2.addWidget(self.chB_extra1_hover, 13, 5, 1, 1)
        self.chB_extra2_hover = QtWidgets.QLabel(self.channel_B_groupBox)
        self.chB_extra2_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.chB_extra2_hover.setObjectName("chB_extra2_hover")


        # trigger control group box setup
        self.trigger_control_groupBox = QtWidgets.QGroupBox(self.channel_control_groupBox)
        self.trigger_control_groupBox.setObjectName("trigger_control_groupBox")
        self.gridLayout_trigger = QtWidgets.QGridLayout(self.trigger_control_groupBox)
        self.gridLayout_trigger.setObjectName("gridLayout_trigger")
 
        self.delay_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.delay_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.delay_hover.setObjectName("delay_hover")
        self.gridLayout_trigger.addWidget(self.delay_hover, 10, 5, 1, 1)
        self.threshold_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.threshold_label.setObjectName("threshold_label")
        self.gridLayout_trigger.addWidget(self.threshold_label, 9, 0, 1, 1)
        self.presample_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.presample_label.setObjectName("presample_label")
        self.gridLayout_trigger.addWidget(self.presample_label, 11, 0, 1, 1)
        self.coupling_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.coupling_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.coupling_hover.setObjectName("coupling_hover")
        self.gridLayout_trigger.addWidget(self.coupling_hover, 7, 5, 1, 1)
        self.postsample_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.postsample_label.setObjectName("postsample_label")
        self.gridLayout_trigger.addWidget(self.postsample_label, 12, 0, 1, 1)
        self.autotrigger_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.autotrigger_label.setObjectName("autotrigger_label")
        self.gridLayout_trigger.addWidget(self.autotrigger_label, 8, 0, 1, 1)
        self.delay_lineEdit = QtWidgets.QLineEdit(self.trigger_control_groupBox)
        self.delay_lineEdit.setObjectName("delay_lineEdit")
        self.gridLayout_trigger.addWidget(self.delay_lineEdit, 10, 3, 1, 1)
        self.direction_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.direction_label.setObjectName("direction_label")
        self.gridLayout_trigger.addWidget(self.direction_label, 6, 0, 1, 3)
        self.autotrigger_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.autotrigger_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.autotrigger_hover.setObjectName("autotrigger_hover")
        self.gridLayout_trigger.addWidget(self.autotrigger_hover, 8, 5, 1, 1)
        self.coupling_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.coupling_label.setObjectName("coupling_label")
        self.gridLayout_trigger.addWidget(self.coupling_label, 7, 0, 1, 3)
        self.threshold_lineEdit = QtWidgets.QLineEdit(self.trigger_control_groupBox)
        self.threshold_lineEdit.setObjectName("threshold_lineEdit")
        self.gridLayout_trigger.addWidget(self.threshold_lineEdit, 9, 3, 1, 1)
        self.delay_label = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.delay_label.setObjectName("delay_label")
        self.gridLayout_trigger.addWidget(self.delay_label, 10, 0, 1, 1)
        self.postsample_lineEdit = QtWidgets.QLineEdit(self.trigger_control_groupBox)
        self.postsample_lineEdit.setObjectName("postsample_lineEdit")
        self.gridLayout_trigger.addWidget(self.postsample_lineEdit, 12, 3, 1, 1)
        self.presample_lineEdit = QtWidgets.QLineEdit(self.trigger_control_groupBox)
        self.presample_lineEdit.setObjectName("presample_lineEdit")
        self.gridLayout_trigger.addWidget(self.presample_lineEdit, 11, 3, 1, 1)
        self.direction_comboBox = QtWidgets.QComboBox(self.trigger_control_groupBox)
        self.direction_comboBox.setObjectName("direction_comboBox")
        self.gridLayout_trigger.addWidget(self.direction_comboBox, 6, 3, 1, 2)
        self.autotrigger_lineEdit = QtWidgets.QLineEdit(self.trigger_control_groupBox)
        self.autotrigger_lineEdit.setObjectName("autotrigger_lineEdit")
        self.gridLayout_trigger.addWidget(self.autotrigger_lineEdit, 8, 3, 1, 1)
        self.postsample_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.postsample_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.postsample_hover.setObjectName("postsample_hover")
        self.gridLayout_trigger.addWidget(self.postsample_hover, 12, 5, 1, 1)
        self.threshold_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.threshold_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.threshold_hover.setObjectName("threshold_hover")
        self.gridLayout_trigger.addWidget(self.threshold_hover, 9, 5, 1, 1)
        self.direction_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.direction_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.direction_hover.setObjectName("direction_hover")
        self.gridLayout_trigger.addWidget(self.direction_hover, 6, 5, 1, 1)
        self.coupling_comboBox = QtWidgets.QComboBox(self.trigger_control_groupBox)
        self.coupling_comboBox.setObjectName("coupling_comboBox")
        self.gridLayout_trigger.addWidget(self.coupling_comboBox, 7, 3, 1, 2)

        self.presample_hover = QtWidgets.QLabel(self.trigger_control_groupBox)
        self.presample_hover.setStyleSheet("QLabel{\n"
"    background-color: rgb(110,110,186);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Candara\";\n"
"}")
        self.presample_hover.setObjectName("presample_hover")
        self.gridLayout_trigger.addWidget(self.presample_hover, 11, 5, 1, 1)
        self.trigger_reset_pushButton = QtWidgets.QPushButton(self.channel_B_groupBox)
        self.trigger_reset_pushButton.setObjectName("trigger_reset_pushButton")
        self.gridLayout_2.addWidget(self.trigger_reset_pushButton, 20, 0, 1, 4)

        # Set horizontal layout for channel_control_groupBox and add the group boxes
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.channel_control_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.channel_A_groupBox)
        self.horizontalLayout_2.addWidget(self.channel_B_groupBox)
        self.horizontalLayout_2.addWidget(self.trigger_control_groupBox)
        self.gridLayout_2.addWidget(self.chB_extra2_hover, 14, 5, 1, 1)
        self.gridLayout_2.setColumnStretch(4, 6)
        self.gridLayout_2.setColumnStretch(5, 2)
        self.verticalLayout_4.addWidget(self.channel_control_groupBox)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.horizontalLayout.addWidget(self.scope_control_groupBox)

        # add options to select_scope_comboBox
        self.select_scope_comboBox.addItems(["Scope 1", "Scope 2", "Scope 3", "Scope 4"])

        # Ensure the loadSettings function is called not only at initialization but also when the scope selection changes
        self.select_scope_comboBox.currentIndexChanged.connect(self.loadSettings)

        # add options to channel control comboBoxes
        self.chA_range_comboBox.addItems(["0.01", "0.02", "0.05", "0.1", "0.2", "0.5", 
                                                           "1", "2", "5", "10", "20", "50", "100"]) # V
        self.chB_range_comboBox.addItems(["0.01", "0.02", "0.05", "0.1", "0.2", "0.5", 
                                                           "1", "2", "5", "10", "20", "50", "100"]) # V        
        self.chA_rate_comboBox.addItems(["4", "8", "16", "32", "64", "128", 
                                                           "256", "512", "1024"])  # ns
        self.chB_rate_comboBox.addItems(["4", "8", "16", "32", "64", "128", 
                                                           "256", "512", "1024"])  # ns
        self.direction_comboBox.addItems(["ABOVE", "BELOW", "RISING", 
                                                               "FALLING", "RISING_OR_FALLING"])  # ns
        self.coupling_comboBox.addItems(["AC", "DC"]) 

        # tooltips for hover objects
        self.chA_range_hover.enterEvent = self.show_range_dialog
        self.chA_range_hover.leaveEvent = self.hide_dialog
        self.chB_range_hover.enterEvent = self.show_range_dialog
        self.chB_range_hover.leaveEvent = self.hide_dialog

        self.chA_rate_hover.enterEvent = self.show_rate_dialog
        self.chA_rate_hover.leaveEvent = self.hide_dialog
        self.chB_rate_hover.enterEvent = self.show_rate_dialog
        self.chB_rate_hover.leaveEvent = self.hide_dialog

        self.direction_hover.enterEvent = self.show_direction_dialog
        self.direction_hover.leaveEvent = self.hide_dialog

        self.coupling_hover.enterEvent = self.show_coupling_dialog
        self.coupling_hover.leaveEvent = self.hide_dialog

        self.autotrigger_hover.enterEvent = self.show_autotrigger_dialog
        self.autotrigger_hover.leaveEvent = self.hide_dialog

        self.threshold_hover.enterEvent = self.show_threshold_dialog
        self.threshold_hover.leaveEvent = self.hide_dialog

        self.delay_hover.enterEvent = self.show_threshold_dialog
        self.delay_hover.leaveEvent = self.hide_dialog

        self.presample_hover.enterEvent = self.show_presample_dialog
        self.presample_hover.leaveEvent = self.hide_dialog

        self.postsample_hover.enterEvent = self.show_postsample_dialog
        self.postsample_hover.leaveEvent = self.hide_dialog

        ScopeControlWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ScopeControlWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 22))
        self.menubar.setObjectName("menubar")
        ScopeControlWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ScopeControlWindow)
        self.statusbar.setObjectName("statusbar")
        ScopeControlWindow.setStatusBar(self.statusbar)

        # update settings button
        self.updateSettingsButton = QtWidgets.QPushButton(self.scope_control_groupBox)
        self.updateSettingsButton.setObjectName("updateSettingsButton")
        self.updateSettingsButton.setText("Update Settings")
        self.verticalLayout_4.addWidget(self.updateSettingsButton)
        self.updateSettingsButton.clicked.connect(self.downloadSettings)

        self.retranslateUi(ScopeControlWindow)
        QtCore.QMetaObject.connectSlotsByName(ScopeControlWindow)

        # connect signals 
        self.connectSettings()

        # load settings
        self.loadSettings()

        # connect reset buttons
        self.chA_reset_pushButton.clicked.connect(self.applyDefaultSettingsA)
        self.chB_reset_pushButton.clicked.connect(self.applyDefaultSettingsB)
        self.trigger_reset_pushButton.clicked.connect(self.applyDefaultSettingsTrigger)


  
    def saveSettings(self):
        currentScope = self.select_scope_comboBox.currentText()  # identifies the selected scope

        settings = QSettings("JC", "PicoScopeBananza") # company, application name

        # Channel A settings with scope identifier
        settings.setValue(f"{currentScope}/{chA_attributes[0]}", self.chA_name_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[1]}", self.chA_collect_checkBox.isChecked())
        settings.setValue(f"{currentScope}/{chA_attributes[2]}", self.chA_range_comboBox.currentIndex())
        settings.setValue(f"{currentScope}/{chA_attributes[3]}", self.chA_rate_comboBox.currentIndex())
        settings.setValue(f"{currentScope}/{chA_attributes[4]}", self.autotrigger_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[5]}", self.coupling_comboBox.currentIndex())
        settings.setValue(f"{currentScope}/{chA_attributes[6]}", self.threshold_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[7]}", self.direction_comboBox.currentIndex())
        settings.setValue(f"{currentScope}/{chA_attributes[8]}", self.delay_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[9]}", self.presample_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[10]}", self.postsample_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[11]}", self.chA_extra1_lineEdit.text())
        settings.setValue(f"{currentScope}/{chA_attributes[12]}", self.chA_extra2_lineEdit.text())

        #  Channel B settings with scope identifier
        settings.setValue(f"{currentScope}/{chB_attributes[0]}", self.chB_name_lineEdit.text())
        settings.setValue(f"{currentScope}/{chB_attributes[1]}", self.chB_collect_checkBox.isChecked())
        settings.setValue(f"{currentScope}/{chB_attributes[2]}", self.chB_range_comboBox.currentIndex())
        settings.setValue(f"{currentScope}/{chB_attributes[3]}", self.chB_rate_comboBox.currentIndex())
        settings.setValue(f"{currentScope}/{chB_attributes[11]}", self.chB_extra1_lineEdit.text())
        settings.setValue(f"{currentScope}/{chB_attributes[12]}", self.chB_extra2_lineEdit.text())


    def loadSettings(self):
        currentScope = self.select_scope_comboBox.currentText()  # Identifies the selected scope
        settings = QSettings("JC", "PicoScopeBananza") # company, application name

        # disconnect changes from triggering saveSettings
        self.disconnectSettings()

        # Channel A settings with scope identifier
        self.chA_name_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[0]}", ""))
        self.chA_collect_checkBox.setChecked(settings.value(f"{currentScope}/{chA_attributes[1]}", False, type=bool))
        self.chA_range_comboBox.setCurrentIndex(int(settings.value(f"{currentScope}/{chA_attributes[2]}", 0)))
        self.chA_rate_comboBox.setCurrentIndex(int(settings.value(f"{currentScope}/{chA_attributes[3]}", 0)))
        self.autotrigger_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[4]}", ""))
        self.coupling_comboBox.setCurrentIndex(int(settings.value(f"{currentScope}/{chA_attributes[5]}", 0)))
        self.threshold_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[6]}", ""))
        self.direction_comboBox.setCurrentIndex(int(settings.value(f"{currentScope}/{chA_attributes[7]}", 0)))
        self.delay_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[8]}", ""))
        self.presample_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[9]}", ""))
        self.postsample_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[10]}", ""))
        self.chA_extra1_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[11]}", ""))
        self.chA_extra2_lineEdit.setText(settings.value(f"{currentScope}/{chA_attributes[12]}", ""))

        # Channel B settings with scope identifier
        self.chB_name_lineEdit.setText(settings.value(f"{currentScope}/{chB_attributes[0]}", ""))
        self.chB_collect_checkBox.setChecked(settings.value(f"{currentScope}/{chB_attributes[1]}", False, type=bool))
        self.chB_range_comboBox.setCurrentIndex(int(settings.value(f"{currentScope}/{chB_attributes[2]}", 0)))
        self.chB_rate_comboBox.setCurrentIndex(int(settings.value(f"{currentScope}/{chB_attributes[3]}", 0)))
        self.chB_extra1_lineEdit.setText(settings.value(f"{currentScope}/{chB_attributes[11]}", ""))
        self.chB_extra2_lineEdit.setText(settings.value(f"{currentScope}/{chB_attributes[12]}", ""))
        
        print("Settings loaded for ", currentScope)

        # reconnect signals
        self.connectSettings()

    def connectSettings(self):
         # connect signals to save settings whenever they are changed
        self.chA_name_lineEdit.textChanged.connect(self.saveSettings)
        self.chA_collect_checkBox.stateChanged.connect(self.saveSettings)
        self.chA_range_comboBox.currentIndexChanged.connect(self.saveSettings)
        self.chA_rate_comboBox.currentIndexChanged.connect(self.saveSettings)
        self.autotrigger_lineEdit.textChanged.connect(self.saveSettings)
        self.coupling_comboBox.currentIndexChanged.connect(self.saveSettings)
        self.threshold_lineEdit.textChanged.connect(self.saveSettings)
        self.direction_comboBox.currentIndexChanged.connect(self.saveSettings)
        self.delay_lineEdit.textChanged.connect(self.saveSettings)
        self.presample_lineEdit.textChanged.connect(self.saveSettings)
        self.postsample_lineEdit.textChanged.connect(self.saveSettings)
        self.chA_extra1_lineEdit.textChanged.connect(self.saveSettings)
        self.chA_extra2_lineEdit.textChanged.connect(self.saveSettings)

        self.chB_name_lineEdit.textChanged.connect(self.saveSettings)
        self.chB_collect_checkBox.stateChanged.connect(self.saveSettings)
        self.chB_range_comboBox.currentIndexChanged.connect(self.saveSettings)
        self.chB_rate_comboBox.currentIndexChanged.connect(self.saveSettings)
        self.chB_extra1_lineEdit.textChanged.connect(self.saveSettings)
        self.chB_extra2_lineEdit.textChanged.connect(self.saveSettings)

    def disconnectSettings(self):
         # disconnect signals
        self.chA_name_lineEdit.textChanged.disconnect(self.saveSettings)
        self.chA_collect_checkBox.stateChanged.disconnect(self.saveSettings)
        self.chA_range_comboBox.currentIndexChanged.disconnect(self.saveSettings)
        self.chA_rate_comboBox.currentIndexChanged.disconnect(self.saveSettings)
        self.autotrigger_lineEdit.textChanged.disconnect(self.saveSettings)
        self.coupling_comboBox.currentIndexChanged.disconnect(self.saveSettings)
        self.threshold_lineEdit.textChanged.disconnect(self.saveSettings)
        self.direction_comboBox.currentIndexChanged.disconnect(self.saveSettings)
        self.delay_lineEdit.textChanged.disconnect(self.saveSettings)
        self.presample_lineEdit.textChanged.disconnect(self.saveSettings)
        self.postsample_lineEdit.textChanged.disconnect(self.saveSettings)
        self.chA_extra1_lineEdit.textChanged.disconnect(self.saveSettings)
        self.chA_extra2_lineEdit.textChanged.disconnect(self.saveSettings)

        self.chB_name_lineEdit.textChanged.disconnect(self.saveSettings)
        self.chB_collect_checkBox.stateChanged.disconnect(self.saveSettings)
        self.chB_range_comboBox.currentIndexChanged.disconnect(self.saveSettings)
        self.chB_rate_comboBox.currentIndexChanged.disconnect(self.saveSettings)
        self.chB_extra1_lineEdit.textChanged.disconnect(self.saveSettings)
        self.chB_extra2_lineEdit.textChanged.disconnect(self.saveSettings)
         
    def indexToValue(self,row):
        range_mapper = {0:"0.01", 1:"0.02", 2:"0.05", 3:"0.1", 4:"0.2", 5:"0.5",  6:"1", 7:"2", 
                        8:"5", 9:"10", 10:"20", 11:"50", 12:"100"}
        rate_mapper = {0:"4", 1:"8", 2:"16", 3:"32", 4:"64", 5:"128", 6:"256", 7:"512", 8:"1024"}
        direction_mapper = {0:"ABOVE", 1:"BELOW", 2:"RISING", 3:"FALLING", 4:"RISING_OR_FALLING"}
        coupling_mapper = {0:"AC", 1:"DC"}
        
        row[4] = range_mapper.get(row[4])
        row[5] = rate_mapper.get(row[5])
        row[9] = direction_mapper.get(row[9])
        row[7] = coupling_mapper.get(row[7])

        return(row)


    def downloadSettings(self):
        csv_file_path = './GUI/scope_settings.csv'
        settings = QSettings("JC", "PicoScopeBananza") # company, application name

        # Data to be written
        chA_data, chB_data = [], []

        for scope in range(1, NUM_SCOPE+1):  # For scopes 1-4
                chA_row, chB_row = [], []
                chA_row.append(scope)
                chA_row.append('A')
                chB_row.append(scope)
                chB_row.append('B')
                for fieldA, fieldB in zip(chA_attributes, chB_attributes):
                        valA = settings.value(f"Scope {scope}/{fieldA}", "")
                        chA_row.append(valA)
                        valB = settings.value(f"Scope {scope}/{fieldB}", "")
                        chB_row.append(valB)
                chA_row = self.indexToValue(chA_row)
                chB_row = self.indexToValue(chB_row)
                chA_data.append(chA_row)
                chB_data.append(chB_row)

        # Read the first row
        with open(csv_file_path, mode='r') as file:
                reader = csv.reader(file)
                first_row = next(reader)

        # Write the first row and then the data
        with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(first_row)  # Write the original first row
                writer.writerows(chA_data)  # Write the new data starting from the second row
                writer.writerows(chB_data)  # Write the new data starting from the second row

        print("Settings updated for all scopes")


    def readDefaultSettings(self):
        defaults = {}
        with open('./GUI/default_settings.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                        if ':' in line:
                                key, value = line.split(':', 1)
                                defaults[key.strip()] = value.strip()
        return defaults

    def applyDefaultSettingsA(self):
        defaults = self.readDefaultSettings()

        # Set the text fields and checkboxes directly from the defaults
        self.chA_name_lineEdit.setText(defaults.get("Channel name", ""))
        self.chA_collect_checkBox.setChecked(int(defaults.get("Collect data", 0)))
        self.autotrigger_lineEdit.setText(defaults.get("Autotrigger", ""))
        self.threshold_lineEdit.setText(defaults.get("Threshold", ""))
        self.delay_lineEdit.setText(defaults.get("Delay", ""))
        self.presample_lineEdit.setText(defaults.get("Presample", ""))
        self.postsample_lineEdit.setText(defaults.get("postsample", ""))  # Note the lowercase 'p' in 'postsample' as in your defaults
        self.chA_extra1_lineEdit.setText(defaults.get("extra1", ""))
        self.chA_extra2_lineEdit.setText(defaults.get("extra2", ""))

        # For combo boxes, find the index that corresponds to the default value
        # This assumes you have set up the combo boxes with consistent items
        voltage_range_index = self.chA_range_comboBox.findText(defaults.get("Voltage range", ""), QtCore.Qt.MatchFixedString)
        self.chA_range_comboBox.setCurrentIndex(voltage_range_index if voltage_range_index >= 0 else 0)

        sampling_rate_index = self.chA_rate_comboBox.findText(defaults.get("Sampling rate", ""), QtCore.Qt.MatchFixedString)
        self.chA_rate_comboBox.setCurrentIndex(sampling_rate_index if sampling_rate_index >= 0 else 0)

        coupling_mode_index = self.coupling_comboBox.findText(defaults.get("Coupling mode", ""), QtCore.Qt.MatchFixedString)
        self.coupling_comboBox.setCurrentIndex(coupling_mode_index if coupling_mode_index >= 0 else 0)

        direction_index = self.direction_comboBox.findText(defaults.get("Direction", ""), QtCore.Qt.MatchFixedString)
        self.direction_comboBox.setCurrentIndex(direction_index if direction_index >= 0 else 0)

    def applyDefaultSettingsB(self):
        defaults = self.readDefaultSettings()

        # Set the text fields and checkboxes directly from the defaults
        self.chB_name_lineEdit.setText(defaults.get("Channel name", ""))
        self.chB_collect_checkBox.setChecked(int(defaults.get("Collect data", 0)))
        self.chB_extra1_lineEdit.setText(defaults.get("extra1", ""))
        self.chB_extra2_lineEdit.setText(defaults.get("extra2", ""))

        # For combo boxes, find the index that corresponds to the default value
        # This assumes you have set up the combo boxes with consistent items
        voltage_range_index = self.chB_range_comboBox.findText(defaults.get("Voltage range", ""), QtCore.Qt.MatchFixedString)
        self.chB_range_comboBox.setCurrentIndex(voltage_range_index if voltage_range_index >= 0 else 0)

        sampling_rate_index = self.chB_rate_comboBox.findText(defaults.get("Sampling rate", ""), QtCore.Qt.MatchFixedString)
        self.chB_rate_comboBox.setCurrentIndex(sampling_rate_index if sampling_rate_index >= 0 else 0)

    def show_range_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Select voltage range (in V)")

    def show_rate_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Select timebase in ns")

    def show_direction_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Select the direction the signal must move to cause a trigger")

    def show_coupling_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Select AC or DC coupling")

    def show_autotrigger_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Enter time until auto trigger in ns")
   
    def show_threshold_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Enter ADC count at which the trigger will fire")

    def show_delay_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Enter time, in sample periods, between the trigger occurring and the first sample being taken")

    def show_presample_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Enter number of pre trigger samples")

    def show_postsample_dialog(self, event):
        QToolTip.showText(event.globalPos(), "Enter number of post trigger samples")


    def hide_dialog(self, event):
        QToolTip.hideText()

    def retranslateUi(self, ScopeControlWindow):
        _translate = QtCore.QCoreApplication.translate
        ScopeControlWindow.setWindowTitle(_translate("ScopeControlWindow", "Main Window"))
        self.scope_control_groupBox.setTitle(_translate("ScopeControlWindow", "Scope control"))
        self.select_scope_groupBox.setTitle(_translate("ScopeControlWindow", "Select scope"))
        self.select_scope_label.setText(_translate("ScopeControlWindow", "Scope"))
        self.channel_control_groupBox.setTitle(_translate("ScopeControlWindow", "Channel control"))

        # channel A controls
        self.channel_A_groupBox.setTitle(_translate("ScopeControlWindow", "Channel A"))
        self.chA_name_label.setText(_translate("ScopeControlWindow", "Channel name:"))
        self.chA_extra1_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chA_extra2_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chA_rate_label.setText(_translate("ScopeControlWindow", "Sampling rate:"))
        self.chA_reset_pushButton.setText(_translate("ScopeControlWindow", "Reset to default"))
        self.chA_range_label.setText(_translate("ScopeControlWindow", "Voltage range:"))
        self.chA_extra2_label.setText(_translate("ScopeControlWindow", "Extra 2"))
        self.chA_rate_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chA_collect_label.setText(_translate("ScopeControlWindow", "Collect data?"))
        self.chA_range_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chA_extra1_label.setText(_translate("ScopeControlWindow", "Extra 1"))

        # channel B controls
        self.channel_B_groupBox.setTitle(_translate("ScopeControlWindow", "Channel B"))
        self.chB_collect_label.setText(_translate("ScopeControlWindow", "Collect data?"))
        self.chB_rate_label.setText(_translate("ScopeControlWindow", "Sampling rate:"))
        self.chB_name_label.setText(_translate("ScopeControlWindow", "Channel name:"))
        self.chB_range_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chB_extra1_label.setText(_translate("ScopeControlWindow", "Extra 1"))
        self.chB_rate_label.setText(_translate("ScopeControlWindow", "Sampling rate:"))
        self.chB_rate_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chB_reset_pushButton.setText(_translate("ScopeControlWindow", "Reset to default"))
        self.chB_range_label.setText(_translate("ScopeControlWindow", "Voltage range:"))
        self.chB_extra2_label.setText(_translate("ScopeControlWindow", "Extra 2"))
        self.chB_extra1_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.chB_extra2_hover.setText(_translate("ScopeControlWindow", "  ?"))

        # trigger controls
        self.trigger_control_groupBox.setTitle(_translate("ScopeControlWindow", "Trigger"))
        self.delay_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.threshold_label.setText(_translate("ScopeControlWindow", "Threshold:"))
        self.presample_label.setText(_translate("ScopeControlWindow", "Pretrigger samples:"))
        self.coupling_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.postsample_label.setText(_translate("ScopeControlWindow", "Post trigger samples:"))
        self.autotrigger_label.setText(_translate("ScopeControlWindow", "Auto trigger:"))
        self.direction_label.setText(_translate("ScopeControlWindow", "Direction:"))
        self.autotrigger_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.coupling_label.setText(_translate("ScopeControlWindow", "Coupling type:"))
        self.delay_label.setText(_translate("ScopeControlWindow", "Delay:"))
        self.postsample_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.threshold_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.direction_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.presample_hover.setText(_translate("ScopeControlWindow", "  ?"))
        self.trigger_reset_pushButton.setText(_translate("ScopeControlWindow", "Reset to default"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScopeControlWindow = QtWidgets.QMainWindow()
    ui = Ui_ScopeControlWindow()
    ui.setupUi(ScopeControlWindow)
    ScopeControlWindow.show()
    sys.exit(app.exec_())
