import sys
from PySide2.QtWidgets \
	import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

class DemoWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.textlabel = QLabel("Start Text")
        self.button = QPushButton("Click me!")
        
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.textlabel)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        
        self.button.clicked.connect(self.press)
        
    @Slot()
    def press(self):
        self.textlabel.setText('Button Pressed!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DemoWidget()
    widget.resize(400,400)
    widget.show()
    
    sys.exit(app.exec_())