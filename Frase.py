# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frase.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random

class Ui_TelaFrase(object):
    def gerar_Frase(self):
        n = random.randint(1, 18) #obs: mudar isso quando finalizar as frases no banco!!!!!!!!
        print(n)

        connection = sqlite3.connect("database.db")
        c = connection.cursor()

        for linha in c.execute("SELECT ROWID, FRASE FROM FRASES"):
            if(linha[0] == n):
                frase = linha[1]
                return frase
        connection.close()

    def setupUi(self, TelaFrase):
        TelaFrase.setObjectName("TelaFrase")
        TelaFrase.resize(390, 121)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaFrase.setWindowIcon(icon)
        self.label_frase = QtWidgets.QLabel(TelaFrase)
        self.label_frase.setGeometry(QtCore.QRect(10, 10, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_frase.setFont(font)
        self.label_frase.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_frase.setWordWrap(True)
        self.label_frase.setObjectName("label_frase")

        self.retranslateUi(TelaFrase)
        QtCore.QMetaObject.connectSlotsByName(TelaFrase)

    def retranslateUi(self, TelaFrase):
        _translate = QtCore.QCoreApplication.translate
        TelaFrase.setWindowTitle(_translate("TelaFrase", "..."))
        frase = self.gerar_Frase()
        self.label_frase.setText(_translate("TelaFrase", frase))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaFrase = QtWidgets.QDialog()
    ui = Ui_TelaFrase()
    ui.setupUi(TelaFrase)
    TelaFrase.show()
    sys.exit(app.exec_())
