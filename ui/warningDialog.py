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
        print "oking"
        if self.function != None:
            self.function()
        self.close()
