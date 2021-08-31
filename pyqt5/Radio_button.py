from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()

        male_btn = QRadioButton("Male")
        female_btn = QRadioButton("Female")
        self.label = QLabel("select your gender")

        male_btn.toggled.connect(lambda: self.show_selected(male_btn))
        female_btn.toggled.connect(lambda: self.show_selected(female_btn))

        layout.addWidget(male_btn)
        layout.addWidget(female_btn)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_selected(self,gender):
        self.label.setText(gender.text())



app = QApplication([])
window = MyWindow()
window.show()
app.exec()