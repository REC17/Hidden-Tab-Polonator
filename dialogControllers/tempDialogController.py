# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php

"""
tempDialogController.py

Created by Roger Conturie on 2011-08-17.
"""

import os
import sys
import json

#add root directory to path
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, _root_dir)

from ui.warningDialog import WarningDialog
from ui import ui_tempDesign
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class typeCB(QComboBox):
    def __init__(self, row, controller, parent = None):
        super(typeCB, self).__init__()
        self.row = row
        self.controller = controller
        self.savedFlag = True
        self.insertItem(1, QString('Sequence'))
        self.insertItem(2, QString('Primer Site'))
        self.currentIndexChanged.connect(self.indexChangeEvent)

    def indexChangeEvent(self):
        #Table is grandparent of combobox
        table = self.parent().parent()
        print self.row
        print table.rowCount()
        table.item(self.row, 1).setText(QString(''))
        self.controller.primerLabelUpdate()
        self.controller.savedFlag = False

class TDController(QMainWindow, ui_tempDesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(TDController, self).__init__(parent)
        self.setupUi(self)
        self.openPath = None
        self.warningDialog = None
        self.tempDesignTable.setColumnWidth(2, 290)
        self.establishConnections()

        self.addNewSequence('NNNNNNNNNNNNNNNNNNNN', 'S')
        self.savedFlag = True
        self.editPosCB.setCurrentIndex(self.editPosCB.currentIndex() + 1)

    def establishConnections(self):
        self.addSeqPB.pressed.connect(self.addSeq)
        self.rmSeqPB.pressed.connect(self.rmSeq)
        self.newTempPB.pressed.connect(self.newTemp)
        self.loadTempPB.pressed.connect(self.loadTemp)
        self.saveTempPB.pressed.connect(self.saveTemp)
        self.saveTempAsPB.pressed.connect(self.saveTempAs)

        self.tempDesignTable.cellChanged.connect(self.cellChangeEvent)

    def cellChangeEvent(self, row, column):
        self.savedFlag = False
 
    def primerLabelUpdate(self):
        index = 65
        for row in range(self.tempDesignTable.rowCount()):
            if index >= 65 + 26:
                self.tempDesignTable.cellWidget(row, 0).setCurrentIndex(0)
            if self.tempDesignTable.cellWidget(row, 0).currentIndex() == 1:
                self.tempDesignTable.item(row, 1).setText(chr(index))
                index = index + 1
        self.savedFlag = False

    def addSeq(self):
        self.addNewSequence('NNNNNNNNNNNNNNNNNNNN', 'S')



    def addNewSequence(self, sequence, seqType):
        row = self.editPosCB.currentIndex() + 1

        self.tempDesignTable.insertRow(row)
        self.editPosCB.addItem(QString(str(self.tempDesignTable.rowCount())))
        self.editPosCB.setCurrentIndex(self.editPosCB.currentIndex() + 1)

        setattr(self, str(row)+'1', QTableWidgetItem(QString(''), QTableWidgetItem.Type))
        setattr(self, str(row)+'2', QTableWidgetItem(QString(sequence), QTableWidgetItem.Type))
        getattr(self, str(row)+'1').setFlags(Qt.NoItemFlags)
        self.tempDesignTable.setItem(row, 1, getattr(self, str(row)+'1'))
        self.tempDesignTable.setItem(row, 2, getattr(self, str(row)+'2'))

        self.tempDesignTable.setCellWidget(row , 0, typeCB(row, self))

        #Reassign Class Names to reflect rearrangement
        
        if row + 1 < self.tempDesignTable.rowCount():
            for missRow in range(self.tempDesignTable.rowCount() - row):
                newRow = self.tempDesignTable.rowCount() - missRow - 1
                setattr(self, str(newRow) + '1', getattr(self, str(newRow - 1)+'1'))
                setattr(self, str(newRow) +'2', getattr(self, str(newRow - 1)+'2'))
                self.tempDesignTable.cellWidget(newRow, 0).row = newRow
#                self.tempDesignTable.setCellWidget(newRow , 0, typeCB(newRow, self))
        



        if seqType == 'P':
            self.tempDesignTable.cellWidget(row, 0).setCurrentIndex(1)
        self.savedFlag = False

    def rmSeq(self):
        row = self.editPosCB.currentIndex()
        if self.tempDesignTable.rowCount() > 1:

            self.tempDesignTable.removeRow(row)
            self.editPosCB.removeItem(self.editPosCB.count()-1)

        #Reassign Class Names to reflect rearrangement
        if row + 1 < self.tempDesignTable.rowCount():
            for missRow in range(self.tempDesignTable.rowCount() - row):
                newRow = self.tempDesignTable.rowCount() - missRow - 1
                setattr(self, str(newRow) + '1', getattr(self, str(newRow - 1)+'1'))
                setattr(self, str(newRow) +'2', getattr(self, str(newRow - 1)+'2'))
                self.tempDesignTable.cellWidget(newRow, 0).row = newRow

        self.primerLabelUpdate()
        self.savedFlag = False
        '''
        if self.tempDesignTable.rowCount() > 1:
            self.tempDesignTable.setRowCount(self.tempDesignTable.rowCount()-1)

        '''

#self.rmPosCB




























    def newTemp(self):
        if self.savedFlag == False:
            self.warningDialog = WarningDialog('Any unsaved data will be lost.'\
                                +'Do you wish to proceed?', self.newTempApproved)
            self.warningDialog.show()
        else:
            self.newTempApproved()

    def newTempApproved(self):
        self.tempDesignTable.setRowCount(0)
        self.addSeq()
        self.savedFlag = True

    def loadTemp(self):
        if self.savedFlag == False:
            self.warningDialog = WarningDialog('Any unsaved data will be lost.'\
                                +'Do you wish to proceed?', self.loadApproved)
            self.warningDialog.show()
        else:
            self.loadApproved()

    def loadApproved(self):
        self.openPath = QFileDialog.getOpenFileName(self, \
                            "Open File", _root_dir + '/templateSchemes/' , \
                            QString("Schemes (*.cfg)"))
        self.tempDesignTable.setRowCount(0)
        f = file(self.openPath, 'r')
        seqList = json.load(f)
        for row in range(len(seqList)):
            self.addNewSequence(seqList[row][1:], seqList[row][0])
        self.primerLabelUpdate()
        self.savedFlag = True

    def saveTemp(self):
        if self.openPath == None:
            self.saveTempAs()
        else:
            self.saveFile(self.openPath)

    def saveTempAs(self):
        self.openPath = QFileDialog.getSaveFileName(self, \
                            "Save File As", _root_dir + '/templateSchemes/' , \
                            QString("Schemes (*.cfg)"))
        try:
            self.saveFile(self.openPath)
        except:
            pass

    def saveFile(self, path):
        seqList = []
        for row in range(self.tempDesignTable.rowCount()):
            seq = ''
            if self.tempDesignTable.cellWidget(row, 0).currentIndex() == 1:
                seq = 'P'
            else:
                seq = 'S'
            seq = seq + str(self.tempDesignTable.item(row, 2).text())
            seqList.append(seq)
        f = file(self.openPath, 'w')
        json.dump(seqList, f)
        self.savedFlag = True
    
if __name__ == "__main__":
    import sys
    # add comments as to what this specifically does
    app = QApplication(sys.argv)
    form = TDController()
    form.show()
    app.exec_()
