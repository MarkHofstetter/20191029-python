import sys
from PySide2.QtWidgets import *
#	import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

class DemoWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.textlabel = QLabel("Start Text")
        self.text2change = QLabel("")
        self.button = QPushButton("Click me!")
        self.textbox = QLineEdit(self)
        
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.text2change)
        self.layout.addWidget(self.textlabel)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        
        self.button.clicked.connect(self.press)
        self.textbox.textChanged.connect(self.text_change)
        
    @Slot()
    def press(self):
        self.textlabel.setText('Button Pressed!')

    '''
    neues QLabel und bei jedem change Signal von textbox, den text 
    neu setzen
    '''
        
    @Slot()
    def text_change(self):
        self.text2change.setText(self.textbox.text())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DemoWidget()
    widget.resize(400,400)
    widget.show()
    
    sys.exit(app.exec_())