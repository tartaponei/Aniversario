# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Texto import Ui_TelaTexto
from Principal import Ui_TelaPrincipal

class Ui_TelaLogin(object):
    def show_MessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def show_Texto(self):
        self.janelaTxt = QtWidgets.QDialog()
        self.ui = Ui_TelaTexto()
        self.ui.setupUi(self.janelaTxt)
        self.janelaTxt.show()
        TelaLogin.close()

    def show_Principal(self):
        self.janelaPrincipal = QtWidgets.QDialog()
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self.janelaPrincipal)
        self.janelaPrincipal.show()
        TelaLogin.close()

    def update_Entrada(self):
        login = self.form_login.text()

        connection = sqlite3.connect("database.db")
        #c = connection.cursor()
        connection.execute("UPDATE USERS SET ENTRADA = 1 WHERE LOGIN = ?", (login,))
        connection.commit()
        #c.close()
        connection.close()

    def loginCheck(self):
        entrada = 2
        login = self.form_login.text()
        senha = self.form_senha.text()

        connection = sqlite3.connect("database.db")
        c = connection.cursor()
        result = c.execute("SELECT * FROM USERS WHERE LOGIN = ? AND SENHA = ?", (login, senha))
        for linha in result:
            entrada = linha[2]
            print(entrada)

        if(entrada != 2): #se tiver achado
            if(entrada == 0):
                self.show_Texto()
                self.update_Entrada()
            else:
                self.show_Principal()
        else:
            print("usuario nao achado")
            self.show_MessageBox("Ei!", "Login e/ou senha inválidos.")

        connection.close()

    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(331, 251)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaLogin.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label_bemvindo1 = QtWidgets.QLabel(self.centralwidget)
        self.label_bemvindo1.setGeometry(QtCore.QRect(40, 0, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_bemvindo1.setFont(font)
        self.label_bemvindo1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bemvindo1.setObjectName("label_bemvindo1")
        self.label_entrarlogin = QtWidgets.QLabel(self.centralwidget)
        self.label_entrarlogin.setGeometry(QtCore.QRect(70, 50, 190, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_entrarlogin.setFont(font)
        self.label_entrarlogin.setObjectName("label_entrarlogin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.form_login = QtWidgets.QLineEdit(self.centralwidget)
        self.form_login.setGeometry(QtCore.QRect(130, 100, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.form_login.setFont(font)
        self.form_login.setMaxLength(15)
        self.form_login.setObjectName("form_login")
        self.form_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.form_senha.setGeometry(QtCore.QRect(130, 130, 113, 21))
        self.form_senha.setMaxLength(10)
        self.form_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.form_senha.setObjectName("form_senha")
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(210, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_entrar.setFont(font)
        self.btn_entrar.setObjectName("btn_entrar")

        #evento do botão:
        self.btn_entrar.clicked.connect(self.loginCheck)

        TelaLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        TelaLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaLogin)
        self.statusbar.setObjectName("statusbar")
        TelaLogin.setStatusBar(self.statusbar)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)
    """
    def __init__(self):
        self.btn_entrar.clicked.connect(self.close)
    """

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Olá!"))
        self.label_bemvindo1.setText(_translate("TelaLogin", "Olá, bem vindo!"))
        self.label_entrarlogin.setText(_translate("TelaLogin", "Entre com seu login e senha."))
        self.label_3.setText(_translate("TelaLogin", "Login:"))
        self.label_4.setText(_translate("TelaLogin", "Senha:"))
        self.form_login.setPlaceholderText(_translate("TelaLogin", "Digite seu login..."))
        self.form_senha.setPlaceholderText(_translate("TelaLogin", "Digite sua senha..."))
        self.btn_entrar.setText(_translate("TelaLogin", "Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())
