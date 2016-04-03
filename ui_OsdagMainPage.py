# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OsdagMainPage.ui'
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
        MainWindow.resize(1352, 1110)
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
        self.myListWidget = QtGui.QListWidget(self.centralwidget)
        self.myListWidget.setMinimumSize(QtCore.QSize(300, 0))
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
        self.myStackedWidget = QtGui.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        self.myStackedWidget.setFont(font)
        self.myStackedWidget.setObjectName(_fromUtf8("myStackedWidget"))
        self.Osdagpage = QtGui.QWidget()
        self.Osdagpage.setObjectName(_fromUtf8("Osdagpage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Osdagpage)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lbl_OsdagHeader = QtGui.QLabel(self.Osdagpage)
        self.lbl_OsdagHeader.setMinimumSize(QtCore.QSize(800, 200))
        self.lbl_OsdagHeader.setMaximumSize(QtCore.QSize(800, 200))
        self.lbl_OsdagHeader.setText(_fromUtf8(""))
        self.lbl_OsdagHeader.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/Osdag_header.png")))
        self.lbl_OsdagHeader.setScaledContents(True)
        self.lbl_OsdagHeader.setObjectName(_fromUtf8("lbl_OsdagHeader"))
        self.gridLayout_2.addWidget(self.lbl_OsdagHeader, 0, 0, 1, 3)
        self.lbl_iitblogo = QtGui.QLabel(self.Osdagpage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_iitblogo.sizePolicy().hasHeightForWidth())
        self.lbl_iitblogo.setSizePolicy(sizePolicy)
        self.lbl_iitblogo.setMinimumSize(QtCore.QSize(100, 100))
        self.lbl_iitblogo.setText(_fromUtf8(""))
        self.lbl_iitblogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/iit_logo.png")))
        self.lbl_iitblogo.setScaledContents(True)
        self.lbl_iitblogo.setObjectName(_fromUtf8("lbl_iitblogo"))
        self.gridLayout_2.addWidget(self.lbl_iitblogo, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(455, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.lbl_fosseelogo = QtGui.QLabel(self.Osdagpage)
        self.lbl_fosseelogo.setMinimumSize(QtCore.QSize(250, 92))
        self.lbl_fosseelogo.setMaximumSize(QtCore.QSize(250, 92))
        self.lbl_fosseelogo.setText(_fromUtf8(""))
        self.lbl_fosseelogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/Fossee_logo.png")))
        self.lbl_fosseelogo.setScaledContents(True)
        self.lbl_fosseelogo.setObjectName(_fromUtf8("lbl_fosseelogo"))
        self.gridLayout_2.addWidget(self.lbl_fosseelogo, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 556, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.myStackedWidget.addWidget(self.Osdagpage)
        self.Connectionpage = QtGui.QWidget()
        self.Connectionpage.setObjectName(_fromUtf8("Connectionpage"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.Connectionpage)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mytabWidget = QtGui.QTabWidget(self.Connectionpage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mytabWidget.sizePolicy().hasHeightForWidth())
        self.mytabWidget.setSizePolicy(sizePolicy)
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
        self.gridLayout_3 = QtGui.QGridLayout(self.tab1_shearconnection)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.rdbtn_finplate = QtGui.QRadioButton(self.tab1_shearconnection)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rdbtn_finplate.setFont(font)
        self.rdbtn_finplate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_finplate.setObjectName(_fromUtf8("rdbtn_finplate"))
        self.gridLayout_3.addWidget(self.rdbtn_finplate, 0, 1, 1, 1)
        self.rdbtn_cleat = QtGui.QRadioButton(self.tab1_shearconnection)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.rdbtn_cleat.setFont(font)
        self.rdbtn_cleat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_cleat.setStyleSheet(_fromUtf8("QRadioButton {\n"
"text-shadow : black 0.1em 0.1em 0.2em  ;\n"
"}"))
        self.rdbtn_cleat.setObjectName(_fromUtf8("rdbtn_cleat"))
        self.gridLayout_3.addWidget(self.rdbtn_cleat, 0, 5, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.lbl_finplate = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_finplate.setText(_fromUtf8(""))
        self.lbl_finplate.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/finplate.png")))
        self.lbl_finplate.setScaledContents(False)
        self.lbl_finplate.setObjectName(_fromUtf8("lbl_finplate"))
        self.gridLayout_3.addWidget(self.lbl_finplate, 1, 1, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(126, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 4, 1, 1)
        self.lbl_cleatAngle = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_cleatAngle.setText(_fromUtf8(""))
        self.lbl_cleatAngle.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/cleatangle.png")))
        self.lbl_cleatAngle.setScaledContents(False)
        self.lbl_cleatAngle.setObjectName(_fromUtf8("lbl_cleatAngle"))
        self.gridLayout_3.addWidget(self.lbl_cleatAngle, 1, 5, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 8, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 326, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 326, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 2, 7, 1, 1)
        self.rdbtn_endplate = QtGui.QRadioButton(self.tab1_shearconnection)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rdbtn_endplate.setFont(font)
        self.rdbtn_endplate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_endplate.setObjectName(_fromUtf8("rdbtn_endplate"))
        self.gridLayout_3.addWidget(self.rdbtn_endplate, 3, 1, 1, 1)
        self.rdbtn_seat = QtGui.QRadioButton(self.tab1_shearconnection)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rdbtn_seat.setFont(font)
        self.rdbtn_seat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdbtn_seat.setObjectName(_fromUtf8("rdbtn_seat"))
        self.gridLayout_3.addWidget(self.rdbtn_seat, 3, 5, 1, 2)
        spacerItem7 = QtGui.QSpacerItem(125, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 4, 0, 1, 1)
        self.lbl_endplate = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_endplate.setText(_fromUtf8(""))
        self.lbl_endplate.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/endplate.png")))
        self.lbl_endplate.setScaledContents(False)
        self.lbl_endplate.setObjectName(_fromUtf8("lbl_endplate"))
        self.gridLayout_3.addWidget(self.lbl_endplate, 4, 1, 2, 3)
        self.lbl_seat = QtGui.QLabel(self.tab1_shearconnection)
        self.lbl_seat.setText(_fromUtf8(""))
        self.lbl_seat.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/seated.png")))
        self.lbl_seat.setScaledContents(False)
        self.lbl_seat.setObjectName(_fromUtf8("lbl_seat"))
        self.gridLayout_3.addWidget(self.lbl_seat, 4, 5, 2, 3)
        spacerItem8 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 4, 8, 2, 1)
        spacerItem9 = QtGui.QSpacerItem(126, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 5, 4, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(143, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 6, 2, 1, 1)
        self.btn_start = QtGui.QPushButton(self.tab1_shearconnection)
        self.btn_start.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_start.setMaximumSize(QtCore.QSize(190, 30))
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
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.gridLayout_3.addWidget(self.btn_start, 6, 3, 1, 3)
        spacerItem11 = QtGui.QSpacerItem(261, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 6, 6, 1, 1)
        self.mytabWidget.addTab(self.tab1_shearconnection, _fromUtf8(""))
        self.tab2_momentconnection = QtGui.QWidget()
        self.tab2_momentconnection.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tab2_momentconnection.setObjectName(_fromUtf8("tab2_momentconnection"))
        self.mytabWidget.addTab(self.tab2_momentconnection, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.mytabWidget)
        self.myStackedWidget.addWidget(self.Connectionpage)
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
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.myStackedWidget.addWidget(self.page)
        self.gridLayout.addWidget(self.myStackedWidget, 0, 2, 1, 1)
        self.btn_connection = QtGui.QPushButton(self.centralwidget)
        self.btn_connection.setGeometry(QtCore.QRect(60, 120, 200, 35))
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
        self.btn_tension.setGeometry(QtCore.QRect(60, 180, 200, 35))
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
        self.btn_compression.setGeometry(QtCore.QRect(60, 240, 200, 35))
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
        self.btn_flexural.setGeometry(QtCore.QRect(60, 300, 200, 35))
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
        self.btn_beamCol.setGeometry(QtCore.QRect(60, 360, 200, 35))
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
        self.btn_plate.setGeometry(QtCore.QRect(60, 420, 200, 35))
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
        self.btn_gantry.setGeometry(QtCore.QRect(60, 480, 200, 35))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 25))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Osdag", None))
        self.btn_help.setText(_translate("MainWindow", "Help", None))
        self.btn_openfile.setText(_translate("MainWindow", "Open file", None))
        __sortingEnabled = self.myListWidget.isSortingEnabled()
        self.myListWidget.setSortingEnabled(False)
        item = self.myListWidget.item(0)
        item.setText(_translate("MainWindow", " Design :", None))
        self.myListWidget.setSortingEnabled(__sortingEnabled)
        self.mytabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"#\">Shear Connection</a></p></body></html>", None))
        self.rdbtn_finplate.setText(_translate("MainWindow", "Fin Plate", None))
        self.rdbtn_cleat.setText(_translate("MainWindow", "Cleat Angle", None))
        self.rdbtn_endplate.setText(_translate("MainWindow", "End Plate", None))
        self.rdbtn_seat.setText(_translate("MainWindow", "Seated", None))
        self.btn_start.setText(_translate("MainWindow", "Start", None))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab1_shearconnection), _translate("MainWindow", "Shear Connection", None))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab2_momentconnection), _translate("MainWindow", "Moment Connection", None))
        self.label.setText(_translate("MainWindow", "Coming Soon.....", None))
        self.btn_connection.setText(_translate("MainWindow", "Connection", None))
        self.btn_tension.setText(_translate("MainWindow", "Tension Member", None))
        self.btn_compression.setText(_translate("MainWindow", "Compression Member", None))
        self.btn_flexural.setText(_translate("MainWindow", "Flexural Member", None))
        self.btn_beamCol.setText(_translate("MainWindow", "Beam-Column", None))
        self.btn_plate.setText(_translate("MainWindow", "Plate Girder", None))
        self.btn_gantry.setText(_translate("MainWindow", "Gantry Girder", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

import osdagMainPageIcons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

