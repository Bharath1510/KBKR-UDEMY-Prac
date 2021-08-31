from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self,*a,**b):
        super(MyWindow,self).__init__(*a,**b)
        self.setWindowTitle("CheckBoxes")
        self.resize(500,500)
        layout = QVBoxLayout()

        check1 = QCheckBox("pick up groceries")
        check1.toggled.connect(lambda: self.something_checked(check1))

        check2 = QCheckBox("code everyday")
        check2.toggled.connect(lambda: self.something_checked(check2))

        self.label = QLabel('you have not selected anything')

        self.checked_stuff =[]

        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def something_checked(self,check):
        if check.isChecked() == False:
            self.checked_stuff = list(filter(lambda stuff: (
                stuff != check.text()), self.checked_stuff))
        else:
            self.checked_stuff.append(check.text())
        task_string = ""
        for task in self.checked_stuff:
            task_string += (task+"\n")

        self.label.setText(task_string)


app = QApplication([])
window = MyWindow()
window.show()
app.exec()

