# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from TextoInteiro import Ui_TelaTextoInteiro
from Frase import Ui_TelaFrase
from Evolucao import Ui_TelaEvolucao
from Creditos import Ui_TelaCreditos
import webbrowser
import sys
import sqlite3

sys.path.insert(1, './game')

class Ui_TelaPrincipal(object):
    def show_Creditos(self):
        self.janelaCred = QtWidgets.QDialog()
        self.ui = Ui_TelaCreditos()
        self.ui.setupUi(self.janelaCred)
        self.janelaCred.show()

    def show_Evolucao(self):
        self.janelaEvo = QtWidgets.QDialog()
        self.ui = Ui_TelaEvolucao()
        self.ui.setupUi(self.janelaEvo)
        self.janelaEvo.show()

    def show_Frase(self):
        self.janelaFrase = QtWidgets.QDialog()
        self.ui = Ui_TelaFrase()
        self.ui.setupUi(self.janelaFrase)
        self.janelaFrase.show()

    def show_TextoInteiro(self):
        self.janelaTexto = QtWidgets.QDialog()
        self.ui = Ui_TelaTextoInteiro()
        self.ui.setupUi(self.janelaTexto)
        self.janelaTexto.show()

    def abrirJogo(self):
        from puzzle import GameGrid

    def openSpot(self):
        webbrowser.open("https://open.spotify.com/playlist/6QUi0mtWqckDpAFJBofeRT?si=5zKrtOIZQ5ica45FLTyFgQ")

    def openAlbum(self):
        webbrowser.open("https://photos.app.goo.gl/6U6wphzQ4oCMmcyc7")

    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.resize(543, 362)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipal.setWindowIcon(icon)

        self.label_bemvindo2 = QtWidgets.QLabel(TelaPrincipal)
        self.label_bemvindo2.setGeometry(QtCore.QRect(100, 20, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)

        self.label_bemvindo2.setFont(font)
        self.label_bemvindo2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bemvindo2.setObjectName("label_bemvindo2")

        self.btn_playlist = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_playlist.setGeometry(QtCore.QRect(30, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_playlist.setFont(font)
        self.btn_playlist.setObjectName("btn_playlist")

        self.btn_playlist.clicked.connect(self.openSpot)

        self.btn_evolucao = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_evolucao.setGeometry(QtCore.QRect(30, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_evolucao.setFont(font)
        self.btn_evolucao.setObjectName("btn_evolucao")

        self.btn_evolucao.clicked.connect(self.show_Evolucao)

        self.btn_album = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_album.setGeometry(QtCore.QRect(30, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_album.setFont(font)
        self.btn_album.setObjectName("btn_album")

        self.btn_album.clicked.connect(self.openAlbum)

        self.btn_texto = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_texto.setGeometry(QtCore.QRect(370, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_texto.setFont(font)
        self.btn_texto.setObjectName("btn_texto")

        self.btn_texto.clicked.connect(self.show_TextoInteiro)

        self.btn_creditos = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_creditos.setGeometry(QtCore.QRect(370, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_creditos.setFont(font)
        self.btn_creditos.setObjectName("btn_creditos")

        self.btn_creditos.clicked.connect(self.show_Creditos)

        self.btn_jogo = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_jogo.setGeometry(QtCore.QRect(370, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_jogo.setFont(font)
        self.btn_jogo.setObjectName("btn_jogo")
        self.btn_jogo.setText("Joguinho (créditos a\n yangshun no GitHub)")

        self.btn_jogo.clicked.connect(self.abrirJogo)

        self.btn_frases = QtWidgets.QPushButton(TelaPrincipal)
        self.btn_frases.setGeometry(QtCore.QRect(430, 300, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_frases.setFont(font)
        self.btn_frases.setObjectName("btn_frases")

        self.btn_frases.clicked.connect(self.show_Frase)

        self.label_felizaniversario = QtWidgets.QLabel(TelaPrincipal)
        self.label_felizaniversario.setGeometry(QtCore.QRect(140, 60, 271, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_felizaniversario.setFont(font)
        self.label_felizaniversario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_felizaniversario.setObjectName("label_felizaniversario")

        self.foto = QtWidgets.QLabel(TelaPrincipal)
        self.foto.setGeometry(QtCore.QRect(210, 120, 131, 151))
        self.foto.setText("")
        self.foto.setPixmap(QtGui.QPixmap("img/pinguim.png"))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")

        self.retranslateUi(TelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "Página Principal"))
        self.label_bemvindo2.setText(_translate("TelaPrincipal", "Bem-vindo!"))

        self.btn_playlist.setStatusTip(_translate("TelaPrincipal", "Abre nossa playlist num link do Spotify"))
        self.btn_playlist.setWhatsThis(_translate("TelaPrincipal", "Link da playlist"))
        self.btn_playlist.setText(_translate("TelaPrincipal", "Playlist (Spotify)"))

        self.btn_evolucao.setStatusTip(_translate("TelaPrincipal", "Abre uma janela com nossa evolução"))
        self.btn_evolucao.setWhatsThis(_translate("TelaPrincipal", "Nossa evolução"))
        self.btn_evolucao.setText(_translate("TelaPrincipal", "Evolução"))

        self.btn_album.setStatusTip(_translate("TelaPrincipal", "Abre nosso álbum num link do Google Fotos"))
        self.btn_album.setWhatsThis(_translate("TelaPrincipal", "Link do álbum"))
        self.btn_album.setText(_translate("TelaPrincipal", "Álbum (Google Fotos)"))

        self.btn_texto.setStatusTip(_translate("TelaPrincipal", "Abre uma janela com o texto do início"))
        self.btn_texto.setWhatsThis(_translate("TelaPrincipal", "Texto de aniversário"))
        self.btn_texto.setText(_translate("TelaPrincipal", "Texto do Início"))

        self.btn_jogo.setStatusTip(_translate("TelaPrincipal", "Abre um joguinho"))
        self.btn_jogo.setWhatsThis(_translate("TelaPrincipal", "Joguinho"))
        self.btn_jogo.setText(_translate("TelaPrincipal", "Joguinho"))

        self.btn_creditos.setStatusTip(_translate("TelaPrincipal", "Abre uma janela com os créditos do programa"))
        self.btn_creditos.setWhatsThis(_translate("TelaPrincipal", "Créditos"))
        self.btn_creditos.setText(_translate("TelaPrincipal", "Créditos"))

        self.btn_frases.setStatusTip(_translate("TelaPrincipal", "O que é isso?"))
        self.btn_frases.setWhatsThis(_translate("TelaPrincipal", "??"))
        self.btn_frases.setText(_translate("TelaPrincipal", "Clica aqui..."))

        self.label_felizaniversario.setText(_translate("TelaPrincipal", "Feliz Primeiro Aniversário! <3"))

#login: sasusaku
#senha: euteamo
#tudo minúsculo ;)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QDialog()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())
