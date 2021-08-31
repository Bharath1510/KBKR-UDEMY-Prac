from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

class My_Window(QMainWindow):
    def __init__(self,*a,**b):
        super(My_Window,self).__init__(*a,**b)
        self.setWindowTitle("bharath's window")
        self.resize(500,500)
        label = QLabel("hello this is KBKR")
        font = label.font()
        font.setPointSize(40)
        label.setFont(font)
        self.setCentralWidget(label)

app = QApplication([])
window = My_Window()
window.show()
app.exec()