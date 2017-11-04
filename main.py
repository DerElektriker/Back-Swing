import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):        
    def __init__(self):
        super(Example, self).__init__()            
        self.initUI()
        self.setMouseTracking(1)
        self.xMouse=-100
        self.yMouse=-100

        self.aux = QtGui.QPixmap("gen.png")
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
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
        qp.drawPixmap(self.xMouse-65,self.yMouse-65 ,self.aux)
        qp.end()
        
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 

    def test(self):
      print ("test")

def main():        
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
