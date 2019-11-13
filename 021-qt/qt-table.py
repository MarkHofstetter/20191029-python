import sys
from PySide2.QtWidgets import *
#	import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import *

headers = ['A', 'B', 'C']
rows = [(2,3,4), (3,4,5), (1,78,9)]

class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)
    
    def columnCount(self, parent):
        return len(headers)
        
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return None
        return rows[index.row()][index.column()]
        
    def headerData(self, section, orientation, role):    
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return None
        return headers[section]

class TableWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.model = TableModel()
        self.tableview = QTableView()
        self.tableview.setModel(self.model)
                
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.tableview)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TableWidget()
    widget.resize(400,400)
    widget.show()
    
    sys.exit(app.exec_())