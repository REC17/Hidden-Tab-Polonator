# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tempDesign.ui'
#
# Created: Thu Aug 18 15:37:07 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(560, 659)
        self.tempDesignTable = QtGui.QTableWidget(Dialog)
        self.tempDesignTable.setGeometry(QtCore.QRect(20, 90, 521, 371))
        self.tempDesignTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tempDesignTable.setRowCount(0)
        self.tempDesignTable.setObjectName(_fromUtf8("tempDesignTable"))
        self.tempDesignTable.setColumnCount(3)
        self.tempDesignTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tempDesignTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tempDesignTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tempDesignTable.setHorizontalHeaderItem(2, item)
        self.saveTempPB = QtGui.QPushButton(Dialog)
        self.saveTempPB.setGeometry(QtCore.QRect(20, 590, 251, 51))
        self.saveTempPB.setObjectName(_fromUtf8("saveTempPB"))
        self.addSeqPB = QtGui.QPushButton(Dialog)
        self.addSeqPB.setGeometry(QtCore.QRect(20, 10, 421, 31))
        self.addSeqPB.setObjectName(_fromUtf8("addSeqPB"))
        self.editPosCB = QtGui.QComboBox(Dialog)
        self.editPosCB.setGeometry(QtCore.QRect(450, 10, 85, 71))
        self.editPosCB.setObjectName(_fromUtf8("editPosCB"))
        self.rmSeqPB = QtGui.QPushButton(Dialog)
        self.rmSeqPB.setGeometry(QtCore.QRect(20, 50, 421, 31))
        self.rmSeqPB.setObjectName(_fromUtf8("rmSeqPB"))
        self.loadTempPB = QtGui.QPushButton(Dialog)
        self.loadTempPB.setGeometry(QtCore.QRect(20, 530, 521, 51))
        self.loadTempPB.setObjectName(_fromUtf8("loadTempPB"))
        self.saveTempAsPB = QtGui.QPushButton(Dialog)
        self.saveTempAsPB.setGeometry(QtCore.QRect(290, 590, 251, 51))
        self.saveTempAsPB.setObjectName(_fromUtf8("saveTempAsPB"))
        self.newTempPB = QtGui.QPushButton(Dialog)
        self.newTempPB.setGeometry(QtCore.QRect(20, 470, 521, 51))
        self.newTempPB.setObjectName(_fromUtf8("newTempPB"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.tempDesignTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tempDesignTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.tempDesignTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTempPB.setText(QtGui.QApplication.translate("Dialog", "Save Template", None, QtGui.QApplication.UnicodeUTF8))
        self.addSeqPB.setText(QtGui.QApplication.translate("Dialog", "Add Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.rmSeqPB.setText(QtGui.QApplication.translate("Dialog", "Remove Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.loadTempPB.setText(QtGui.QApplication.translate("Dialog", "Load Existing Template", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTempAsPB.setText(QtGui.QApplication.translate("Dialog", "Save Template As", None, QtGui.QApplication.UnicodeUTF8))
        self.newTempPB.setText(QtGui.QApplication.translate("Dialog", "New Template", None, QtGui.QApplication.UnicodeUTF8))

