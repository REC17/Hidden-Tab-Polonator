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
maestroTab.py

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

class maestroTab:
    def __init__(self, mainWin, parent=None):

        self.mainWin = mainWin
        self.homePB = self.mainWin.homePB
        self.stageAlignPB = self.mainWin.stageAlignPB
        self.statusPB = self.mainWin.statusPB
        self.gotoPosPB = self.mainWin.gotoPosPB
        self.completeAScanPB = self.mainWin.completeAScanPB
        self.viewBasePB = self.mainWin.viewBasePB
        self.viewImgPB = self.mainWin.viewImgPB
        self.viewLogPB = self.mainWin.viewLogPB
        self.viewScorePB = self.mainWin.viewScorePB

        self.establishConnections()

    def establishConnections(self):
        self.homePB.pressed.connect(self.home)
        self.stageAlignPB.pressed.connect(self.stageAlign)
        self.statusPB.pressed.connect(self.status)
        self.gotoPosPB.pressed.connect(self.gotoPos)
        self.completeAScanPB.pressed.connect(self.completeAScan)
        self.viewBasePB.pressed.connect(self.viewBase)
        self.viewImgPB.pressed.connect(self.viewImg)
        self.viewLogPB.pressed.connect(self.viewLog)
        self.viewScorePB.pressed.connect(self.viewScore)

    def home(self):
        print 'test pass'
        self.ButtonPermission(self.AcquisitionUtilitiesTab, False)
        #        cmd = "/home/polonator/G.007/G.007_acquisition/PolonatorUtils hometheta"
        cmd = acqbase_dir + "/PolonatorUtils hometheta"
        self.process_start(cmd, ['pass'], "self.process_pass()")    

    def stageAlign(self):
        print 'test pass'
        if self.stagealign_fc0.isChecked():
            stagealign_fcnum = 0                                 
        if self.stagealign_fc1.isChecked():
            stagealign_fcnum = 1       
        cmd = "/home/polonator/G.007/G.007_acquisition/Polonator-stagealign " + stagealign_fcnum 
        self.process_start(cmd, ['pass'], "self.process_pass()")      


    def status(self):
        print 'test pass'
        #    cmd = "/home/polonator/G.007/G.007_acquisition/PolonatorUtils status"
        cmd = acqbase_dir+"/PolonatorUtils status"   
        self.process_start(cmd,  ['pass'], "self.process_pass()")       

    def gotoPos(self):
        print 'test pass'
        if self.stagealign_fc0.isChecked():
            stagealign_fcnum = 0
        if self.stagealign_fc1.isChecked():
            stagealign_fcnum = 1
        cmd = acqbase_dir + "/PolonatorUtils gotostagealignpos " \
        + str(stagealign_fcnum) + " " + str(int(self.stagealign_lane.value())) 
        #self.process_start(cmd, ['pass'], "self.process_pass()")

    def completeAScan(self):
        print 'test pass'

    def viewBase(self):
        print 'test pass'
        if self.stagealign_fc0.isChecked():
            stagealign_fcnum = 0                                 
        if self.stagealign_fc1.isChecked():
            stagealign_fcnum = 1    
        stagealign_dir = "/home/polonator/G.007/G.007_acquisition/stagealign/"
        cmd = "/home/polonator/G.007/G.007_acquisition/run_load_raw.sh /opt/MATLAB/MATLAB_Component_Runtime/v77/ " \
        + str(stagealign_dir) + "ALIGN_BASE" + str(stagealign_fcnum) + "_" + str(int(self.stagealign_lane.value())) + ".raw" 
        title = "STAGEALIGN-BASE-IMAGE-FLOWCELL-" + str(stagealign_fcnum) + "-LANE-" + str(int(self.stagealign_lane.value()))
        cmd = cmd + " " + title
        self.process_start(cmd,  ['pass'], "self.process_pass()")   
                    
    def viewImg(self):
        print 'test pass'
        if self.stagealign_fc0.isChecked():
            stagealign_fcnum = 0                                 
        if self.stagealign_fc1.isChecked():
            stagealign_fcnum = 1    
        stagealign_dir = "/home/polonator/G.007/G.007_acquisition/stagealign/"
        cmd = "/home/polonator/G.007/G.007_acquisition/run_load_raw.sh /opt/MATLAB/MATLAB_Component_Runtime/v77/ " \
        + str(stagealign_dir) + "stagealign-image" \
        + str(stagealign_fcnum) + "_" +str(int(self.stagealign_lane.value())) + ".raw" 
        title = "STAGEALIGN-CURRENT-IMAGE-FLOWCELL-" \
        + str(stagealign_fcnum) + "-LANE-" \
        + str(int(self.stagealign_lane.value()))
        cmd = cmd + " " + title
        self.process_start(cmd,  ['pass'], "self.process_pass()")    


    def viewLog(self):
        print 'test pass'
        if self.stagealign_fc0.isChecked():
            stagealign_fcnum = 0                                 
        if self.stagealign_fc1.isChecked():
            stagealign_fcnum = 1      
        stagealign_dir = "/home/polonator/G.007/G.007_acquisition/stagealign/"                                      
        stagealign_textwindow.setText("");
        try:
            Input = open("/home/polonator/G.007/G.007_acquisition/logs/polonator-stagealign" + stagealign_fcnum + ".offsetlog" )
            br = Input.read()
            while Input == br.readLine():
                stagealign_textwindow.append(input + "\n");
            Input.close()
        except IOError: #as (errno, strerror):
            print "Error writing to cycle_list file, I/O error" #: ({0}): {1}".format(errno, strerror)

    def viewScore(self):
        print 'test pass'

