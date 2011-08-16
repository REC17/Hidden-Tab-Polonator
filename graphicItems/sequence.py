from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base import Base

class Sequence(QGraphicsItem):
    def __init__(self, mainWin, sequence, position, minusPrimer, plusPrimer, parent = None):
        super(Sequence, self).__init__()

        self.mainWin = mainWin
        self.baseClassL = self.mainWin.baseClassL
        self.sortBaseL = self.mainWin.sortBaseL


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

