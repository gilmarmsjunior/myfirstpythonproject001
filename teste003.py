import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# Cria a aplicação
app = QApplication(sys.argv)

# Cria a janela (QWidget é um widget em branco que serve como janela)
janela = QWidget()
janela.setWindowTitle("Minha Janela PyQt")
janela.setGeometry(100, 100, 400, 100) # (pos_x, pos_y, largura, altura)

# Cria um rótulo e o posiciona na janela
rotulo = QLabel("Olá, Mundo com PyQt6!", parent=janela)
rotulo.move(120, 40) # (pos_x, pos_y) dentro da janela

# Mostra a janela
janela.show()

# Inicia o loop da aplicação
sys.exit(app.exec())