from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()

        input_field = QLineEdit()
        input_field.returnPressed.connect(lambda : print(input_field.text()))    

        layout.addWidget(input_field)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)





app = QApplication([])
window = MyWindow()
window.show()
app.exec()