import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela")

# Cria um rótulo (label) com o texto
rotulo = tk.Label(janela, text="Olá, Mundo! Esta é minha primeira interface gráfica!")
rotulo.pack(padx=20, pady=20) # .pack() "empacota" o widget na janela

# Inicia o loop principal da aplicação (deixa a janela aberta)
janela.mainloop()