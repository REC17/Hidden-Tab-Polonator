# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hiddenTabPolonator.ui'
#
# Created: Tue Aug  2 13:33:41 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(668, 916)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget_4 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_4.setGeometry(QtCore.QRect(9, 10, 641, 771))
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.layoutWidget = QtGui.QWidget(self.tab_9)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 20, 613, 261))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_15.setMargin(0)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.EnterCyclesHerelabel_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EnterCyclesHerelabel_2.setFont(font)
        self.EnterCyclesHerelabel_2.setLineWidth(1)
        self.EnterCyclesHerelabel_2.setMidLineWidth(1)
        self.EnterCyclesHerelabel_2.setObjectName(_fromUtf8("EnterCyclesHerelabel_2"))
        self.gridLayout_6.addWidget(self.EnterCyclesHerelabel_2, 0, 0, 1, 1)
        self.Executinglabel_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Executinglabel_2.setFont(font)
        self.Executinglabel_2.setObjectName(_fromUtf8("Executinglabel_2"))
        self.gridLayout_6.addWidget(self.Executinglabel_2, 0, 2, 1, 1)
        self.polonatorStart = QtGui.QPushButton(self.layoutWidget)
        self.polonatorStart.setEnabled(True)
        self.polonatorStart.setObjectName(_fromUtf8("polonatorStart"))
        self.gridLayout_6.addWidget(self.polonatorStart, 1, 1, 1, 1)
        self.polonatorCycleList = QtGui.QTextEdit(self.layoutWidget)
        self.polonatorCycleList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.polonatorCycleList.setObjectName(_fromUtf8("polonatorCycleList"))
        self.gridLayout_6.addWidget(self.polonatorCycleList, 1, 2, 1, 1)
        self.cycleTable = QtGui.QTableWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cycleTable.sizePolicy().hasHeightForWidth())
        self.cycleTable.setSizePolicy(sizePolicy)
        self.cycleTable.setLineWidth(1)
        self.cycleTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cycleTable.setRowCount(10)
        self.cycleTable.setColumnCount(3)
        self.cycleTable.setObjectName(_fromUtf8("cycleTable"))
        self.cycleTable.setColumnCount(3)
        self.cycleTable.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.cycleTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.cycleTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.cycleTable.setHorizontalHeaderItem(2, item)
        self.cycleTable.horizontalHeader().setDefaultSectionSize(71)
        self.cycleTable.horizontalHeader().setMinimumSectionSize(71)
        self.gridLayout_6.addWidget(self.cycleTable, 1, 0, 1, 1)
        self.verticalLayout_15.addLayout(self.gridLayout_6)
        self.polonatorCycleEntryValidate_2 = QtGui.QPushButton(self.layoutWidget)
        self.polonatorCycleEntryValidate_2.setObjectName(_fromUtf8("polonatorCycleEntryValidate_2"))
        self.verticalLayout_15.addWidget(self.polonatorCycleEntryValidate_2)
        self.frame = QtGui.QFrame(self.tab_9)
        self.frame.setGeometry(QtCore.QRect(10, 290, 611, 131))
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.sequenceGraphicsView = QtGui.QGraphicsView(self.tab_9)
        self.sequenceGraphicsView.setGeometry(QtCore.QRect(10, 430, 611, 101))
        self.sequenceGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sequenceGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sequenceGraphicsView.setObjectName(_fromUtf8("sequenceGraphicsView"))
        self.clearSelectionPB = QtGui.QPushButton(self.tab_9)
        self.clearSelectionPB.setGeometry(QtCore.QRect(10, 540, 611, 31))
        self.clearSelectionPB.setObjectName(_fromUtf8("clearSelectionPB"))
        self.touchFlagCB = QtGui.QComboBox(self.tab_9)
        self.touchFlagCB.setGeometry(QtCore.QRect(10, 580, 611, 31))
        self.touchFlagCB.setObjectName(_fromUtf8("touchFlagCB"))
        self.touchFlagCB.addItem(_fromUtf8(""))
        self.touchFlagCB.addItem(_fromUtf8(""))
        self.tabWidget_4.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.layoutWidget_3 = QtGui.QWidget(self.tab_10)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 10, 301, 66))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, -1, -1, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.stopButton_2 = QtGui.QPushButton(self.layoutWidget_3)
        self.stopButton_2.setObjectName(_fromUtf8("stopButton_2"))
        self.gridLayout_3.addWidget(self.stopButton_2, 0, 0, 1, 1)
        self.homing_axis_2 = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.homing_axis_2.setFont(font)
        self.homing_axis_2.setObjectName(_fromUtf8("homing_axis_2"))
        self.gridLayout_3.addWidget(self.homing_axis_2, 1, 0, 1, 1)
        self.frame_34 = QtGui.QFrame(self.tab_10)
        self.frame_34.setGeometry(QtCore.QRect(20, 250, 501, 261))
        self.frame_34.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_34.setObjectName(_fromUtf8("frame_34"))
        self.label_99 = QtGui.QLabel(self.frame_34)
        self.label_99.setGeometry(QtCore.QRect(40, 40, 41, 16))
        self.label_99.setObjectName(_fromUtf8("label_99"))
        self.label_100 = QtGui.QLabel(self.frame_34)
        self.label_100.setGeometry(QtCore.QRect(40, 100, 51, 21))
        self.label_100.setObjectName(_fromUtf8("label_100"))
        self.stageSwitch_4 = QtGui.QSlider(self.frame_34)
        self.stageSwitch_4.setGeometry(QtCore.QRect(50, 60, 20, 41))
        self.stageSwitch_4.setMaximum(1)
        self.stageSwitch_4.setOrientation(QtCore.Qt.Vertical)
        self.stageSwitch_4.setObjectName(_fromUtf8("stageSwitch_4"))
        self.label_107 = QtGui.QLabel(self.frame_34)
        self.label_107.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label_107.setObjectName(_fromUtf8("label_107"))
        self.layoutWidget_2 = QtGui.QWidget(self.frame_34)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 10, 383, 222))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_23.setMargin(0)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.SelectFlowcelllabel_6 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SelectFlowcelllabel_6.setFont(font)
        self.SelectFlowcelllabel_6.setObjectName(_fromUtf8("SelectFlowcelllabel_6"))
        self.horizontalLayout_17.addWidget(self.SelectFlowcelllabel_6)
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.stagealign_fc0_3 = QtGui.QRadioButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stagealign_fc0_3.setFont(font)
        self.stagealign_fc0_3.setObjectName(_fromUtf8("stagealign_fc0_3"))
        self.verticalLayout_21.addWidget(self.stagealign_fc0_3)
        self.stagealign_fc1_3 = QtGui.QRadioButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stagealign_fc1_3.setFont(font)
        self.stagealign_fc1_3.setObjectName(_fromUtf8("stagealign_fc1_3"))
        self.verticalLayout_21.addWidget(self.stagealign_fc1_3)
        self.horizontalLayout_17.addLayout(self.verticalLayout_21)
        self.verticalLayout_22.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.Selectlanelabel_3 = QtGui.QLabel(self.layoutWidget_2)
        self.Selectlanelabel_3.setObjectName(_fromUtf8("Selectlanelabel_3"))
        self.horizontalLayout_6.addWidget(self.Selectlanelabel_3)
        self.stagealign_lane_3 = QtGui.QSpinBox(self.layoutWidget_2)
        self.stagealign_lane_3.setMaximum(7)
        self.stagealign_lane_3.setObjectName(_fromUtf8("stagealign_lane_3"))
        self.horizontalLayout_6.addWidget(self.stagealign_lane_3)
        self.verticalLayout_22.addLayout(self.horizontalLayout_6)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.gridLayout_40 = QtGui.QGridLayout()
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.utilsHomeButton_5 = QtGui.QPushButton(self.layoutWidget_2)
        self.utilsHomeButton_5.setObjectName(_fromUtf8("utilsHomeButton_5"))
        self.gridLayout_40.addWidget(self.utilsHomeButton_5, 0, 0, 1, 1)
        self.stagealign_gotoposition_3 = QtGui.QPushButton(self.layoutWidget_2)
        self.stagealign_gotoposition_3.setObjectName(_fromUtf8("stagealign_gotoposition_3"))
        self.gridLayout_40.addWidget(self.stagealign_gotoposition_3, 0, 1, 1, 1)
        self.utilsStatusButton_5 = QtGui.QPushButton(self.layoutWidget_2)
        self.utilsStatusButton_5.setObjectName(_fromUtf8("utilsStatusButton_5"))
        self.gridLayout_40.addWidget(self.utilsStatusButton_5, 1, 0, 1, 1)
        self.stagealign_viewlog_3 = QtGui.QPushButton(self.layoutWidget_2)
        self.stagealign_viewlog_3.setObjectName(_fromUtf8("stagealign_viewlog_3"))
        self.gridLayout_40.addWidget(self.stagealign_viewlog_3, 1, 1, 1, 1)
        self.verticalLayout_20.addLayout(self.gridLayout_40)
        self.stagealign_dostagealign_3 = QtGui.QPushButton(self.layoutWidget_2)
        self.stagealign_dostagealign_3.setObjectName(_fromUtf8("stagealign_dostagealign_3"))
        self.verticalLayout_20.addWidget(self.stagealign_dostagealign_3)
        self.verticalLayout_23.addLayout(self.verticalLayout_20)
        self.frame_11 = QtGui.QFrame(self.tab_10)
        self.frame_11.setGeometry(QtCore.QRect(20, 120, 501, 121))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.label_97 = QtGui.QLabel(self.frame_11)
        self.label_97.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_97.setObjectName(_fromUtf8("label_97"))
        self.label_105 = QtGui.QLabel(self.frame_11)
        self.label_105.setGeometry(QtCore.QRect(40, 89, 67, 21))
        self.label_105.setObjectName(_fromUtf8("label_105"))
        self.filterSwitch_4 = QtGui.QSlider(self.frame_11)
        self.filterSwitch_4.setGeometry(QtCore.QRect(50, 49, 20, 41))
        self.filterSwitch_4.setMaximum(1)
        self.filterSwitch_4.setOrientation(QtCore.Qt.Vertical)
        self.filterSwitch_4.setObjectName(_fromUtf8("filterSwitch_4"))
        self.label_104 = QtGui.QLabel(self.frame_11)
        self.label_104.setGeometry(QtCore.QRect(40, 30, 41, 16))
        self.label_104.setObjectName(_fromUtf8("label_104"))
        self.layoutWidget_20 = QtGui.QWidget(self.frame_11)
        self.layoutWidget_20.setGeometry(QtCore.QRect(110, 20, 381, 71))
        self.layoutWidget_20.setObjectName(_fromUtf8("layoutWidget_20"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_20)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_38 = QtGui.QVBoxLayout()
        self.verticalLayout_38.setObjectName(_fromUtf8("verticalLayout_38"))
        self.label_89 = QtGui.QLabel(self.layoutWidget_20)
        self.label_89.setObjectName(_fromUtf8("label_89"))
        self.verticalLayout_38.addWidget(self.label_89)
        self.label_90 = QtGui.QLabel(self.layoutWidget_20)
        self.label_90.setObjectName(_fromUtf8("label_90"))
        self.verticalLayout_38.addWidget(self.label_90)
        self.horizontalLayout_5.addLayout(self.verticalLayout_38)
        self.gridLayout_39 = QtGui.QGridLayout()
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        self.label_91 = QtGui.QLabel(self.layoutWidget_20)
        self.label_91.setObjectName(_fromUtf8("label_91"))
        self.gridLayout_39.addWidget(self.label_91, 0, 0, 1, 1)
        self.label_92 = QtGui.QLabel(self.layoutWidget_20)
        self.label_92.setObjectName(_fromUtf8("label_92"))
        self.gridLayout_39.addWidget(self.label_92, 0, 1, 1, 1)
        self.label_93 = QtGui.QLabel(self.layoutWidget_20)
        self.label_93.setObjectName(_fromUtf8("label_93"))
        self.gridLayout_39.addWidget(self.label_93, 0, 2, 1, 1)
        self.label_94 = QtGui.QLabel(self.layoutWidget_20)
        self.label_94.setObjectName(_fromUtf8("label_94"))
        self.gridLayout_39.addWidget(self.label_94, 0, 3, 1, 1)
        self.label_95 = QtGui.QLabel(self.layoutWidget_20)
        self.label_95.setObjectName(_fromUtf8("label_95"))
        self.gridLayout_39.addWidget(self.label_95, 0, 4, 1, 1)
        self.label_96 = QtGui.QLabel(self.layoutWidget_20)
        self.label_96.setObjectName(_fromUtf8("label_96"))
        self.gridLayout_39.addWidget(self.label_96, 0, 5, 1, 1)
        self.graphicsView_13 = QtGui.QGraphicsView(self.layoutWidget_20)
        self.graphicsView_13.setObjectName(_fromUtf8("graphicsView_13"))
        self.gridLayout_39.addWidget(self.graphicsView_13, 1, 0, 1, 1)
        self.graphicsView_14 = QtGui.QGraphicsView(self.layoutWidget_20)
        self.graphicsView_14.setObjectName(_fromUtf8("graphicsView_14"))
        self.gridLayout_39.addWidget(self.graphicsView_14, 1, 1, 1, 1)
        self.graphicsView_15 = QtGui.QGraphicsView(self.layoutWidget_20)
        self.graphicsView_15.setObjectName(_fromUtf8("graphicsView_15"))
        self.gridLayout_39.addWidget(self.graphicsView_15, 1, 2, 1, 1)
        self.graphicsView_16 = QtGui.QGraphicsView(self.layoutWidget_20)
        self.graphicsView_16.setObjectName(_fromUtf8("graphicsView_16"))
        self.gridLayout_39.addWidget(self.graphicsView_16, 1, 3, 1, 1)
        self.graphicsView_17 = QtGui.QGraphicsView(self.layoutWidget_20)
        self.graphicsView_17.setObjectName(_fromUtf8("graphicsView_17"))
        self.gridLayout_39.addWidget(self.graphicsView_17, 1, 4, 1, 1)
        self.graphicsView_18 = QtGui.QGraphicsView(self.layoutWidget_20)
        self.graphicsView_18.setObjectName(_fromUtf8("graphicsView_18"))
        self.gridLayout_39.addWidget(self.graphicsView_18, 1, 5, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_39)
        self.stagealign_viewcurrent_3 = QtGui.QPushButton(self.tab_10)
        self.stagealign_viewcurrent_3.setGeometry(QtCore.QRect(200, 570, 143, 31))
        self.stagealign_viewcurrent_3.setObjectName(_fromUtf8("stagealign_viewcurrent_3"))
        self.stagealign_viewscore_3 = QtGui.QPushButton(self.tab_10)
        self.stagealign_viewscore_3.setGeometry(QtCore.QRect(250, 620, 135, 31))
        self.stagealign_viewscore_3.setObjectName(_fromUtf8("stagealign_viewscore_3"))
        self.stagealign_viewbase_3 = QtGui.QPushButton(self.tab_10)
        self.stagealign_viewbase_3.setGeometry(QtCore.QRect(260, 660, 126, 31))
        self.stagealign_viewbase_3.setObjectName(_fromUtf8("stagealign_viewbase_3"))
        self.tabWidget_4.addTab(self.tab_10, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPro_Mode = QtGui.QAction(MainWindow)
        self.actionPro_Mode.setObjectName(_fromUtf8("actionPro_Mode"))
        self.menuFile.addAction(self.actionPro_Mode)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.EnterCyclesHerelabel_2.setText(QtGui.QApplication.translate("MainWindow", "Enter Cycles Here", None, QtGui.QApplication.UnicodeUTF8))
        self.Executinglabel_2.setText(QtGui.QApplication.translate("MainWindow", "Executing", None, QtGui.QApplication.UnicodeUTF8))
        self.polonatorStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.cycleTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Primer", None, QtGui.QApplication.UnicodeUTF8))
        self.cycleTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.cycleTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Position", None, QtGui.QApplication.UnicodeUTF8))
        self.polonatorCycleEntryValidate_2.setText(QtGui.QApplication.translate("MainWindow", "Validate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearSelectionPB.setText(QtGui.QApplication.translate("MainWindow", "Clear Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.touchFlagCB.setItemText(0, QtGui.QApplication.translate("MainWindow", "Operate Polonator via Graphical Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.touchFlagCB.setItemText(1, QtGui.QApplication.translate("MainWindow", "Operate Polonator via Touch Sensor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_9), QtGui.QApplication.translate("MainWindow", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton_2.setText(QtGui.QApplication.translate("MainWindow", "Abort All Processes", None, QtGui.QApplication.UnicodeUTF8))
        self.homing_axis_2.setText(QtGui.QApplication.translate("MainWindow", "Include Homing Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_99.setText(QtGui.QApplication.translate("MainWindow", "Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_100.setText(QtGui.QApplication.translate("MainWindow", "Unlock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_107.setText(QtGui.QApplication.translate("MainWindow", "Stage", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectFlowcelllabel_6.setText(QtGui.QApplication.translate("MainWindow", "Select Flowcell", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_fc0_3.setText(QtGui.QApplication.translate("MainWindow", "Flowcell 0", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_fc1_3.setText(QtGui.QApplication.translate("MainWindow", "Flowcell 1", None, QtGui.QApplication.UnicodeUTF8))
        self.Selectlanelabel_3.setText(QtGui.QApplication.translate("MainWindow", "Select Lane", None, QtGui.QApplication.UnicodeUTF8))
        self.utilsHomeButton_5.setText(QtGui.QApplication.translate("MainWindow", "Home / reset motion axes", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_gotoposition_3.setText(QtGui.QApplication.translate("MainWindow", "Goto alignment position", None, QtGui.QApplication.UnicodeUTF8))
        self.utilsStatusButton_5.setText(QtGui.QApplication.translate("MainWindow", "Get motion status", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_viewlog_3.setText(QtGui.QApplication.translate("MainWindow", "View stage alignment log", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_dostagealign_3.setText(QtGui.QApplication.translate("MainWindow", "Perform stage alignment now", None, QtGui.QApplication.UnicodeUTF8))
        self.label_97.setText(QtGui.QApplication.translate("MainWindow", "Filter Wheel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_105.setText(QtGui.QApplication.translate("MainWindow", "Unlock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_104.setText(QtGui.QApplication.translate("MainWindow", "Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_89.setText(QtGui.QApplication.translate("MainWindow", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90.setText(QtGui.QApplication.translate("MainWindow", "Filter Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_91.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_92.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_93.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_94.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_95.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_96.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_viewcurrent_3.setText(QtGui.QApplication.translate("MainWindow", "View current image", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_viewscore_3.setText(QtGui.QApplication.translate("MainWindow", "View score matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.stagealign_viewbase_3.setText(QtGui.QApplication.translate("MainWindow", "View base image", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QtGui.QApplication.translate("MainWindow", "Maintenence", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPro_Mode.setText(QtGui.QApplication.translate("MainWindow", "Pro Mode", None, QtGui.QApplication.UnicodeUTF8))

