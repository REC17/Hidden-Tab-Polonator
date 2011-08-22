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
base.py

Created by Roger Conturie on 2011-07-25.
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Base(QGraphicsItem):
    def __init__(self, nucleotide, primer, parent = None):
        super(Base, self).__init__()

        self.setFlag(QGraphicsItem.ItemIsSelectable)
     #   self.setFlag(QGraphicsItem.ItemIsMovable)

        self.primer = primer
        self.selected = False

        self.purple = QColor(100, 104, 250)
        self.red = QColor(200, 54, 50)
        self.fill = self.purple

        self.nuc = nucleotide
        self.rect = QRectF(0, 0, 12, 15)

        self.position = 0


        self.seqGraphic = QGraphicsSimpleTextItem(QString(self.nuc))
        self.seqGraphic.setParentItem(self)
        self.seqGraphic.setPos(1, -3)
        
    def determinePosition(self):
        if self.pos().x()/12 < self.parentItem().boundingRect().width()/24:
            self.position = str(int(1 + self.pos().x()/12))
        else:
            self.position = str(int(20 - self.pos().x()/12))       

    def mousePressEvent(self, event):
        self.baseSelect()

    def baseSelect(self):
     #   if self.parentItem().__class__.__name__ != 'Primer':\
        self.determinePosition()
        if self.primer != None:
            if self.fill == self.purple:
                self.fill = self.red
                self.parentItem().baseClassL.append(self)
                self.parentItem().mainWin.applyPB.setEnabled(True)
#                self.parentItem().mainWin.applyRepeatPB.setEnabled(True)
            elif self.fill == self.red:
                self.fill = self.purple
                self.parentItem().baseClassL.remove(self)
                self.parentItem().mainWin.applyPB.setEnabled(True)
 #               self.parentItem().mainWin.applyRepeatPB.setEnabled(True)
            self.update()


        """    
        if self.fill == self.purple:
            self.fill = self.red
        elif self.fill == self.red:
            self.fill = self.purple
        self.update()
        """
    def mouseReleaseEvent(self, event):

        pass
        """
        if self.selected == False:
            if self.fill == self.purple:
                self.fill = self.red
            elif self.fill == self.red:
                self.fill = self.purple
        self.selected = not(self.selected)
        self.update()
        """
    def itemChange(self, change, value):
      #  print self.isSelected()


        if change == QGraphicsItem.ItemSelectedHasChanged and self.primer != None:#self.parentItem().__class__.__name__ != 'Primer':# and self.isSelected() == False:
            sortBaseL = []
            if self.pos().x()/12 < self.parentItem().boundingRect().width()/24:
                self.position = str(int(1 + self.pos().x()/12))
            else:
                self.position = str(int(20 - self.pos().x()/12))

            if self.selected == False:
         #   if self.scene().views()[0].held == True:
                if self.fill == self.purple:
                    self.fill = self.red
                    self.parentItem().sortBaseL.append(self)
                elif self.fill == self.red:
                    self.fill = self.purple
                    self.parentItem().baseClassL.remove(self)
            self.selected = not(self.selected)

        self.update()

     #   if self.scene() != None:
     #       print self.scene().views()[0].held
    
        return QGraphicsItem.itemChange(self, change, value)

    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(self.fill))
       # painter.setPen(QPen(self.stroke))
        painter.drawRect(self.rect)
       # painter.drawEllipse(QRectF(-6,-6,12,12))



