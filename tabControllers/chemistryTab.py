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
chemistryTab.py

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

class chemTab:
    def __init__(self, mainWin, parent=None):
        self.mainWin = mainWin
        
        #Select flow cell
        self.chemFC0 = self.mainWin.chemFC0
        self.chemFC1 = self.mainWin.chemFC1

        #Sbl tab
        self.sblHybPB = self.mainWin.sblHybPB
        self.sblHybPortSB = self.mainWin.sblHybPortSB
        self.sblHybValveSB = self.mainWin.sblHybValveSB
        self.sblLigPB = self.mainWin.sblLigPB
        self.sblLigPortSB = self.mainWin.sblLigPortSB
        self.sblLigValveSB = self.mainWin.sblLigValveSB
        self.sblStripPB = self.mainWin.sblStripPB
        self.sblStripPortSB = self.mainWin.sblStripPortSB
        self.sblStripValveSB = self.mainWin.sblStripValveSB

        #Sbs tab
        self.sbsHybPB = self.mainWin.sbsHybPB
        self.sbsHybPortSB = self.mainWin.sbsHybPortSB
        self.sbsHybValveSB = self.mainWin.sbsHybValveSB
        self.sbsDebPB = self.mainWin.sbsDebPB
        self.sbsDebPortSB = self.mainWin.sbsDebPortSB
        self.sbsDebValveSB = self.mainWin.sbsDebValveSB
        self.sbsIncPB = self.mainWin.sbsIncPB
        self.sbsIncPortSB = self.mainWin.sbsIncPortSB
        self.sbsIncValveSB = self.mainWin.sbsIncValveSB
        
        #Chemistry Cycle
        self.cycleDebPortSB = self.mainWin.cycleDebPortSB
        self.cycleDebValveSB = self.mainWin.cycleDebValveSB
        self.cycleIncPortSB = self.mainWin.cycleIncPortSB
        self.cycleIncValveSB = self.mainWin.cycleIncValveSB
        self.cyclePB = self.mainWin.cyclePB

        #Manual Reaction
        self.manReactPB = self.mainWin.manReactPB
        #Manual Biochemistry Cycle
        self.manBCStartPB = self.mainWin.manBCStartPB
        self.manBCPrimeBlockPB = self.mainWin.manBCPrimeBlockPB
        self.manBCPrimeFlowcellPB = self.mainWin.manBCPrimeFlowcellPB
        self.manBCInitSyringePB = self.mainWin.manBCInitSyringePB
        
        self.establishConnections()

    def establishConnections(self):

        self.sblHybPB.pressed.connect(self.sblHybRun)
        self.sblLigPB.pressed.connect(self.sblLigRun)
        self.sblStripPB.pressed.connect(self.sblStripRun)
        self.sbsHybPB.pressed.connect(self.sbsHybRun)
        self.sbsDebPB.pressed.connect(self.sbsDebRun)
        self.sbsIncPB.pressed.connect(self.sbsIncRun)
        self.cyclePB.pressed.connect(self.cycleRun)

        #Manual Reaction
        self.manReactPB.pressed.connect(self.manReact)
        #Manual Biochemistry Cycle
        self.manBCStartPB.pressed.connect(self.manBCStart)
        self.manBCPrimeBlockPB.pressed.connect(self.manBCPrimeBlock)
        self.manBCPrimeFlowcellPB.pressed.connect(self.manBCPrimeFlowcell)
        self.manBCInitSyringePB.pressed.connect(self.manBCInitSyringe)

    def manReact(self):
        print 'test pass'

    def manBCStart(self):
        print 'test pass'

    def manBCPrimeBlock(self):
        print 'test pass'

    def manBCPrimeFlowcell(self):
        print 'test pass'

    def manBCInitSyringe(self):
        print 'test pass'

    def cycleRun(self):
        print 'test pass'

    def sblHybRun(self):
        print 'test pass'

    def sblLigRun(self):
        print 'test pass'

    def sblStripRun(self):
        print 'test pass'

    def sbsHybRun(self):
        print 'test pass'

    def sbsDebRun(self):
        print 'test pass'

    def sbsIncRun(self):
        print 'test pass'


