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
sequenceMenuController.py

Created by Roger Conturie on 2011-08-18.
"""
import math
import sys
import json
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#add root directory to path
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, _root_dir)

from dialogControllers.tempDialogController import TDController
from ui.warningDialog import WarningDialog

class SeqMenuController(QWidget):
    def __init__(self, mainWin, parent=None):
        super(SeqMenuController, self).__init__(parent)
        self.mainWin = mainWin
        self.actionSave_Cycle_List = self.mainWin.actionSave_Cycle_List
        self.actionSave_Cycle_List_As = self.mainWin.actionSave_Cycle_List_As
        self.actionLoad_Cycle_List = self.mainWin.actionLoad_Cycle_List
        self.actionDesign_New_Layout = self.mainWin.actionDesign_New_Layout
        self.actionLoad_Layout = self.mainWin.actionLoad_Layout

        self.actionMap_Cycle_List_to_Template = self.mainWin.actionMap_Cycle_List_to_Template
        self.actionClear_Layout = self.mainWin.actionClear_Layout

        self.openPath = None
        self.seqTab = self.mainWin.seqTab

        self.establishConnections()

    def establishConnections(self):
        self.actionSave_Cycle_List.triggered.connect(self.saveCycleList)
        self.actionSave_Cycle_List_As.triggered.connect(self.saveCycleListAs)
        self.actionLoad_Cycle_List.triggered.connect(self.loadCycleList)
        self.actionMap_Cycle_List_to_Template.triggered.connect(self.mapCtoT)        
        self.actionDesign_New_Layout.triggered.connect(self.designNewLayout)
        self.actionLoad_Layout.triggered.connect(self.loadLayout)
        self.actionClear_Layout.triggered.connect(self.clearLayout)

    def mapCtoT(self):
        print 'map!'

    def clearLayout(self):
        for item in self.seqTab.seqScene.items():
            self.seqTab.seqScene.removeItem(item)

    def saveCycleList(self):
        if self.openPath == None:
            self.saveCycleListAs()
        else:
            self.saveFile(self.openPath)

    def saveCycleListAs(self):
        self.openPath = QFileDialog.getSaveFileName(self, \
                            "Save File As", _root_dir + '/cycleLists/' , \
                            QString("Schemes (*.cfg)"))
        try:
            self.saveFile(self.openPath)
        except:
            pass

    def saveFile(self, path):
        f = file(path, 'w')
        json.dump((self.seqTab.polonatorCycleListVector, self.seqTab.seqList), f)
        self.savedFlag = True

    def loadCycleList(self):
        self.openPath = QFileDialog.getOpenFileName(self, \
                            "Save File As", _root_dir + '/cycleLists/' , \
                            QString("Schemes (*.cfg)"))
        try:
            f = file(self.openPath, 'r')
            data = json.load(f)
            self.seqTab.polonatorCycleListVector = data[0]      
            self.seqTab.seqList = data[1]
        except:
            print 'cycle list load fail'

        self.seqTab.functions.addSequence(self.openPath)
      #  try:
     #       
      #  except:
      #      print 'sequence layout fail'

        self.seqTab.updateCycleList(False)

    def designNewLayout(self):
        designWindow = TDController()
        designWindow.show()

    def loadLayout(self):
        self.openPath = QFileDialog.getOpenFileName(self, \
                            "Open File", _root_dir + '/templateSchemes/' , \
                            QString("Schemes (*.cfg)"))
        try:
            self.seqTab.functions.addSequence(self.openPath)
        except:
            pass

