from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_hiddenTabPolonator
import math
import json
import os

from graphicItems.primer import Primer
from graphicItems.seqFunc import SeqFunc
from graphicItems.sequence import Sequence



class Polonator(QMainWindow, ui_hiddenTabPolonator.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Polonator, self).__init__(parent)
        self.setupUi(self)


        self.baseClassL = []
        self.sortBaseL = []
        self.sortedCyclesL = []
        self.sortCycleD = {}


        self.seqScene = QGraphicsScene()
        self.seqScene.setSceneRect(QRectF(0, 0, self.sequenceGraphicsView.width(), self.sequenceGraphicsView.height()))
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
        self.sequenceGraphicsView.setDragMode(QGraphicsView.RubberBandDrag)
        self.sequenceGraphicsView.setScene(self.seqScene)
        self.sequenceGraphicsView.mouseReleaseEvent = self.graphicsViewMouseRelease
      #  self.sequenceGraphicsView.mousePressEvent = self.graphicsViewMousePress
        self.sequenceGraphicsView.held = True

      #  self.sequenceGraphicsView.setRubberBandSelectionMode(Qt.IntersectsItemShape)
        self.sequenceGraphicsView.setRubberBandSelectionMode(Qt.ContainsItemBoundingRect)
        self.customContextMenuRequested.connect(\
            self.graphicsViewContextMenu)

        """
        self.helixWidget = GLWidget(self.frame)
      #  print self.frame.frameRect().width()
      #  self.helixWidget.resizeGL(self.frame.frameRect().width(), self.frame.frameRect().height())
        self.helixWidget.resize(self.frame.frameRect().width(), self.frame.frameRect().height())
        """

   #     self.cycleTable.setHorizontalHeader(QHeaderView(Qt.Horizontal))
   #     self.cycleTable.setColumnWidth(1,2)

     #   self.tWI = QTableWidgetItem(QString('Hello'), QTableWidgetItem.Type)

       # self.cycleTable.setItem(1,1, self.tWI)

        self.tabWidget_4.removeTab(1)
        self.actionPro_Mode.triggered.connect(self.proMode)
        self.addSequence()        


    def graphicsViewMousePress(self, event):    
        self.sequenceGraphicsView.held = True    

    def graphicsViewMouseRelease(self, event):

        #Create cycle name from base
        sortCycleL = []
        for base in self.sortBaseL:
            cycle = base.primer.primerLetter
            if base.parentItem().pos().x() > base.primer.pos().x():
                cycle = cycle + 'P'
            else:
                cycle = cycle + 'M'
            cycle = cycle + base.position

            self.sortCycleD.update({cycle : base})
            sortCycleL.append(cycle)

        #Create a plus list and a minus list
        plusL = []
        minusL = []
        maxPos = 1

        cycleCount = 0
        for cycle in sortCycleL:
            if cycle[1] == 'P':
                plusL.append(cycle)
            if cycle[1] == 'M':
                minusL.append(cycle)

        #Sort Plus
        sortL = []
        for cycle in plusL:
            pos = int(cycle[2])
            if sortL.count(pos) == 0:
                sortL.append(pos)
        sortL.sort()
        sortL.reverse()
        for num in sortL:
            for cycle in plusL:
                pos = int(cycle[2])
                if pos == num:
                    self.sortedCyclesL.append(cycle)
        
        #Sort Minus
        sortL = []
        for cycle in minusL:
            pos = int(cycle[2])
            if sortL.count(pos) == 0:
                sortL.append(pos)
        sortL.sort()
        sortL.reverse()
        for num in sortL:
            for cycle in minusL:
                pos = int(cycle[2])
                if pos == num:
                    self.sortedCyclesL.append(cycle)


        for cycle in self.sortedCyclesL:
            self.baseClassL.append(self.sortCycleD[cycle])


        self.sortedCyclesL = []
        self.sortCycleD = {}

        #Empty list without jeapordizing data structure location
        while len(self.sortBaseL) != 0:
            self.sortBaseL.pop()
        self.updateCycleList()

    def addSequence(self):
        
        xpos = 5
        f = file(self.currentDir+"/.config/.polGV.cfg", 'r')
        seqList = json.load(f)
        #seqListRel is for enabling relationships between sequences and primers
        seqListRel = seqList


        primerLabelIndex = 65
        for i in range(len(seqList)):
            seq = seqList[i]
            if seq[0] == 'P':
                setattr(self, 'seq%s'%str(xpos), Primer(self, seq[1:], [xpos, 30], chr(primerLabelIndex)))
                self.seqScene.addItem(getattr(self, 'seq%s'%str(xpos)))
                seqListRel[i] = getattr(self, 'seq%s'%str(xpos))         
                primerLabelIndex = primerLabelIndex + 1
            xpos = xpos + 12*len(seq[1:])
        
        del seqList
        f = file(self.currentDir+"/.config/.polGV.cfg", 'r')
        seqList = json.load(f)

        xpos = 5

        for i in range(len(seqList)):
            seq = seqList[i]
            plusPrimer = None
            minusPrimer = None

            if i > 0:
                try:
                    plusPrimer = seqListRel[i-1]
                except:
                    pass
            if i < len(seqList)-1:
                try:
                    minusPrimer = seqListRel[i+1]
                except:
                    pass


            if seq[0] == 'S':
                setattr(self, 'seq%s'%str(xpos), Sequence(self, seq[1:], [xpos, 30], minusPrimer, plusPrimer))
                self.seqScene.addItem(getattr(self, 'seq%s'%str(xpos)))

            xpos = xpos + 12*len(seq[1:])


        self.seqScene.setSceneRect(QRectF(0, 0, xpos, self.sequenceGraphicsView.height()))

    
    def proMode(self):
        print "PRO!"
        self.tabWidget_4.insertTab(1, self.tab_10, QString('Maintenence'))

        #self.tab_10.setVisible(False)


    def on_polonatorStart_pressed(self):
        touchFlag = "0"

        polonatorCycleListVector = []
        entry = str(self.polonatorCycleEntry.toPlainText()).split("\n")
        CycleEntryRows = len(entry)


        for i in range(len(entry)):
            polonatorCycleListVector.append(entry[i])
        polonatorCycleListVector.pop()

        print polonatorCycleListVector

        try:
            outfile = open("/home/polonator/G.007/G.007_fluidics/src/cycle_list", "w")
            for i in range(len(entry)):
                outfile.write(str(self.polonatorCycleListVector[i]))
                outfile.write('\n')
                outfile.close()
            if self.touchFlagCB.currentIndex() == 1:
                touchFlag = "1"

            cmd = "python /home/polonator/G.007/G.007_fluidics/src/polonator_main.py "+ touchFlag 
            os.system(cmd)

        except IOError: #as (errno, strerror):
            print "Error writing to cycle_list file, I/O error" #: ({0}): {1}".format(errno, strerror)


        #  self.process_start(cmd, ['pass'], "self.process_pass()")   



    def updateCycleList(self):

        self.polonatorCycleListVector = []
        self.cycleTable.clear()

        cycle = ''
        for base in self.baseClassL:
            cycle = base.primer.primerLetter
            if base.parentItem().pos().x() > base.primer.pos().x():
                cycle = cycle + 'P'
            else:
                cycle = cycle + 'M'
            cycle = cycle + base.position

            self.polonatorCycleListVector.append(cycle)

        row = 0
        for cycle in self.polonatorCycleListVector:
            setattr(self, cycle + 'Pr', QTableWidgetItem(QString(cycle[0]), QTableWidgetItem.Type))
            setattr(self, cycle + 'D', QTableWidgetItem(QString(cycle[1]), QTableWidgetItem.Type))
            setattr(self, cycle + 'Po', QTableWidgetItem(QString(cycle[2]), QTableWidgetItem.Type))

            self.cycleTable.setItem(row, 0, getattr(self, cycle + 'Pr'))
            self.cycleTable.setItem(row, 1, getattr(self, cycle + 'D'))
            self.cycleTable.setItem(row, 2, getattr(self, cycle + 'Po'))

            row = row + 1





    def graphicsViewContextMenu(self, event):
        print 'HELLO'

            #This script builds a context menu from scratch
        cm = QMenu()
        self.actionInsert = QAction(cm)
       # self.actionInsert.triggered.connect(self.quickHelp)
        self.actionInsert.setText("Insert")
        cm.addAction(self.actionInsert)
        cm.exec_(self.mapToGlobal(event))









    """

	def processkill(self):
	    for process in self.processlist:
			if process.pid() > 0:
			    process.kill()
	    
	    self.processlist = []

    
	def process_readyRead(self):
	    self.outWin.append(str(self.process.readLine()).strip('\n'))
	
	def process_finished(self):
	    self.outWin.append(QString(self.process.readAllStandardError()))
	    self.outWin.append("++++++++++++++++++++++++++++++++++++++")
	    self.process.close()


	    for arg in self.args:
	    	exec(arg)
	    #	exec arg in globals()
	    	# function unnecessary and untested
	    if self.nextFunc == "self.process_pass()":
	    	pass
	    else:
		    eval(self.nextFunc)

	def process_start(self, cmd, args, nextFunc):

	    
	    self.process = QProcess()
	    self.process.start(cmd)
	    try:
	    	processlist.append(self.process)
	    except:
	    	print "no process to add"
	    self.outWin = self.polonatorTextArea
	    self.args = args
	    self.nextFunc = nextFunc

	    self.connect(self.process, SIGNAL("readyRead()"), self.process_readyRead)
	    self.connect(self.process, SIGNAL("finished(int)"), self.process_finished)

    """




if __name__ == "__main__":
    import sys

    # add comments as to what this specifically does
    app = QApplication(sys.argv)
    form = Polonator()
    form.show()
    app.exec_()
