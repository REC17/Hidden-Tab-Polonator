from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base import Base

class SeqFunc(QGraphicsItem):
    def __init__(self, color, seq, position, parent = None):
        super(SeqFunc, self).__init__()
        self.fill = color

        self.position = position
        self.primer = parent
        self.seq = seq

        self.rect = QRectF(0, 0, len(seq)*12, 15)
        self.setPos(self.position[0], self.position[1])
        self.setAcceptHoverEvents(True)   
        print self.seq
        self.seqDen = QGraphicsSimpleTextItem(QString('Den PS'))
        self.seqHyb = QGraphicsSimpleTextItem(QString('Hyb PS'))
        self.seqHyb.setParentItem(self)
        self.seqHyb.setPos((12*len(self.seq))/2 - 10*len('Hyb_PS')/2, -4)


    def hybridize(self):
        
        count = 0 + self.position[0]
        for nucleotide in self.seq:
            base = Base(self.primer.complement(nucleotide))
            self.primer.hybBases.append(base)
            base.setParentItem(self.primer)
            base.setPos(count, -15)
            count = count + 12

        self.primer.scene().removeItem(self.primer.seqHybAll)
        self.primer.seqDenAll.setParentItem(self.primer)
        self.primer.seqDenAll.setPos(12*len(self.primer.seq)/2 - 12*len('Denature')/2, 28)

    def denature(self):
        
        for nucleotide in self.primer.hybBases:
            self.primer.scene().removeItem(nucleotide)
        self.primer.hybBases = []
        
        self.primer.scene().removeItem(self.primer.seqDenAll)
        self.primer.seqHybAll.setParentItem(self.primer)
        self.primer.seqHybAll.setPos(12*len(self.primer.seq)/2 - 12*len('Denature')/2, 28)

    def mousePressEvent(self, event):
        if self.primer.isHybed == False:
            self.hybridize()
            self.primer.isHybed = True

    def hoverMoveEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)

    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(self.fill))
        painter.drawRect(self.rect)

