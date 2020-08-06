# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextoInteiro.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaTextoInteiro(object):
    def setupUi(self, TelaTextoInteiro):
        TelaTextoInteiro.setObjectName("TelaTextoInteiro")
        TelaTextoInteiro.resize(902, 761)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaTextoInteiro.setWindowIcon(icon)

        self.label_texto = QtWidgets.QLabel(TelaTextoInteiro)
        self.label_texto.setGeometry(QtCore.QRect(10, 10, 881, 741))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_texto.setFont(font)
        self.label_texto.setScaledContents(False)
        self.label_texto.setWordWrap(True)
        self.label_texto.setObjectName("label_texto")

        self.retranslateUi(TelaTextoInteiro)
        QtCore.QMetaObject.connectSlotsByName(TelaTextoInteiro)

    def retranslateUi(self, TelaTextoInteiro):
        _translate = QtCore.QCoreApplication.translate
        TelaTextoInteiro.setWindowTitle(_translate("TelaTextoInteiro", "Texto"))
        self.label_texto.setText(_translate("TelaTextoInteiro", "Oi :) Você deve estar se perguntando o que é isso.\n"
"\n"
"E eu te respondo: é um programa nosso! Nele você vai poder ter acesso a várias coisas legais sobre a gente como um casal.\n"
"\n"
"Quando eu disse que tinha começado a estudar uma coisa nova em Python, era pra isso. Pra fazer isso pra você.\n"
"\n"
"E, bom, você já deve estar acostumado com os meus textos e cartinhas clichês, mas não consigo evitar. Sempre tenho muito o que dizer pra você.\n"
"\n"
"Não sei bem por onde começar. Eu realmente não esperava que você fosse fazer parte da minha vida. Quando eu te conheci e conversamos pelo Whatsapp a primeira vez, eu realmente achei que seria só aquela vez, que você seria mais um dos contatos que eu teria de coleção, só pra verem meus status, nada mais.\n"
"\n"
"Até hoje eu não sei o que deu na minha cabeça pra te chamar pra conversar no dia em que decidimos passar a conversar o dia todo. Penso que era pra ter sido assim desde o início. E é isso o que me motivou a não terminar com você nas vezes eu que considerei isso, e eu não me arrependo. Não mesmo.\n"
"\n"
"E eu também sou grata por você também não ter terminado. Eu sempre falo isso, mas eu sempre penso nas merdas que já te fiz e é muito difícil deixar elas irem embora, mas eu tô tentando. Desculpa por todas elas. E como eu sempre digo, tô me esforçando pra melhorar isso tudo. Você me faz querer mudar isso tudo. Por você, vale a pena mudar certas coisas. Minha inveja, meu egoísmo, meu individualismo. Vale a pena.\n"
"\n"
"Você além de meu namorado é o meu melhor amigo, sempre. É o primeiro que eu busco quando eu tô feliz, quando eu tô triste e quero desabafar com alguém, quando eu tô precisando de ajuda em qualquer coisa, quando tô com uma ideia nova, quando quero começar um projeto. É sempre você, apesar dos apesares. Mesmo você sendo meio insensível ou algo do tipo às vezes.\n"
"\n"
"E eu não canso de falar que você despertou uma versão melhor de mim. Não é a melhor de todas porque ainda tenho muita coisa pra mudar e repensar, mas você tá despertando isso aos poucos. E, mesmo a minha parte lógica achando isso uma coisa errada, eu realmente não consigo mais me ver sem você do meu lado. E vou aprender a administrar esse sentimento.\n"
"\n"
"Passou tão rápido. Parece que foi ontem que você foi na Rural e me pediu em namoro no lago das capivaras. Parece que foi ontem que beijamos a primeira vez. Parece que foi ontem que a gente foi no cinema a primeira vez. E ao mesmo tempo parece que faz tanto tempo, que tenho essa conexão com você há muitos anos. Eu realmente espero que dure por muitos anos, isso só demanda esforço dos dois lados.\n"
"\n"
"Ninguém é perfeito, e precisamos de esforço pra nos deixar menos defeituosos do que somos. Do mesmo jeito que eu já te machuquei várias vezes, você também já me machucou várias. Mas a gente aprende com o tempo, e sempre renovamos o que sentimos. E isso faz parte do esforço que disse antes, se já não é ele inteiro.\n"
"\n"
"Às vezes não parece real. Mas é, e sou grata todos os dias por ter alguém como você na minha vida. Eu não sei mais no que eu acredito, mas se algo guiou a gente então eu sou totalmente grata a esse algo.\n"
"\n"
"Obrigada por me dar apoio sempre nos meus maiores problemas, por sempre estar disposto a me ajudar, por ver coisas boas em mim, por insistir e não desistir de mim em todos os sentidos. Por sempre separar um tempinho pra mim quando você tá ocupado com seu futuro, e por me incluir nele em alguns de seus planos. Por estar me ensinando lições valiosas desde os nossos primeiros dias, e por ter virado a minha vida de cabeça pra cima. É, pra cima. Obrigada por sempre estar disposto a me oferecer seu abraço quente quando preciso me aquecer, e por me dar toques frios quando preciso esfriar. Obrigada por iluminar meus dias. Obrigada por tudo.\n"
"\n"
"Você a pessoa mais inteligente e incrível que eu já conheci. Sua beleza veio de bônus rs. Espero que eu seja importante pra você ao menos metade do que você é pra mim.\n"
"\n"
"Feliz 1 ano de namoro. Eu realmente espero que continuemos juntos por mais um tempinho. Ok, tempão, rs. \n"
"\n"
"Eu te amo muito. Mesmo quando não parecer, eu te amo muito. E nunca duvide disso."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaTextoInteiro = QtWidgets.QDialog()
    ui = Ui_TelaTextoInteiro()
    ui.setupUi(TelaTextoInteiro)
    TelaTextoInteiro.show()
    sys.exit(app.exec_())
