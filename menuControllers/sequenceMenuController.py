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

class SeqMenuController(QWidget):
    def __init__(self, mainWin, parent=None):
        super(SeqMenuController, self).__init__(parent)
        self.mainWin = mainWin
        self.actionSave_Cycle_List = self.mainWin.actionSave_Cycle_List
        self.actionSave_Cycle_List_As = self.mainWin.actionSave_Cycle_List_As
        self.actionLoad_Cycle_List = self.mainWin.actionLoad_Cycle_List
        self.actionDesign_New_Layout = self.mainWin.actionDesign_New_Layout
        self.actionLoad_Layout = self.mainWin.actionLoad_Layout
        
        self.seqTab = self.mainWin.seqTab

        self.establishConnections()

    def establishConnections(self):
        self.actionSave_Cycle_List.triggered.connect(self.saveCycleList)
        self.actionSave_Cycle_List_As.triggered.connect(self.saveCycleListAs)
        self.actionLoad_Cycle_List.triggered.connect(self.loadCycleList)
        self.actionDesign_New_Layout.triggered.connect(self.designNewLayout)
        self.actionLoad_Layout.triggered.connect(self.loadLayout)

    def saveCycleList(self):
        print 'test pass'

    def saveCycleListAs(self):
        print 'test pass'

    def loadCycleList(self):
        print 'test pass'

    def designNewLayout(self):
        designWindow = TDController()
        designWindow.show()

    def loadLayout(self):
        self.openPath = QFileDialog.getOpenFileName(self, \
                            "Open File", _root_dir + '/templateSchemes/' , \
                            QString("Schemes (*.cfg)"))
        try:
            self.seqTab.addSequence(self.openPath)
        except:
            pass













