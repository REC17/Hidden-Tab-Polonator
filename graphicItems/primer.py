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
primer.py

Created by Roger Conturie on 2011-07-25.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base import Base
from seqFunc import SeqFunc

class Primer(QGraphicsItem):
    def __init__(self, mainwin, sequence, position, primerLetter, parent = None):
        super(Primer, self).__init__()
        self.fill = QColor(170, 54, 20)
        self.seq = sequence
        self.rect = QRectF(0, 0, 12*len(self.seq), 45)
        self.setAcceptHoverEvents(True)
     #   self.setFlags(QGraphicsItem.ItemIsMovable)
        
        self.primerLetter = primerLetter

        count = 0
        for nucleotide in self.seq:
            base = Base(nucleotide, None)
            base.setParentItem(self)
            base.setPos(count, 0)
            count = count + 12
           
        self.isHybed = False
        self.hybBases = []

        self.plusLabel = QGraphicsSimpleTextItem(QString('Plus'))
        self.minusLabel = QGraphicsSimpleTextItem(QString('Minus'))
        self.primerLabel = QGraphicsSimpleTextItem(QString(self.primerLetter))

        self.plusLabel.setParentItem(self)       
        self.minusLabel.setParentItem(self)
        self.primerLabel.setParentItem(self)

        self.minusLabel.setPos(0, 15)
        self.plusLabel.setPos(12*len(self.seq)- self.plusLabel.boundingRect().width(), 15)
        self.primerLabel.setPos(12*len(self.seq)/2, 28)


        """
        self.seqDenAll = QGraphicsSimpleTextItem(QString('Denature'))
        self.seqHybAll = QGraphicsSimpleTextItem(QString('Hybridize'))
        self.seqHybAll.setParentItem(self)
        self.seqHybAll.setPos(12*len(self.seq)/2 - 12*len('Hybridize')/2, 28)
        """



        """
        psSeq = self.seq[len(self.seq)-6:]
        self.primeSite = SeqFunc(QColor(130, 190, 50), psSeq, [12*len(self.seq)-12*len(psSeq), 15], self)
        self.primeSite.setParentItem(self)
        """

        self.setPos(position[0], position[1])


 #   def hoverMoveEvent(self, event):
  #      """docstring for mouseMoveEvent"""
   #     self.setPos(self.mapToScene(event.pos().x(), event.pos().y()))

        

    def hoverMoveEvent(self, event):
        pass
        """
        if event.pos().y() > 30:
            self.setCursor(Qt.PointingHandCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        """

    def mousePressEvent(self, event):
        pass        
        """
        if event.pos().y() > 30:
            if self.isHybed == False:
                self.hybridize()
                self.isHybed = True
            else:
                self.denature()
                self.isHybed = False
        """
    def hybridize(self):
        count = 0
        for nucleotide in self.seq:
            base = Base(self.complement(nucleotide))
            self.hybBases.append(base)
            base.setParentItem(self)
            base.setPos(count, -15)
            count = count + 12

        self.scene().removeItem(self.seqHybAll)
        self.seqDenAll.setParentItem(self)
        self.seqDenAll.setPos(12*len(self.seq)/2 - 12*len('Denature')/2, 28)

    def denature(self):
        for nucleotide in self.hybBases:
            self.scene().removeItem(nucleotide)
        self.hybBases = []
        
        self.scene().removeItem(self.seqDenAll)
        self.seqHybAll.setParentItem(self)
        self.seqHybAll.setPos(12*len(self.seq)/2 - 12*len('Denature')/2, 28)

    def complement(self, nuc):
        if nuc == 'A':
            return 'T'
        if nuc == 'T':
            return 'A'
        if nuc == 'G':
            return 'C'
        if nuc == 'C':
            return 'G'


    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(self.fill))
       # painter.setPen(QPen(self.stroke))
      #  painter.drawEllipse(self.rect)
        painter.drawRect(self.rect)
