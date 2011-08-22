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
sequenceTab.py

Created by Roger Conturie on 2011-07-25.
"""
import os
import sys
import json

#add root directory to path
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, _root_dir)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from seqTabFunctions import SeqTabFunctions
from graphicItems.primer import Primer
from graphicItems.seqFunc import SeqFunc
from graphicItems.sequence import Sequence
from ui.warningDialog import WarningDialog

class seqTab:
    def __init__(self, mainWin, parent=None):

        self.mainWin = mainWin
        self.functions = SeqTabFunctions(self)


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
        self.seqList = []
        self.polonatorCycleListVector = self.mainWin.polonatorCycleListVector

        self.seqScene = QGraphicsScene()
        self.seqScene.setSceneRect(QRectF(0, 0, self.sequenceGraphicsView.width(), self.sequenceGraphicsView.height()))

        self.sequenceGraphicsView.setDragMode(QGraphicsView.RubberBandDrag)
        self.sequenceGraphicsView.setScene(self.seqScene)
        self.sequenceGraphicsView.mouseReleaseEvent = self.graphicsViewMouseRelease
        self.sequenceGraphicsView.setRubberBandSelectionMode(Qt.ContainsItemBoundingRect)

        #load most recent template
        f = file(_root_dir + "/.config/.polGV.cfg", 'r')
        path = json.load(f)
        if path != 'None':
            try:    
                self.functions.addSequence(path)
            except:
                f = file(_root_dir + "/.config/.polGV.cfg", 'w')
                json.dump('None', f)

        #initialize table widget
        self.functions.updateCycleList(True)

        self.establishConnections()


    def establishConnections(self):
        self.seqStartPB.pressed.connect(self.start)
        self.cycleEntryValidatePB.pressed.connect(self.validate)
        self.clearSelectionPB.pressed.connect(self.clear)
        self.applyPB.pressed.connect(self.applySeq)
        self.applyRepeatPB.pressed.connect(self.applyRepeatSeq)
        #prevent user from starting invalid cycle
        self.cycleTable.cellChanged.connect(self.disableStart)

    def disableStart(self):
        self.seqStartPB.setEnabled(False)

    def start(self):
        print 'start'
        touchFlag = "0"
        for i in range(self.cycleTable.rowCount()):
            if self.cycleTable.item(i,0).text() != '':
                print self.cycleTable.item(i,0).text() + \
                        self.cycleTable.item(i,1).text() + \
                        self.cycleTable.item(i,2).text()

        cmd = 'python ' + _root_dir + '/pol_API/G.007_fluidics/src/polonator_main.py ' + touchFlag
#        os.system(cmd)
        print cmd
  
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
        self.seqStartPB.setEnabled(True)
        self.functions.executeValidation()

    def clear(self):
        self.warningDialog = WarningDialog('Are you sure that you want to'+\
                                        ' clear the cycle list?', self.okClear)
        self.warningDialog.show()

    def okClear(self):
        self.cycleTable.clearContents()
        while len(self.baseClassL) != 0:
            #Make sure to remove all repeats, base select turns bases purple
            self.baseClassL[0].fill = self.baseClassL[0].red
            self.baseClassL[0].baseSelect()
        self.functions.updateCycleList(True)
        self.applyPB.setEnabled(False)
        self.applyRepeatPB.setEnabled(False)
        self.warningDialog = None

    def applySeq(self):
        self.functions.updateCycleList(True)
        self.applyPB.setEnabled(False)
        self.applyRepeatPB.setEnabled(True)

    def applyRepeatSeq(self):
        baseClassLPreserve = []
        for base in self.baseClassL:
            if baseClassLPreserve.count(base) == 0:
                baseClassLPreserve.append(base)
        for base in baseClassLPreserve:
            self.baseClassL.append(base)
        self.functions.updateCycleList(True)

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


