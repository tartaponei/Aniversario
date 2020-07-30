from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow): #MyWindow terá as mesmas propriedades de QMainWindow, mas posso mudar certas coisas
    #obs: estudar POO em python pqnão entendi nada
    def __init__(self):
        super(MyWindow, self).__init__()
        #usa uma instância da própria classe ao invés da janela criada (lá embaixo tem ex)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("yay")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("teste")
        self.label.move(50, 50)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("clica ae")
        self.btn1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("botão clicado aaaaaaaaaa")
        self.update()

    #ajustar tamanho do label quando algo mudar
    def update(self):
        self.label.adjustSize()

#========================================
"""
#função pra quando não usa classe:
def clicked():
    print("clicado")
"""

def window():
    #não entendi bem oq faz, mas tem a ver com pegar as configurações do sistema operacional
    app = QApplication(sys.argv)
    win = MyWindow()

    """
    #código pra quando não usa classe:
    win = QMainWindow() #janela de nome 'win'

    #dimensões da janela: win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("yay") #título da janela

    #label: QtWidgets.Qlabel(janela_onde_vai_aparecer)
    label = QtWidgets.QLabel(win)
    label.setText("teste") #texto do label
    label.move(50, 50) #posição

    #botão: mesma lógica do label
    btn1 = QtWidgets.QPushButton(win)
    btn1.setText("clica ae")
    btn1.clicked.connect(clicked) #função clicked sem () pq tô atribuindo a função ao botão, e não chamando ela
    """
    win.show() #mostra a janela
    sys.exit(app.exec_()) #encerra quando clica no x

window()
