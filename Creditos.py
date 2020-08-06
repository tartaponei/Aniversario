# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Creditos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaCreditos(object):
    def setupUi(self, TelaCreditos):
        TelaCreditos.setObjectName("TelaCreditos")
        TelaCreditos.resize(571, 492)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaCreditos.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaCreditos)
        self.label.setGeometry(QtCore.QRect(20, 10, 531, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(TelaCreditos)
        QtCore.QMetaObject.connectSlotsByName(TelaCreditos)

    def retranslateUi(self, TelaCreditos):
        _translate = QtCore.QCoreApplication.translate
        TelaCreditos.setWindowTitle(_translate("TelaCreditos", "Créditos"))
        self.label.setText(_translate("TelaCreditos", "Isso não é um TCC mas é um projeto então vai ter agradecimentos mesmo, risos. Só pelo fato de ter um banco de dados eu já considero um projeto enorme, odeio mexer com isso.\n"
"\n"
"Primeiramente obrigada aos meus professores de programação do CP2 por despertarem em mim o amor, que hoje é bem maior que na época, pela área da informática e por me darem toda a base. Chico e Flávia principalmente.\n"
"\n"
"Obrigada ao Tim do canal Tech With Tim pelos seus tutoriais incríveis de PyQt5 muito bem explicados que me deram a base pra esse código.\n"
"Obrigada ao Ajay do canal Ssj6 por ter sido o único que eu achei que fez um vídeo completo sobre navegação entre páginas, junto com um sistema de login com banco de dados.\n"
"\n"
"Obrigada à Claudia pelo apoio moral e pelas dicas de apps e etc pra facilitar meu trabalho. Você sempre tem umas cartas na manga.\n"
"Obrigada ao Bruno por ter aguentado minhas mensagens infinitas com minhas dúvidas idiotas e por estar disposto a me ajudar apesar da minha chatice.\n"
"Obrigada à Carina pelo apoio moral e pela ajuda com as frases.\n"
"Na questão de apoio moral, agradeço também ao próprio Jonathan, que não sabia o propósito disso mas me dava apoio mesmo assim.\n"
"Obrigada támbém à Nayure, de tão longe sempre me dando apoio moral também, e por ter me dado algumas ideias pra esse projeto.\n"
"\n"
"E obrigada principalmente ao Jonathan. Você foi a minha maior motivação pra estudar o PyQt5 e todas as questões sobre interface (coisa que não é a minha praia). Fazer as coisas pra você aumenta minha motivação pelo menos umas 5x. Obrigada por me motivar e ser um exemplo.\n"
"\n"
"Créditos a /yangshun pelo jogo do 2048."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCreditos = QtWidgets.QDialog()
    ui = Ui_TelaCreditos()
    ui.setupUi(TelaCreditos)
    TelaCreditos.show()
    sys.exit(app.exec_())
