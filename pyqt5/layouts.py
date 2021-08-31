from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
       
        grid = QGridLayout()
        grid.addWidget(QLabel("hello"),0,0)
        grid.addWidget(QLabel("bharath"),1,1)
        grid.addWidget(QLabel("kumar"),2,2)
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)





app = QApplication([])
window = MyWindow()
window.show()
app.exec()