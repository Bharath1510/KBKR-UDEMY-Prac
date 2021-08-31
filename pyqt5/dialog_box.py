from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyDialog(QDialog):
    def __init__(self,*a,**b):
        super(MyDialog,self).__init__(*a,**b)
        self.setWindowTitle('dialog box')
        self.resize(200,200)
        self.layout = QVBoxLayout()
        self.label = QLabel('DIALOG')
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)



class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()

        btn = QPushButton('press here')
        btn.pressed.connect(self.new_dialog)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def new_dialog(self):
        dialog = MyDialog()
        dialog.label.setText('NEW DIALOG')
        dialog.exec()




app = QApplication([])
window = MyWindow()
window.show()
app.exec()