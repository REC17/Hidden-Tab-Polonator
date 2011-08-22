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
seqTabFunctions.py

Created by Roger Conturie on 2011-08-22.
"""
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

class SeqTabFunctions():
    def __init__(self, seqTab, parent = None):

        self.seqTab = seqTab
        pass

    def addSequence(self, path):

        for item in self.seqTab.seqScene.items():
            self.seqTab.seqScene.removeItem(item)

        #update config file
        f = file(_root_dir + "/.config/.polGV.cfg", 'w')
        json.dump(str(path), f)  

        xpos = 5

        f = file(path, 'r')
        seqList = json.load(f)[1]
        #seqListRel is for enabling relationships between sequences and primers
        seqListRel = seqList

        primerLabelIndex = 65
        for i in range(len(seqList)):
            seq = seqList[i]
            if seq[0] == 'P':
                setattr(self.seqTab, 'seq%s'%str(xpos), Primer(self.seqTab, seq[1:], [xpos, 30], chr(primerLabelIndex)))
                self.seqTab.seqScene.addItem(getattr(self.seqTab, 'seq%s'%str(xpos)))
                seqListRel[i] = getattr(self.seqTab, 'seq%s'%str(xpos))         
                primerLabelIndex = primerLabelIndex + 1
            xpos = xpos + 12*len(seq[1:])
        
        #Debug for garbage collection issue
        del seqList
        f = file(path, 'r')
        seqList = json.load(f)[1]

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
                setattr(self.seqTab, 'seq%s'%str(xpos), Sequence(self.seqTab, seq[1:], [xpos, 30], minusPrimer, plusPrimer))
                self.seqTab.seqScene.addItem(getattr(self.seqTab, 'seq%s'%str(xpos)))
            xpos = xpos + 12*len(seq[1:])
        self.seqTab.seqScene.setSceneRect(QRectF(0, 0, xpos, self.seqTab.sequenceGraphicsView.height()))

        self.seqTab.seqList = seqList

    def updateCycleList(self, flag):
        #Flag = True : Generate list using highlighted base list
        #Flag = False: Generate list using existing cycle list vector

        self.seqTab.seqStartPB.setEnabled(False)
        # Initialize Table and List Vector
        if flag:
            self.seqTab.polonatorCycleListVector = []
            # Create Cycle Names (tuple object)
            for base in self.seqTab.baseClassL:
                if base.parentItem().pos().x() > base.primer.pos().x():
                    cycle = base.primer.primerLetter, 'P', base.position
                else:
                    cycle = base.primer.primerLetter, 'M', base.position

                self.seqTab.polonatorCycleListVector.append(cycle)

        self.seqTab.cycleTable.clearContents()

        # Manage Table Size
        if self.seqTab.cycleTable.rowCount() < len(self.seqTab.polonatorCycleListVector):
            for i in range(len(self.seqTab.polonatorCycleListVector)-self.seqTab.cycleTable.rowCount()):            
                self.seqTab.cycleTable.insertRow(10+i)
        elif self.seqTab.cycleTable.rowCount() > 10 and self.seqTab.cycleTable.rowCount() > len(self.seqTab.baseClassL):
            for i in range(self.seqTab.cycleTable.rowCount() - len(self.seqTab.polonatorCycleListVector)):
                if self.seqTab.cycleTable.rowCount() > 10:
                    self.seqTab.cycleTable.removeRow(self.seqTab.cycleTable.rowCount() - (i+1))
                
        # Replace table widget items so they don't return as none
        for row in range(10):
            self.seqTab.cycleTable.setItem(row, 0, QTableWidgetItem(QString('')))
            self.seqTab.cycleTable.setItem(row, 1, QTableWidgetItem(QString('')))
            self.seqTab.cycleTable.setItem(row, 2, QTableWidgetItem(QString('')))



        # Populate Table
        row = 0
        for cycle in self.seqTab.polonatorCycleListVector:
            setattr(self.seqTab, cycle[0] + cycle[1] + cycle[2] + 'Pr', QTableWidgetItem(QString(cycle[0]), QTableWidgetItem.Type))
            setattr(self.seqTab, cycle[0] + cycle[1] + cycle[2] + 'D', QTableWidgetItem(QString(cycle[1]), QTableWidgetItem.Type))
            setattr(self.seqTab, cycle[0] + cycle[1] + cycle[2] + 'Po', QTableWidgetItem(QString(cycle[2]), QTableWidgetItem.Type))

            self.seqTab.cycleTable.setItem(row, 0, getattr(self.seqTab, cycle[0] + cycle[1] + cycle[2] + 'Pr'))
            self.seqTab.cycleTable.setItem(row, 1, getattr(self.seqTab, cycle[0] + cycle[1] + cycle[2] + 'D'))
            self.seqTab.cycleTable.setItem(row, 2, getattr(self.seqTab, cycle[0] + cycle[1] + cycle[2] + 'Po'))

            row = row + 1
       
        # Auto Scroll To Last Item Feature
        #try:
        #    self.seqTab.cycleTable.scrollToItem(getattr(self.seqTab, cycle + 'Pr'))
        #except:
        #    pass
