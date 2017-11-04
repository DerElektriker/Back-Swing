import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):        
    def __init__(self):
        super(Example, self).__init__()            
        self.initUI()
        self.setMouseTracking(1)
        self.xMouse=-100
        self.yMouse=-100
        self.buffer=""
        self.lastBuffer=list()
        self.lastBufferCursor=0
        self.aux = QtGui.QPixmap("gen.png")
        self.text = u'Remil PUTO el que lee'
        #self.lbl.setScaledContents(True)

        #picSize = QtCore.QSize(lbl.width() / 2 , lbl.height() / 2)
        #lbl.resize(picSize)


        
        # self.setWindowTitle('Viewer')
        # self.show()

    def mousePressEvent(self, QMouseEvent):
        print (QMouseEvent.pos())
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            print ("Simple mouse motion")
            cursor =QtGui.QCursor()
            self.update()
            self.xMouse=event.x()
            self.yMouse=event.y()
        elif event.buttons() == QtCore.Qt.LeftButton:
            print ("Left click drag")
        elif event.buttons() == QtCore.Qt.RightButton:
            print ("Right click drag")      

    def initUI(self):                           
            # qbtn = QtGui.QPushButton('Quit', self)
            # qbtn.resize(qbtn.sizeHint())
            # qbtn.move(50, 50)       

        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle('Quit button')    
        self.setWindowFlags(self.windowFlags())
        self.show()


    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        print("X->",self.xMouse,"  Y->",self.yMouse)
        #qp.drawPixmap(self.xMouse-65,self.yMouse-65 ,self.aux)
        
        txt=self.buffer

    
        qp.setBrush(QtGui.QColor.fromRgb(0.4, 0.4, 0.4,1))
        
        #rect=QtGui.QFontMetrics.boundingRect(txt)
        textbox=QtCore.QRect(self.xMouse+10,self.yMouse+10 , 10 ,10)
        textbox = qp.drawText(textbox,QtCore.Qt.TextWordWrap, txt) # draw to get the bounding rectangle
        qp.setBrush(QtGui.QBrush(QtGui.QColor(128,128,128)))
        qp.drawRect(textbox)
        qp.setPen(QtCore.Qt.white)
        qp.drawText(textbox,QtCore.Qt.TextWordWrap, 
        txt) # draw again on top of the box


        qp.end()
        print (self.buffer)
        
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 

    def test(self):
        print ("test")
    
    def keyPressEvent(self, e):
        if(e.key()==QtCore.Qt.Key_Backspace):
            if len(self.buffer)>0:
                self.buffer=self.buffer[:-1]
                self.lastBufferCursor=0

        elif e.key()==QtCore.Qt.Key_Enter or e.key()==QtCore.Qt.Key_Return:
            if(len(self.lastBuffer)>5):
                self.lastBuffer.pop(0)
            self.lastBuffer.append(self.buffer)
            self.lastBufferCursor=0
            self.buffer=""

        
        elif e.key()==QtCore.Qt.Key_Escape:
            self.buffer=""
            print("Escape pressed")


        elif e.key()==QtCore.Qt.Key_Up:
            if not(abs(self.lastBufferCursor)>(len(self.lastBuffer)-1)):
                print("YAY")
                self.lastBufferCursor-=1
                self.buffer=self.lastBuffer[self.lastBufferCursor]

        else:
            self.buffer+=e.text()
            self.lastBufferCursor=0

        self.update()

def main():        
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
