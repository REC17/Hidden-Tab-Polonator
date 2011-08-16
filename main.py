from PyQt4.QtCore import *
from PyQt4.QtGui import *

import math
import json
import os

from ui import ui_htPol
from tabControllers.sequenceTab import seqTab
from tabControllers.maestroTab import maestroTab
from tabControllers.chemistryTab import chemTab
from tabControllers.imagingTab import imgTab

class Polonator(QMainWindow, ui_htPol.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Polonator, self).__init__(parent)
        self.setupUi(self)
        #columnWidth = self.cycleTable.width()/4
        #for i in range(4):
        #    self.cycleTable.setColumnWidth(i, columnWidth - 11)

        self.polonatorCycleListVector = []
        self.currentDir = os.getcwd()
        try:
            os.mkdir(self.currentDir+"/.config")
            f = file(self.currentDir+"/.config/.polGV.cfg", 'w')
            seqList = ['SNNNNNNNNNNNNNNNNNNNN', 'PATCATGCCATTCATG', 'SNNNNNNNNNNNNNNNNNNNN', 'PATCATGCCATTCATG','SNNNNNNNNNNNNNNNNNNNN', 'PATCATGCCATTCATG', 'SNNNNNNNNNNNNNNNNNNNN' ]
            json.dump(seqList, f)
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
