'''
Created on 31-Mar-2016

@author: deepa
'''
import sys
from PyQt4 import QtGui,QtCore
from ui_osdagMainPage import Ui_MainWindow
from Connections.Shear.Finplate.finPlateMain import launchFinPlateController

class OsdagMainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        listItems = {'Osdagpage':0,'connectionpage':1,'tensionpage':2,'compressionpage':3,'flexuralpage':4}
        
        self.ui.myStackedWidget.setCurrentIndex(listItems['Osdagpage'])
        self.ui.btn_connection.clicked.connect(lambda:self.changePage(listItems['connectionpage'],listItems['Osdagpage']))
        self.ui.myListWidget.currentItemChanged.connect(self.changePage)
        
        self.ui.btn_start.clicked.connect(self.showConnection)
        
    def changePage(self, current, previous):
        if not current:
            current = previous

        self.ui.myStackedWidget.setCurrentIndex(current)
    
    def showConnection(self):
        
        if self.ui.rdbtn_finplate.isChecked():
            launchFinPlateController(self)
            self.ui.myStackedWidget.setCurrentIndex(0)
            
        elif self.ui.rdbtn_cleatangle.isChecked():
            QtGui.QMessageBox.about(self,"INFO","Cleat connection design is coming soon!")
        
        elif self.ui.rdbtn_endplate.isChecked():
            QtGui.QMessageBox.about(self,"INFO","End plate connection design is coming soon!")
        
        elif self.ui.rdbtn_seated.isChecked():
            QtGui.QMessageBox.about(self,"INFO","Seated connection design is coming soon!")
        
        else:
            QtGui.QMessageBox.about(self,"INFO","Please select appropriate connection")
            
        
    

    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = OsdagMainWindow()
    window.show()
    sys.exit(app.exec_())