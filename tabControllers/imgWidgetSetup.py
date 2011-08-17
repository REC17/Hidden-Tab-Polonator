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
imgWidgetSetup.py

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

class widgetSetup:
    def __init__(self, mainWin, parent=None):
        self.mainWin = mainWin

        #Cycle Scan Tab
        self.csFAMGainDial = self.mainWin.csFAMGainDial
        self.csCy3GainDial = self.mainWin.csCy3GainDial
        self.csCy5GainDial = self.mainWin.csCy5GainDial
        self.csTxRGainDial = self.mainWin.csTxRGainDial

        self.csFAMIntDial = self.mainWin.csFAMIntDial
        self.csCy3IntDial = self.mainWin.csCy3IntDial
        self.csCy5IntDial = self.mainWin.csCy5IntDial
        self.csTxRIntDial = self.mainWin.csTxRIntDial

        self.csFAMGainSB = self.mainWin.csFAMGainSB
        self.csCy3GainSB = self.mainWin.csCy3GainSB
        self.csCy5GainSB = self.mainWin.csCy5GainSB
        self.csTxRGainSB = self.mainWin.csTxRGainSB

        self.csFAMIntSB = self.mainWin.csFAMIntSB
        self.csCy3IntSB = self.mainWin.csCy3IntSB
        self.csCy5IntSB = self.mainWin.csCy5IntSB
        self.csTxRIntSB = self.mainWin.csTxRIntSB

        #Still Tab
        self.stillFAMGainDial = self.mainWin.stillFAMGainDial
        self.stillCy3GainDial = self.mainWin.stillCy3GainDial
        self.stillCy5GainDial = self.mainWin.stillCy5GainDial
        self.stillTxRGainDial = self.mainWin.stillTxRGainDial

        self.stillFAMGainSB = self.mainWin.stillFAMGainSB
        self.stillCy3GainSB = self.mainWin.stillCy3GainSB
        self.stillCy5GainSB = self.mainWin.stillCy5GainSB
        self.stillTxRGainSB = self.mainWin.stillTxRGainSB

        self.stillIntDial = self.mainWin.stillIntDial
        self.stillGainDial = self.mainWin.stillGainDial
        self.stillIntSB = self.mainWin.stillIntSB
        self.stillEMGainSB = self.mainWin.stillEMGainSB

        #Live Tab
        self.liveEMGainDial = self.mainWin.liveEMGainDial
        self.liveIntDial = self.mainWin.liveIntDial
        self.liveIntSB = self.mainWin.liveIntSB
        self.liveEMGainSB = self.mainWin.liveEMGainSB

        self.liveIntSB.setValue(self.liveIntDial.value())
        self.liveEMGainSB.setValue(self.liveEMGainDial.value())
        self.establishConnections()

    def establishConnections(self):
        #Live Tab Dial and Spin Box Connections
        self.liveEMGainDial.valueChanged.connect(self.liveEMGainChangeD)
        self.liveIntDial.valueChanged.connect(self.liveIntChangeD)

        self.liveEMGainSB.valueChanged.connect(self.liveEMGainChangeSB)
        self.liveIntSB.valueChanged.connect(self.liveIntChangeSB)

        #Still Tab Dial and Spin Box Connections
        self.stillIntDial.valueChanged.connect(self.stillIntChangeD)
        self.stillGainDial.valueChanged.connect(self.stillGainChangeD)
        self.stillFAMGainDial.valueChanged.connect(self.stillFAMGainChangeD)
        self.stillCy3GainDial.valueChanged.connect(self.stillCy3GainChangeD)
        self.stillCy5GainDial.valueChanged.connect(self.stillCy5GainChangeD)
        self.stillTxRGainDial.valueChanged.connect(self.stillTxRGainChangeD)

        self.stillIntSB.valueChanged.connect(self.stillIntChangeSB)
        self.stillEMGainSB.valueChanged.connect(self.stillEMGainChangeSB)
        self.stillFAMGainSB.valueChanged.connect(self.stillFAMGainChangeSB)
        self.stillCy3GainSB.valueChanged.connect(self.stillCy3GainChangeSB)
        self.stillCy5GainSB.valueChanged.connect(self.stillCy5GainChangeSB)
        self.stillTxRGainSB.valueChanged.connect(self.stillTxRGainChangeSB)

        #Cycle Scan Tab Dial and Spin Box Connections

        self.csFAMGainDial.valueChanged.connect(self.csFAMGainChangeD)
        self.csCy3GainDial.valueChanged.connect(self.csCy3GainChangeD)
        self.csCy5GainDial.valueChanged.connect(self.csCy5GainChangeD)
        self.csTxRGainDial.valueChanged.connect(self.csTxRGainChangeD)

        self.csFAMGainSB.valueChanged.connect(self.csFAMGainChangeSB)
        self.csCy3GainSB.valueChanged.connect(self.csCy3GainChangeSB)
        self.csCy5GainSB.valueChanged.connect(self.csCy5GainChangeSB)
        self.csTxRGainSB.valueChanged.connect(self.csTxRGainChangeSB)
        
        self.csFAMIntDial.valueChanged.connect(self.csFAMIntChangeD)
        self.csCy3IntDial.valueChanged.connect(self.csCy3IntChangeD)
        self.csCy5IntDial.valueChanged.connect(self.csCy5IntChangeD)
        self.csTxRIntDial.valueChanged.connect(self.csTxRIntChangeD)

        self.csFAMIntSB.valueChanged.connect(self.csFAMIntChangeSB)
        self.csCy3IntSB.valueChanged.connect(self.csCy3IntChangeSB)
        self.csCy5IntSB.valueChanged.connect(self.csCy5IntChangeSB)
        self.csTxRIntSB.valueChanged.connect(self.csTxRIntChangeSB)


    def csFAMGainChangeD(self):
        self.csFAMGainSB.setValue(self.csFAMGainDial.value())
    def csCy3GainChangeD(self):
        self.csCy3GainSB.setValue(self.csCy3GainDial.value())
    def csCy5GainChangeD(self):
        self.csCy5GainSB.setValue(self.csCy5GainDial.value())
    def csTxRGainChangeD(self):
        self.csTxRGainSB.setValue(self.csTxRGainDial.value())
    def csFAMGainChangeSB(self):
        self.csFAMGainDial.setValue(self.csFAMGainSB.value())
    def csCy3GainChangeSB(self):
        self.csCy3GainDial.setValue(self.csCy3GainSB.value())
    def csCy5GainChangeSB(self):
        self.csCy5GainDial.setValue(self.csCy5GainSB.value())
    def csTxRGainChangeSB(self):
        self.csTxRGainDial.setValue(self.csTxRGainSB.value())
    def csFAMIntChangeD(self):
        self.csFAMIntSB.setValue(self.csFAMIntDial.value())
    def csCy3IntChangeD(self):
        self.csCy3IntSB.setValue(self.csCy3IntDial.value())
    def csCy5IntChangeD(self):
        self.csCy5IntSB.setValue(self.csCy5IntDial.value())
    def csTxRIntChangeD(self):
        self.csTxRIntSB.setValue(self.csTxRIntDial.value())
    def csFAMIntChangeSB(self):
        self.csFAMIntDial.setValue(self.csFAMIntSB.value())
    def csCy3IntChangeSB(self):
        self.csCy3IntDial.setValue(self.csCy3IntSB.value())
    def csCy5IntChangeSB(self):
        self.csCy5IntDial.setValue(self.csCy5IntSB.value())
    def csTxRIntChangeSB(self):
        self.csTxRIntDial.setValue(self.csTxRIntSB.value())
    def stillIntChangeD(self):
        self.stillIntSB.setValue(self.stillIntDial.value())
    def stillGainChangeD(self):
        self.stillEMGainSB.setValue(self.stillGainDial.value())
    def stillFAMGainChangeD(self):
        self.stillFAMGainSB.setValue(self.stillFAMGainDial.value())
    def stillCy3GainChangeD(self):
        self.stillCy3GainSB.setValue(self.stillCy3GainDial.value())
    def stillCy5GainChangeD(self):
        self.stillCy5GainSB.setValue(self.stillCy5GainDial.value())
    def stillTxRGainChangeD(self):
        self.stillTxRGainSB.setValue(self.stillTxRGainDial.value())
    def stillIntChangeSB(self):
        self.stillIntDial.setValue(self.stillIntSB.value())
    def stillEMGainChangeSB(self):
        self.stillGainDial.setValue(self.stillEMGainSB.value())
    def stillFAMGainChangeSB(self):
        self.stillFAMGainDial.setValue(self.stillFAMGainSB.value())
    def stillCy3GainChangeSB(self):
        self.stillCy3GainDial.setValue(self.stillCy3GainSB.value())
    def stillCy5GainChangeSB(self):
        self.stillCy5GainDial.setValue(self.stillCy5GainSB.value())
    def stillTxRGainChangeSB(self):
        self.stillTxRGainDial.setValue(self.stillTxRGainSB.value())
    def liveEMGainChangeD(self):
        self.liveEMGainSB.setValue(self.liveEMGainDial.value())
    def liveIntChangeD(self):
        self.liveIntSB.setValue(self.liveIntDial.value())
    def liveEMGainChangeSB(self):
        self.liveEMGainDial.setValue(self.liveEMGainSB.value())
    def liveIntChangeSB(self):
        self.liveIntDial.setValue(self.liveIntSB.value())

