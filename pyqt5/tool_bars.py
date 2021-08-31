from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("ToolBar")
        self.resize(500,500)
        layout = QVBoxLayout()
        toolbar = QToolBar("my toolbar")
        action_btn1 = QAction("KBKR",self)
        action_btn1.setCheckable(True)
        toolbar.addAction(action_btn1)
        self.addToolBar(toolbar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)





app = QApplication([])
window = MyWindow()
window.show()
app.exec()