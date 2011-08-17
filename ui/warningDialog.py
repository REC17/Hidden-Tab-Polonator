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
warningDialog.py

created by Roger Conturie on 2011-08-16
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class WarningDialog(QDialog):
    def __init__(self, message, function, parent = None):
        super(WarningDialog, self).__init__(parent)
        self.function = function
        self.okButton = QPushButton("&Ok")
        self.cancelButton = QPushButton("&Cancel")
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.okButton)
        buttonLayout.addWidget(self.cancelButton)
        self.layout = QGridLayout() 
        self.layout.addWidget(QLabel(message), 0, 0)
        self.setLayout(self.layout)
        self.layout.addLayout(buttonLayout, 1,0)
        self.setWindowTitle("Alert!")
        self.connect(self.cancelButton, SIGNAL("clicked()"), \
                                    self, SLOT("reject()"))
        self.connect(self.okButton, SIGNAL("clicked()"), self.ok)
    
    def ok(self):
        if self.function != None:
            self.function()
        self.close()
