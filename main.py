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
main.py

Created by Roger Conturie on 2011-07-25.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import math
import json
import os

from styles import styleSheet
from ui import ui_htPol
from tabControllers.sequenceTab import seqTab
from tabControllers.maestroTab import maestroTab
from tabControllers.chemistryTab import chemTab
from tabControllers.imagingTab import imgTab
from menuControllers.menuBehavior import MenuBehavior
from menuControllers.toolMenuController import ToolMenuController

class Polonator(QMainWindow, ui_htPol.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Polonator, self).__init__(parent)

        self.setupUi(self)
  #      self.setStyleSheet('QMainWindow{background-color: #1a191f }')
 #       self.menubar.setStyleSheet('QMenuBar{background-color: #35352f}')

        columnWidth = self.cycleTable.width()/3
        for i in range(3):
            self.cycleTable.setColumnWidth(i, columnWidth - 15)

        self.polonatorCycleListVector = []

        self.currentDir = os.getcwd()
        try:
            os.mkdir(self.currentDir+"/.config")
            f = file(self.currentDir+"/.config/.polGV.cfg", 'w')
            json.dump('None', f)
        except:
            pass

        self.setContextMenuPolicy(Qt.CustomContextMenu)
      #  self.sequenceGraphicsView.mousePressEvent = self.graphicsViewMousePress
      #  self.sequenceGraphicsView.setRubberBandSelectionMode(Qt.IntersectsItemShape)
        self.customContextMenuRequested.connect(\
            self.graphicsViewContextMenu)
        """
        self.helixWidget = GLWidget(self.frame)
      #  print self.frame.frameRect().width()
      #  self.helixWidget.resizeGL(self.frame.frameRect().width(), self.frame.frameRect().height())
        self.helixWidget.resize(self.frame.frameRect().width(), self.frame.frameRect().height())
        """
      #  self.tabWidget_4.removeTab(1)
        self.actionPro_Mode.triggered.connect(self.proMode)
        self.seqTab = seqTab(self)

        self.maestroTab = maestroTab(self)
        self.chemTab = chemTab(self)
        self.imgTab = imgTab(self)
#    def graphicsViewMousePress(self, event):    
#        self.sequenceGraphicsView.held = True    
        self.menuBehavior = MenuBehavior(self)
        self.toolMenuController = ToolMenuController(self)
        self.abortButton.pressed.connect(self.abort)

    def abort(self):
        print 'abort'

    def proMode(self):
        self.tabWidget_4.insertTab(1, self.tab_10, QString('Maintenence'))
        #self.tab_10.setVisible(False)

    def graphicsViewContextMenu(self, event):
        #This script builds a context menu from scratch
        cm = QMenu()
        self.actionInsert = QAction(cm)
        self.actionRemove = QAction(cm)
        # self.actionInsert.triggered.connect(self.quickHelp)
        self.actionInsert.setText("Insert")
        self.actionRemove.setText("Remove")
        cm.addAction(self.actionInsert)
        cm.addAction(self.actionRemove)
        cm.exec_(self.mapToGlobal(event))

if __name__ == "__main__":
    import sys
    # add comments as to what this specifically does
    app = QApplication(sys.argv)
    form = Polonator()
    form.show()
    app.exec_()
