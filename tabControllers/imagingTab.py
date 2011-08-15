import os
import sys
import json
from imgWidgetSetup import widgetSetup

#add root directory to path
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, _root_dir)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class imgTab:
    def __init__(self, mainWin, parent=None):

        self.mainWin = mainWin
        self.ws = widgetSetup(self.mainWin)

        #Cycle Scan
        self.csCopySnapSetPB = self.mainWin.csCopySnapSetPB
        self.csDarkfieldScanPB = self.mainWin.csDarkfieldScanPB
        self.csCycleScanPB = self.mainWin.csCycleScanPB
        
        #Still Snap
        self.stillSnapPB = self.mainWin.stillSnapPB
        self.stillViewPB = self.mainWin.stillViewPB
        
        #Live Snap
        self.liveStartPB = self.mainWin.liveStartPB
        self.liveCloseShutterPB = self.mainWin.liveCloseShutterPB
        self.liveSetFocusPB = self.mainWin.liveSetFocusPB

        self.lightSwitch = self.mainWin.lightSwitch
        self.darkfieldSwitch = self.mainWin.darkfieldSwitch

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

        self.establishConnections()

    def establishConnections(self):
        self.csCopySnapSetPB.pressed.connect(self.csCopySnapSet)
        self.csDarkfieldScanPB.pressed.connect(self.csDarkfieldScan)
        self.csCycleScanPB.pressed.connect(self.csCycleScan)
        self.stillSnapPB.pressed.connect(self.stillSnap)
        self.stillViewPB.pressed.connect(self.stillView)
        self.liveStartPB.pressed.connect(self.liveStart)
        self.liveCloseShutterPB.pressed.connect(self.liveCloseShutter)
        self.liveSetFocusPB.pressed.connect(self.liveSetFocus)
        
        #Switch Connections
        self.lightSwitch.sliderPressed.connect(self.lightSwitchClicked)
        self.darkfieldSwitch.sliderPressed.connect(self.darkfieldSwitchClicked)

    def lightSwitchClicked(self):
        self.lightSwitch.setSliderPosition(1 - self.lightSwitch.value())

    def darkfieldSwitchClicked(self):
        self.darkfieldSwitch.setSliderPosition(1 - self.darkfieldSwitch.value())

    def csCopySnapSet(self):
        print 'test pass'
self.updateCycleScanParams()


    def csDarkfieldScan(self):
	    self.ButtonPermission("All", False)
	
	    if self.acqSingle.isChecked():
	        cyclename = "WL1"
	        flowcell = "0"
	
	    elif self.acqDual.isChecked():
	        cyclename = "WL2"
	        flowcell = "2"
	        
	    else:
	        cyclename = "WL2"
	        flowcell = "3"
	 
	    cmd = "python /home/polonator/G.007/G.007_acquisition/src/test-img.py " + cyclename + " " + flowcell 
	
	    self.process_start(cmd,  ['pass'], "self.process_pass()")    
	    

    def csCycleScan(self):
	    fcnum = "0";
	
	    self.ButtonPermission("All", False)    
	    if not self.acqFC0.isChecked():
	        fcnum = "1"
	
	    cmd = "python /home/polonator/G.007/G.007_acquisition/src/test-img.py " \
			+ str(self.acqCycleName.displayText()) + " " \
			+ fcnum + " "+ str(self.acqCycleIntFAM.value()) \
			+ " " + str(self.acqCycleGainFAM.value()) \
			+ " " + str(self.acqCycleIntCy5.value()) \
			+ " " + str(self.acqCycleGainCy5.value()) \
			+ " " + str(self.acqCycleIntCy3.value()) + " " \
			+ str(self.acqCycleGainCy3.value()) + " " \
			+ str(self.acqCycleGainTxRed.value()) \
			+ " " + str(self.acqCycleIntTxR.value())
	
	    self.process_start(cmd,  ['pass'], "self.process_pass()") 
	    

    def stillSnap(self):
        print 'test pass'
        commandArgs = "" + str(self.utilsSnapFilterList.currentItem().text()) \
        + " " + str((float(self.utilsSnapExp.value())) / 1000) + " " + str(int(self.utilsSnapGain.value()))
        cmd = acqbase_dir + "/PolonatorUtils snap " + commandArgs 
        self.process_start(cmd,  ['pass'], "self.process_pass()")

#COLOR
	    commandArgs = "" + str(float(int(self.utilsSnapExp.value())) / 1000) \
	+ " " + str(int(self.utilsColorFAMgain.value())) \
	+ " " + str(int(self.utilsColorCy5gain.value())) \
	+ " " + str(float(int(self.utilsColorCy3gain.value()))) \
	+ " " + str(float(int(self.utilsColorTxRgain.value())))
	    cmd = acqbase_dir + "/PolonatorUtils colorsnap " + commandArgs 
	    self.process_start(cmd,  ['pass'], "self.process_pass()")               
	      
    def stillView(self):
	    filename1 = "none"
	    filename2 = "none"
	    filename3 = "none"
	    red = str(self.utilsColorRed.currentText())
	    green = str(self.utilsColorGreen.currentText())
	    blue = str(self.utilsColorBlue.currentText())
	    if not red == "none" or not green == "none" or not blue == "none":
	        pass
	    if not red == "none":
	        filename1 = "/home/polonator/G.007/G.007_acquisition/colorsnap-" + red + ".raw"
	    if not green == "none":
	        filename2 = "/home/polonator/G.007/G.007_acquisition/colorsnap-" + green + ".raw"
	    if not blue == "none":
	        filename3 = "/home/polonator/G.007/G.007_acquisition/colorsnap-" + blue + ".raw"
	    cmd = "/home/polonator/G.007/G.007_acquisition/run_display_color_raw.sh /opt/MATLAB/MATLAB_Component_Runtime/v77/ " \
	+ filename1 +" " + filename2 +" " + filename3 
	    self.process_start(cmd,  ['pass'], "self.process_pass()")  

        
    def liveStart(self):
	    # disableAllAcqUtilsCameraButtons();
	    commandArgs = ""+ str(float(int(self.utilsLiveExp.value())) / 1000) \
	+ " " + str(int(self.utilsLiveGain.value()))+" "+ str(self.utilsLiveFilterList.currentItem().text())
	    cmd = acqbase_dir+"/PolonatorUtils live_new " + commandArgs 
	    self.utilFocusBar.setEnabled(True);
	    self.utilSetFocus.setEnabled(True);  
	    self.process_start(cmd,  ['pass'], "self.process_pass()")          


    def liveCloseShutter(self):
	    #TODO add your handling code here:
	    cmd = acqbase_dir + "/PolonatorUtils darkfield-off "
	
	    self.process_start(cmd, ['pass'], "self.shutLightButton2()")    
	
	
	#         cmd1 = 'python initialize_processor.py'
	#         self.process_start(cmd1, self.polonator_textarea, ['pass'], "self.shutLightButton2()")    
	
	def shutLightButton2(self):
	    cmd2 = "/home/polonator/G.007/G.007_acquisition/PolonatorUtils shutter_close "
	    self.process_start(cmd2, ['pass'], "self.process_oa()") 


    def liveSetFocus(self):
	    cmd = acqbase_dir + "/PolonatorUtils setfocus " + str(self.utilFocusBar.value())    
	# utilFocusLabel.setText(Integer.toString(utilFocusBar.getValue()));
	    self.process_start(cmd,  ['pass'], "self.process_pass()")              


