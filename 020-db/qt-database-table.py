import sys
from PySide2.QtWidgets import *
#	import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import *
import importlib
data_source = importlib.import_module('data_source') 
    
class TableModel(QAbstractTableModel):
    from data_source import get_data;
    
    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)
        # self.rows, self.count, self.headers = self.get_data()
        self.get_data()
    
    def rowCount(self, parent = None):
        return self.count
    
    def columnCount(self, parent):
        return len(self.headers)
        
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return None
        return self.rows[index.row()][index.column()]
        
    def headerData(self, section, orientation, role):    
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return None
        return self.headers[section]

class TableWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.model = TableModel()
        self.tableview = QTableView()
        self.tableview.setModel(self.model)
        self.searchbox = QLineEdit(self)
                
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.searchbox)
        self.layout.addWidget(self.tableview)
        self.searchbox.textChanged.connect(self.text_change)
    
    @Slot()
    def text_change(self):
        self.model.get_data(filter = self.searchbox.text())
        self.model.rowCount()
        self.model.dataChanged.emit((0,0), 
                                    (1,self.model.count))       
        print(self.searchbox.text())    
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TableWidget()
    widget.resize(400,400)
    widget.show()
    
    sys.exit(app.exec_())