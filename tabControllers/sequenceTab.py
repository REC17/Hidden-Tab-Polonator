import os
import sys
import json

#add root directory to path
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, _root_dir)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from graphicItems.primer import Primer
from graphicItems.seqFunc import SeqFunc
from graphicItems.sequence import Sequence
from ui.warningDialog import WarningDialog

class seqTab:
    def __init__(self, mainWin, parent=None):

        self.mainWin = mainWin

        self.abortButton = self.mainWin.abortButton
        self.seqStartPB = self.mainWin.seqStartPB
        self.seqStartPB.setEnabled(False)
        self.includeHomeAxisRB = self.mainWin.includeHomeAxisRB
        self.cycleEntryValidatePB = self.mainWin.cycleEntryValidatePB
        self.clearSelectionPB = self.mainWin.clearSelectionPB
        self.applyPB = self.mainWin.applyPB
        self.applyRepeatPB = self.mainWin.applyRepeatPB

        self.applyPB.setEnabled(False)
        self.applyRepeatPB.setEnabled(False)

        self.warningDialog = None

        self.touchFlagCB = self.mainWin.touchFlagCB
        self.cycleTable = self.mainWin.cycleTable
        self.sequenceGraphicsView = self.mainWin.sequenceGraphicsView
        
        self.baseClassL = []
        self.sortBaseL = []
        self.sortedCyclesL = []
        self.sortCycleD = {}
        self.polonatorCycleListVector = self.mainWin.polonatorCycleListVector

        self.seqScene = QGraphicsScene()
        self.seqScene.setSceneRect(QRectF(0, 0, self.sequenceGraphicsView.width(), self.sequenceGraphicsView.height()))

        self.sequenceGraphicsView.setDragMode(QGraphicsView.RubberBandDrag)
        self.sequenceGraphicsView.setScene(self.seqScene)
        self.sequenceGraphicsView.mouseReleaseEvent = self.graphicsViewMouseRelease
        self.sequenceGraphicsView.setRubberBandSelectionMode(Qt.ContainsItemBoundingRect)
        self.addSequence()

        #initialize table widget
        self.updateCycleList()

        self.establishConnections()


    def establishConnections(self):
        self.abortButton.pressed.connect(self.abort)
        self.seqStartPB.pressed.connect(self.start)
        self.cycleEntryValidatePB.pressed.connect(self.validate)
        self.clearSelectionPB.pressed.connect(self.clear)
        self.applyPB.pressed.connect(self.applySeq)
        self.applyRepeatPB.pressed.connect(self.applyRepeatSeq)

    def abort(self):
        print 'abort'

    def start(self):
        print 'start'
        touchFlag = "0"
        '''
        try:
            with open("/home/polonator/G.007/G.007_fluidics/src/cycle_list", "w") as outfile:
                for i in range(len(entry)):
                    outfile.write(str(self.polonatorCycleListVector[i][0]+self.polonatorCycleListVector[i][1]+self.polonatorCycleListVector[i][2]))
                    outfile.write('\n')
                if self.touchFlagCB.currentIndex() == 1:
                    touchFlag = "1"

            cmd = "python /home/polonator/G.007/G.007_fluidics/src/polonator_main.py "+ touchFlag 
            #os.system(cmd)

        except IOError: #as (errno, strerror):
            print "Error writing to cycle_list file, I/O error" #: ({0}): {1}".format(errno, strerror)        
        #  self.process_start(cmd, ['pass'], "self.process_pass()")   
        '''
    def validate(self):
        breakAll = False
        isEmpty = True
        validateList = []
        self.seqStartPB.setEnabled(True)
        for i in range(self.cycleTable.rowCount()):
            if self.cycleTable.item(i, 0).text() == '' and \
                    self.cycleTable.item(i, 1).text() == '' and \
                    self.cycleTable.item(i, 2).text() == '':
                pass
            else:
                isEmpty = False
                for j in range(3):
                    if self.cycleTable.item(i,j).text() == '':
                        self.seqStartPB.setEnabled(False)
                        self.warningDialog = WarningDialog(\
                            'Cell (%(i)s, %(j)s) is empty' %{'i':str(i+1),\
                             'j':str(j+1)}, None)
                        self.warningDialog.cancelButton.hide()             
                        self.warningDialog.show()
                        self.seqStartPB.setEnabled(False)
                        breakAll = True                        
                        break

                if breakAll == True:
                    break

                if len(self.cycleTable.item(i, 0).text()) > 1:
                    self.seqStartPB.setEnabled(False)
                    self.warningDialog = WarningDialog(\
                        'Expected a single letter between "A" and "Z" in cell\
                        (%(i)s, 1) (not case sensitive)' %{'i':str(i+1)}, None)
                    self.warningDialog.cancelButton.hide()             
                    self.warningDialog.show()
                    self.seqStartPB.setEnabled(False)
                    breakAll = True                        
                    break

                if not (ord('A') <= ord(str(self.cycleTable.item(i, 0).text()))\
                        <= ord('Z') or\
                        ord('a') <= ord(str(self.cycleTable.item(i, 0).text()))\
                        <= ord('z')):
                    self.seqStartPB.setEnabled(False)
                    self.warningDialog = WarningDialog(\
                        'Expected a single letter between "A" and "Z" in cell\
                        (%(i)s, 2) (not case sensitive)' %{'i':str(i+1)}, None)
                    self.warningDialog.cancelButton.hide()             
                    self.warningDialog.show()
                    self.seqStartPB.setEnabled(False)
                    breakAll = True                        
                    break
    
                if str(self.cycleTable.item(i, 1).text()) != 'P' and\
                        str(self.cycleTable.item(i, 1).text()) != 'p' and\
                        str(self.cycleTable.item(i, 1).text()) != 'M' and\
                        str(self.cycleTable.item(i, 1).text()) != 'm':
                    self.seqStartPB.setEnabled(False)
                    self.warningDialog = WarningDialog(\
                        'Expected either a "P" or "M" in cell (%(i)s, 2)\
                        (not case sensitive)'%{'i':str(i+1)}, None)
                    self.warningDialog.cancelButton.hide()             
                    self.warningDialog.show()
                    self.seqStartPB.setEnabled(False)
                    breakAll = True                        
                    break

                try:
                    int(str(self.cycleTable.item(i, 2).text()))
                except:
                    self.seqStartPB.setEnabled(False)
                    self.warningDialog = WarningDialog(\
                        'Expected an integer in cell (%(i)s, 3)'\
                                    %{'i':str(i+1)}, None)
                    self.warningDialog.cancelButton.hide()             
                    self.warningDialog.show()
                    self.seqStartPB.setEnabled(False)
                    breakAll = True                        
                    break



        if isEmpty == True:
            self.warningDialog = WarningDialog(\
            'Cycle list is empty!', None)
            self.warningDialog.cancelButton.hide()             
            self.warningDialog.show()
            self.seqStartPB.setEnabled(False)

            #if valid == True:
            #    self.seqStartPB.setEnabled(True)
        #print self.polonatorCycleListVector
        # validate each line; keep track if we need to change something
        """
        if len(self.polonatorCycleListVector) == 0:
            changed = True
        else:
            for cycle in self.polonatorCycleListVector:
                if len(cycle) > 4:
                    cycle = cycle[:4]
                    changed = True
                if len(cycle) >= 3:
                    validateList.append(cycle)
                else:
                    changed = True
        self.polonatorCycleListVector = []
        for cycle in validateList:
            self.polonatorCycleListVector.append(cycle) 
        if changed:
            pass
        else:
            
        """
    def clear(self):
        self.warningDialog = WarningDialog('Are you sure that you want to clear\
                                                the cycle list?', self.okClear)
        #self.warningDialog.setMessage()
        self.warningDialog.show()

    def okClear(self):
        print 'clear'
        self.cycleTable.clearContents()
        while len(self.baseClassL) != 0:
            #Make sure to remove all repeats, base select turns bases purple
            self.baseClassL[0].fill = self.baseClassL[0].red
            self.baseClassL[0].baseSelect()
        self.updateCycleList()
        self.applyPB.setEnabled(False)
        self.applyRepeatPB.setEnabled(False)
        self.warningDialog = None

    def applySeq(self):
        self.updateCycleList()
        self.applyPB.setEnabled(False)
        self.applyRepeatPB.setEnabled(True)

    def applyRepeatSeq(self):
        baseClassLPreserve = []
        for base in self.baseClassL:
            if baseClassLPreserve.count(base) == 0:
                baseClassLPreserve.append(base)
        for base in baseClassLPreserve:
            self.baseClassL.append(base)
        self.updateCycleList()
        
    def graphicsViewMouseRelease(self, event):
        #Create cycle name from base
        if len(self.sortBaseL) != 0:
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
                pos = int(cycle[2:])
                if sortL.count(pos) == 0:
                    sortL.append(pos)
            sortL.sort()
            sortL.reverse()
            for num in sortL:
                for cycle in plusL:
                    pos = int(cycle[2:])
                    if pos == num:
                        self.sortedCyclesL.append(cycle)
            
            #Sort Minus
            sortL = []
            for cycle in minusL:
                pos = int(cycle[2:])
                if sortL.count(pos) == 0:
                    sortL.append(pos)
            sortL.sort()
            sortL.reverse()
            for num in sortL:
                for cycle in minusL:
                    pos = int(cycle[2:])
                    if pos == num:
                        self.sortedCyclesL.append(cycle)

            for cycle in self.sortedCyclesL:
                self.baseClassL.append(self.sortCycleD[cycle])

            #Reinitialize data structures
            self.sortedCyclesL = []
            self.sortCycleD = {}

            #Empty list without jeapordizing data structure location
            while len(self.sortBaseL) != 0:
                self.sortBaseL.pop()
            self.applyPB.setEnabled(True)

            #update cycle list


    def addSequence(self):
        
        xpos = 5
        f = file(_root_dir+"/.config/.polGV.cfg", 'r')
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
        f = file(_root_dir+"/.config/.polGV.cfg", 'r')
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

    def updateCycleList(self):
        self.seqStartPB.setEnabled(False)
        # Initialize Table and List Vector
        self.polonatorCycleListVector = []
        self.cycleTable.clearContents()

        # Manage Table Size
        if self.cycleTable.rowCount() < len(self.baseClassL):
            for i in range(len(self.baseClassL)-self.cycleTable.rowCount()):            
                self.cycleTable.insertRow(10+i)
        elif self.cycleTable.rowCount() > 10 and self.cycleTable.rowCount() > len(self.baseClassL):
            for i in range(self.cycleTable.rowCount() - len(self.baseClassL)):
                if self.cycleTable.rowCount() > 10:
                    self.cycleTable.removeRow(self.cycleTable.rowCount() - (i+1))
                
        # Replace table widget items so they don't return as none
        for row in range(10):
            self.cycleTable.setItem(row, 0, QTableWidgetItem(QString('')))
            self.cycleTable.setItem(row, 1, QTableWidgetItem(QString('')))
            self.cycleTable.setItem(row, 2, QTableWidgetItem(QString('')))

        # Create Cycle Names (tuple object)
        for base in self.baseClassL:
            if base.parentItem().pos().x() > base.primer.pos().x():
                cycle = base.primer.primerLetter, 'P', base.position
            else:
                cycle = base.primer.primerLetter, 'M', base.position

            self.polonatorCycleListVector.append(cycle)

        # Populate Table
        row = 0
        for cycle in self.polonatorCycleListVector:
            setattr(self, cycle[0] + cycle[1] + cycle[2] + 'Pr', QTableWidgetItem(QString(cycle[0]), QTableWidgetItem.Type))
            setattr(self, cycle[0] + cycle[1] + cycle[2] + 'D', QTableWidgetItem(QString(cycle[1]), QTableWidgetItem.Type))
            setattr(self, cycle[0] + cycle[1] + cycle[2] + 'Po', QTableWidgetItem(QString(cycle[2]), QTableWidgetItem.Type))

            self.cycleTable.setItem(row, 0, getattr(self, cycle[0] + cycle[1] + cycle[2] + 'Pr'))
            self.cycleTable.setItem(row, 1, getattr(self, cycle[0] + cycle[1] + cycle[2] + 'D'))
            self.cycleTable.setItem(row, 2, getattr(self, cycle[0] + cycle[1] + cycle[2] + 'Po'))

            row = row + 1
        
        # Auto Scroll To Last Item Feature
        #try:
        #    self.cycleTable.scrollToItem(getattr(self, cycle + 'Pr'))
        #except:
        #    pass


