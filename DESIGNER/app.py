from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MyWindow import Ui_MainWindow
from MyDialog import Ui_Dialog

class Dialog(QDialog):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None): 
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_stuff)
        self.done=[]
        self.not_done=[]
        self.pushButton_3.clicked.connect(self.do_task)
        self.pushButton_2.clicked.connect(self.undo_task)

    def add_task(self,task):
        if bool(task) == True:
            self.remaining_list.addItem(task)

    def do_task(self):
        task = self.remaining_list.takeItem(self.remaining_list.currentRow())
        if bool(task)==True:
            self.finished_list.addItem(task.text())
    
    def undo_task(self):
        task = self.finished_list.takeItem(self.finished_list.currentRow())
        if bool(task)==True:
            self.remaining_list.addItem(task.text())

    def add_stuff(self):
        dlg = Dialog()
        dlg.ui.buttonBox.accepted.connect(
            lambda: self.add_task(dlg.ui.lineEdit.text())
        )
        dlg.exec()



app = QApplication([])
window = MainWindow()
window.show()
app.exec()