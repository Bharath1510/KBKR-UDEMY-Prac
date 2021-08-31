from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()
        tab = QTabWidget()
        tab.setMovable(True)
        tab.addTab(QLabel('this is tab1 \n one'),'one')
        tab.addTab(QLabel('this is tab2'),'two')

        layout.addWidget(tab)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)





app = QApplication([])
window = MyWindow()
window.show()
app.exec()