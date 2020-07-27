# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaTexto.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Principal import Ui_TelaPrincipal

click = 1
class Ui_TelaTexto(object):
    def show_Principal(self):
        self.janelaPrincipal = QtWidgets.QDialog()
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self.janelaPrincipal)
        self.janelaPrincipal.show()
        
    def mudarClick():
        global click
        click+=1

    def mudarTexto(self):
        global click

        if(click == 16):
            self.show_Principal()

        connection = sqlite3.connect("login.db")
        c = connection.cursor()

        for linha in c.execute("SELECT ROWID, PARAGRAFO FROM TEXTO"):
            #print(linha)
            if(linha[0] == click):
                self.label_txt.setText(linha[1])
                click+=1
                break

        """
        for linha in c.execute("SELECT * FROM TEXTO"):
            print(linha[0]) #ta printando certinho
            self.label_txt.setText(linha[0])
        """
        connection.close()

    def setupUi(self, TelaTexto):
        TelaTexto.setObjectName("TelaTexto")
        TelaTexto.resize(407, 281)

        self.label_txt = QtWidgets.QLabel(TelaTexto)
        self.label_txt.setGeometry(QtCore.QRect(10, 10, 381, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_txt.setFont(font)
        self.label_txt.setTextFormat(QtCore.Qt.AutoText)
        self.label_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_txt.setWordWrap(True)
        self.label_txt.setObjectName("label_txt")

        self.btn_continuar = QtWidgets.QPushButton(TelaTexto)
        self.btn_continuar.setGeometry(QtCore.QRect(290, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_continuar.setFont(font)
        self.btn_continuar.setObjectName("btn_continuar")

        self.btn_continuar.clicked.connect(lambda: self.mudarTexto())

        self.retranslateUi(TelaTexto)
        QtCore.QMetaObject.connectSlotsByName(TelaTexto)

    def retranslateUi(self, TelaTexto):
        _translate = QtCore.QCoreApplication.translate
        TelaTexto.setWindowTitle(_translate("TelaTexto", "..."))
        self.label_txt.setText(_translate("TelaTexto", "Oi :) Você deve estar se perguntando o que é isso."))
        self.btn_continuar.setText(_translate("TelaTexto", "Continuar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaTexto = QtWidgets.QDialog()
    ui = Ui_TelaTexto()
    ui.setupUi(TelaTexto)
    TelaTexto.show()
    sys.exit(app.exec_())
