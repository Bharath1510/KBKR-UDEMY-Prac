from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("Button's Window")
        self.resize(500,500)
        layout = QVBoxLayout()

        btn_1 = QPushButton("button 1")
        btn_2 = QPushButton("button 2")
        self.label = QLabel("Click any button:")
        font = self.label.font()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        btn_1.clicked.connect(self.btn1_clicked)
        btn_2.clicked.connect(self.btn2_clicked)

        layout.addWidget(self.label)
        layout.addWidget(btn_1)
        layout.addWidget(btn_2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def btn1_clicked(self):
        self.label.setText("Button 1 Clicked")
        
    
    def btn2_clicked(self):
        self.label.setText("Button 2 Clicked")
       

    
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

