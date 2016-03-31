# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'osdagMainPage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1709, 1051)
        MainWindow.setStyleSheet(_fromUtf8("QWidget::showMaximised()"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_help = QtGui.QPushButton(self.centralwidget)
        self.btn_help.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_help.setAutoDefault(True)
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.gridLayout.addWidget(self.btn_help, 1, 1, 1, 1)
        self.btn_openfile = QtGui.QPushButton(self.centralwidget)
        self.btn_openfile.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_openfile.setAutoDefault(True)
        self.btn_openfile.setObjectName(_fromUtf8("btn_openfile"))
        self.gridLayout.addWidget(self.btn_openfile, 1, 0, 1, 1)
        self.myStackedWidget = QtGui.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        self.myStackedWidget.setFont(font)
        self.myStackedWidget.setObjectName(_fromUtf8("myStackedWidget"))
        self.Osdagpage = QtGui.QWidget()
        self.Osdagpage.setObjectName(_fromUtf8("Osdagpage"))
        self.lbl_OsdagHeader = QtGui.QLabel(self.Osdagpage)
        self.lbl_OsdagHeader.setGeometry(QtCore.QRect(30, 60, 1871, 381))
        self.lbl_OsdagHeader.setText(_fromUtf8(""))
        self.lbl_OsdagHeader.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/Osdag_header.png")))
        self.lbl_OsdagHeader.setObjectName(_fromUtf8("lbl_OsdagHeader"))
        self.lbl_fosseelogo = QtGui.QLabel(self.Osdagpage)
        self.lbl_fosseelogo.setGeometry(QtCore.QRect(50, 670, 250, 92))
        self.lbl_fosseelogo.setText(_fromUtf8(""))
        self.lbl_fosseelogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/Fossee_logo.png")))
        self.lbl_fosseelogo.setObjectName(_fromUtf8("lbl_fosseelogo"))
        self.lbl_iitblogo = QtGui.QLabel(self.Osdagpage)
        self.lbl_iitblogo.setGeometry(QtCore.QRect(890, 590, 290, 201))
        self.lbl_iitblogo.setText(_fromUtf8(""))
        self.lbl_iitblogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/iit_logo.png")))
        self.lbl_iitblogo.setScaledContents(False)
        self.lbl_iitblogo.setObjectName(_fromUtf8("lbl_iitblogo"))
        self.myStackedWidget.addWidget(self.Osdagpage)
        self.connectionpage = QtGui.QWidget()
        self.connectionpage.setObjectName(_fromUtf8("connectionpage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.connectionpage)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mytabWidget = QtGui.QTabWidget(self.connectionpage)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mytabWidget.setFont(font)
        self.mytabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mytabWidget.setStyleSheet(_fromUtf8("QTabBar::tab {\n"
"    margin-right: 10;\n"
" }\n"
"QTabBar::tab::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"height: 40px;\n"
"width: 200px;\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}\n"
"QTabBar::tab{\n"
"border-top-left-radius: 2px ;\n"
"border-top-right-radius: 2px ;\n"
"border-bottom-left-radius: 0px ;\n"
"border-bottom-right-radius: 0px ;\n"
"}\n"
" "))
        self.mytabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.mytabWidget.setObjectName(_fromUtf8("mytabWidget"))
        self.tab1_shearconnection = QtGui.QWidget()
        font = QtGui.QFont()
        font.setItalic(True)
        self.tab1_shearconnection.setFont(font)
        self.tab1_shearconnection.setObjectName(_fromUtf8("tab1_shearconnection"))
        self.rdbtn_finplate = QtGui.QRadioButton(self.tab1_shearconnection)
        self.rdbtn_finplate.setGeometry(QtCore.QRect(330, 30, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rdbtn_finplate.setFont(font)
        self.rdbtn_finplate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_finplate.setObjectName(_fromUtf8("rdbtn_finplate"))
        self.rdbtn_seated = QtGui.QRadioButton(self.tab1_shearconnection)
        self.rdbtn_seated.setGeometry(QtCore.QRect(830, 330, 101, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rdbtn_seated.setFont(font)
        self.rdbtn_seated.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_seated.setObjectName(_fromUtf8("rdbtn_seated"))
        self.rdbtn_cleatangle = QtGui.QRadioButton(self.tab1_shearconnection)
        self.rdbtn_cleatangle.setGeometry(QtCore.QRect(830, 30, 151, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.rdbtn_cleatangle.setFont(font)
        self.rdbtn_cleatangle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_cleatangle.setStyleSheet(_fromUtf8("QRadioButton {\n"
"text-shadow : black 0.1em 0.1em 0.2em  ;\n"
"}"))
        self.rdbtn_cleatangle.setObjectName(_fromUtf8("rdbtn_cleatangle"))
        self.rdbtn_endplate = QtGui.QRadioButton(self.tab1_shearconnection)
        self.rdbtn_endplate.setGeometry(QtCore.QRect(340, 330, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rdbtn_endplate.setFont(font)
        self.rdbtn_endplate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_endplate.setObjectName(_fromUtf8("rdbtn_endplate"))
        self.btn_start = QtGui.QPushButton(self.tab1_shearconnection)
        self.btn_start.setGeometry(QtCore.QRect(620, 620, 200, 32))
        self.btn_start.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_start.setAutoDefault(True)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.lbl_cleat = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_cleat.setGeometry(QtCore.QRect(860, 80, 200, 200))
        self.lbl_cleat.setText(_fromUtf8(""))
        self.lbl_cleat.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/cleatangle.png")))
        self.lbl_cleat.setScaledContents(True)
        self.lbl_cleat.setObjectName(_fromUtf8("lbl_cleat"))
        self.lbl_endplate = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_endplate.setGeometry(QtCore.QRect(370, 380, 200, 171))
        self.lbl_endplate.setText(_fromUtf8(""))
        self.lbl_endplate.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/endplate.png")))
        self.lbl_endplate.setScaledContents(True)
        self.lbl_endplate.setObjectName(_fromUtf8("lbl_endplate"))
        self.lbl_seat = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_seat.setGeometry(QtCore.QRect(860, 380, 200, 200))
        self.lbl_seat.setText(_fromUtf8(""))
        self.lbl_seat.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/seated.png")))
        self.lbl_seat.setScaledContents(True)
        self.lbl_seat.setObjectName(_fromUtf8("lbl_seat"))
        self.lbl_finplate = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_finplate.setGeometry(QtCore.QRect(360, 80, 201, 161))
        self.lbl_finplate.setText(_fromUtf8(""))
        self.lbl_finplate.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/finplate.png")))
        self.lbl_finplate.setScaledContents(True)
        self.lbl_finplate.setObjectName(_fromUtf8("lbl_finplate"))
        self.mytabWidget.addTab(self.tab1_shearconnection, _fromUtf8(""))
        self.tab2_momentconnection = QtGui.QWidget()
        self.tab2_momentconnection.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tab2_momentconnection.setObjectName(_fromUtf8("tab2_momentconnection"))
        self.mytabWidget.addTab(self.tab2_momentconnection, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.mytabWidget, 0, 0, 1, 1)
        self.myStackedWidget.addWidget(self.connectionpage)
        self.tensionpage = QtGui.QWidget()
        self.tensionpage.setObjectName(_fromUtf8("tensionpage"))
        self.label = QtGui.QLabel(self.tensionpage)
        self.label.setGeometry(QtCore.QRect(250, 230, 271, 111))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.myStackedWidget.addWidget(self.tensionpage)
        self.compressionpage = QtGui.QWidget()
        self.compressionpage.setObjectName(_fromUtf8("compressionpage"))
        self.myStackedWidget.addWidget(self.compressionpage)
        self.flexuralpage = QtGui.QWidget()
        self.flexuralpage.setObjectName(_fromUtf8("flexuralpage"))
        self.myStackedWidget.addWidget(self.flexuralpage)
        self.gridLayout.addWidget(self.myStackedWidget, 0, 2, 1, 1)
        self.myListWidget = QtGui.QListWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 84, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 84, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 194, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.myListWidget.setPalette(palette)
        self.myListWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.myListWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.myListWidget.setStyleSheet(_fromUtf8("QListWidget\n"
"{\n"
"background-color: #abc250 ;\n"
"}"))
        self.myListWidget.setFrameShape(QtGui.QFrame.Panel)
        self.myListWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.myListWidget.setLineWidth(4)
        self.myListWidget.setMidLineWidth(2)
        self.myListWidget.setObjectName(_fromUtf8("myListWidget"))
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.myListWidget.addItem(item)
        self.gridLayout.addWidget(self.myListWidget, 0, 0, 1, 2)
        self.btn_connection = QtGui.QPushButton(self.centralwidget)
        self.btn_connection.setGeometry(QtCore.QRect(40, 120, 200, 35))
        self.btn_connection.setMouseTracking(False)
        self.btn_connection.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_connection.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn_connection.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}\n"
""))
        self.btn_connection.setAutoDefault(True)
        self.btn_connection.setDefault(False)
        self.btn_connection.setObjectName(_fromUtf8("btn_connection"))
        self.btn_tension = QtGui.QPushButton(self.centralwidget)
        self.btn_tension.setGeometry(QtCore.QRect(40, 180, 200, 35))
        self.btn_tension.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}\n"
""))
        self.btn_tension.setAutoDefault(True)
        self.btn_tension.setObjectName(_fromUtf8("btn_tension"))
        self.btn_compression = QtGui.QPushButton(self.centralwidget)
        self.btn_compression.setGeometry(QtCore.QRect(40, 240, 200, 35))
        self.btn_compression.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}\n"
""))
        self.btn_compression.setAutoDefault(True)
        self.btn_compression.setObjectName(_fromUtf8("btn_compression"))
        self.btn_flexural = QtGui.QPushButton(self.centralwidget)
        self.btn_flexural.setGeometry(QtCore.QRect(40, 300, 200, 35))
        self.btn_flexural.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_flexural.setAutoDefault(True)
        self.btn_flexural.setObjectName(_fromUtf8("btn_flexural"))
        self.btn_beamCol = QtGui.QPushButton(self.centralwidget)
        self.btn_beamCol.setGeometry(QtCore.QRect(40, 360, 200, 35))
        self.btn_beamCol.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_beamCol.setAutoDefault(True)
        self.btn_beamCol.setObjectName(_fromUtf8("btn_beamCol"))
        self.btn_plate = QtGui.QPushButton(self.centralwidget)
        self.btn_plate.setGeometry(QtCore.QRect(40, 420, 200, 35))
        self.btn_plate.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_plate.setAutoDefault(True)
        self.btn_plate.setObjectName(_fromUtf8("btn_plate"))
        self.btn_gantry = QtGui.QPushButton(self.centralwidget)
        self.btn_gantry.setGeometry(QtCore.QRect(40, 480, 200, 35))
        self.btn_gantry.setStyleSheet(_fromUtf8("QPushButton::hover\n"
"{\n"
"   background-color: #d97f7f;\n"
"   color:#000000 ;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: #925a5b;\n"
"color:#ffffff;\n"
"}"))
        self.btn_gantry.setAutoDefault(True)
        self.btn_gantry.setObjectName(_fromUtf8("btn_gantry"))
        self.myListWidget.raise_()
        self.myStackedWidget.raise_()
        self.btn_openfile.raise_()
        self.btn_help.raise_()
        self.btn_connection.raise_()
        self.btn_tension.raise_()
        self.btn_compression.raise_()
        self.btn_flexural.raise_()
        self.btn_beamCol.raise_()
        self.btn_plate.raise_()
        self.btn_gantry.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1709, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.myStackedWidget.setCurrentIndex(1)
        self.mytabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.btn_connection, QtCore.SIGNAL(_fromUtf8("clicked()")), self.mytabWidget.showFullScreen)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Osdag", None))
        self.btn_help.setText(_translate("MainWindow", "Help", None))
        self.btn_openfile.setText(_translate("MainWindow", "Open file", None))
        self.mytabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"#\">Shear Connection</a></p></body></html>", None))
        self.rdbtn_finplate.setText(_translate("MainWindow", "Fin Plate", None))
        self.rdbtn_seated.setText(_translate("MainWindow", "Seated", None))
        self.rdbtn_cleatangle.setText(_translate("MainWindow", "Cleat Angle", None))
        self.rdbtn_endplate.setText(_translate("MainWindow", "End Plate", None))
        self.btn_start.setText(_translate("MainWindow", "Start", None))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab1_shearconnection), _translate("MainWindow", "Shear Connection", None))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab2_momentconnection), _translate("MainWindow", "Moment Connection", None))
        self.label.setText(_translate("MainWindow", "Coming Soon.....", None))
        __sortingEnabled = self.myListWidget.isSortingEnabled()
        self.myListWidget.setSortingEnabled(False)
        item = self.myListWidget.item(0)
        item.setText(_translate("MainWindow", " Design :", None))
        self.myListWidget.setSortingEnabled(__sortingEnabled)
        self.btn_connection.setText(_translate("MainWindow", "Connection", None))
        self.btn_tension.setText(_translate("MainWindow", "Tension Member", None))
        self.btn_compression.setText(_translate("MainWindow", "Compression Member", None))
        self.btn_flexural.setText(_translate("MainWindow", "Flexural Member", None))
        self.btn_beamCol.setText(_translate("MainWindow", "Beam-Column", None))
        self.btn_plate.setText(_translate("MainWindow", "Plate Girder", None))
        self.btn_gantry.setText(_translate("MainWindow", "Gantry Girder", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

import osdag_icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

