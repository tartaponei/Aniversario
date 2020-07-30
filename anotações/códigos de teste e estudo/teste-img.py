# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste-img.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 641, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("cat.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_cat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cat.setGeometry(QtCore.QRect(30, 400, 251, 71))
        self.btn_cat.setObjectName("btn_cat")
        self.btn_dog = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dog.setGeometry(QtCore.QRect(360, 400, 261, 71))
        self.btn_dog.setObjectName("btn_dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_dog.clicked.connect(self.show_dog)
        self.btn_cat.clicked.connect(self.show_cat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_cat.setText(_translate("MainWindow", "Cat"))
        self.btn_dog.setText(_translate("MainWindow", "Dog"))

    def show_dog(self):
        self.label.setPixmap(QtGui.QPixmap("dog.jpg"))

    def show_cat(self):
        self.label.setPixmap(QtGui.QPixmap("cat.webp"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
