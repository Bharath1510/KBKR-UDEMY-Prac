from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()

        lists = QListWidget()
        lists.addItems(['easy','hard','expert'])
        lists.currentItemChanged.connect(self.show_selected)

        layout.addWidget(lists)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_selected(self,item):
        print(item.text())




app = QApplication([])
window = MyWindow()
window.show()
app.exec()