from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()
    
        combo = QComboBox()
        combo.addItems(['easy','normal','difficult'])
        btn = QPushButton('start')
        btn.pressed.connect(lambda: self.show_selected(combo))
        
        layout.addWidget(combo)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_selected(self,button):
        print(button.currentText())




app = QApplication([])
window = MyWindow()
window.show()
app.exec()