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
sequence.py

Created by Roger Conturie on 2011-07-25.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base import Base

class Sequence(QGraphicsItem):
    def __init__(self, seqTab, sequence, position, minusPrimer, plusPrimer, parent = None):
        super(Sequence, self).__init__()


        self.seqTab = seqTab
        self.baseClassL = self.seqTab.baseClassL
        self.sortBaseL = self.seqTab.sortBaseL

        print 'Id from Sequence item: ' + str(id(self.baseClassL))


        self.fill = QColor(100, 204, 150)
        self.seq = sequence
        self.rect = QRectF(0, 0, 12*len(self.seq), 30)
    #    self.setFlags(QGraphicsItem.ItemIsMovable)

        self.minusPrimer = minusPrimer
        self.plusPrimer = plusPrimer



        count = 0
        for nucleotide in self.seq:
            if count >= (len(self.seq))/2:
                primer = self.minusPrimer
            else:
                primer = self.plusPrimer
            base = Base(nucleotide, primer)
            base.setParentItem(self)
            base.setPos(count*12, 0)
            count = count + 1
            

        self.setPos(position[0], position[1])


    def mouseMoveEvent(self, event):
        """docstring for mouseMoveEvent"""
        self.setPos(self.mapToScene(event.pos().x(), event.pos().y()))
        """
        if self.minusPrimer != None:
            print self.minusPrimer.primerLetter
        if self.plusPrimer != None:        
            print self.plusPrimer.primerLetter
        """
    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(self.fill))
       # painter.setPen(QPen(self.stroke))
      #  painter.drawEllipse(self.rect)
        painter.drawRect(self.rect)

