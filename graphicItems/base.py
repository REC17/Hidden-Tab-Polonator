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
        


    def mousePressEvent(self, event):


     #   if self.parentItem().__class__.__name__ != 'Primer':
        if self.pos().x()/12 < self.parentItem().boundingRect().width()/24:
            self.position = str(int(1 + self.pos().x()/12))
        else:
            self.position = str(int(20 - self.pos().x()/12))

        if self.primer != None:
            if self.fill == self.purple:
                self.fill = self.red
                self.parentItem().baseSeqL.append(self)
            elif self.fill == self.red:
                self.fill = self.purple
                self.parentItem().baseSeqL.remove(self)
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
            if self.pos().x()/12 < self.parentItem().boundingRect().width()/24:
                self.position = str(int(1 + self.pos().x()/12))
            else:
                self.position = str(int(20 - self.pos().x()/12))

            if self.selected == False:
         #   if self.scene().views()[0].held == True:
                if self.fill == self.purple:
                    self.fill = self.red
                    self.parentItem().baseSeqL.append(self)
                elif self.fill == self.red:
                    self.fill = self.purple
                    self.parentItem().baseSeqL.remove(self)
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



