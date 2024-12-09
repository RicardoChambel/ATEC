import tkinter as tk
from tkinter import messagebox

print("\n---INFO DO PROGRAMA---\n")

def janela_1():
    # Criar a janela utilizando a class (objeto) ----------------------------
    janela = tk.Tk()

    # Definir o tamanho da janela e centrar a janela no ecrã ----------------------------
    largura = 800 # --> l = Largura
    altura = 600 # --> a = Altura
    larguraEcra = janela.winfo_screenwidth()
    alturaEcra = janela.winfo_screenheight()
    posicao_x = (larguraEcra-largura)//2
    posicao_y = (alturaEcra-altura)//2

    print("Largura do ecrã -> ",larguraEcra)
    print("Altura do ecrã -> ",alturaEcra)

    # Variavel com a posição desejada do ecrã ----------------------------
    # Formato da posição: ( LarguraJanela x AlturaJanela + PosiçãoX + PosiçãoY )
    posicao = f"{largura}x{altura}+{posicao_x}+{posicao_y}"
    janela.geometry(posicao)

    # Definir o fundo da janela ----------------------------
    janela.config(bg="lightgray")

    # Definir o titulo da janela ----------------------------
    janela.title("Novo Programa")

    # Iniciar a janela ----------------------------
    print("\n")
    janela.mainloop()

def janela_2():
    # Criar a janela de login
    window = tk.Tk()

    # Definir as dimensões da janela
    w = 300  # largura
    h = 200  # altura
    ws = window.winfo_screenwidth()  # largura da tela
    hs = window.winfo_screenheight()  # altura da tela

    # Calcular a posição para centralizar a janela
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # Definir as configurações da janela
    window.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    window.configure(bg="lightgray")  # Cor de fundo cinza claro
    window.title("Frames")
    window.iconbitmap('icon.ico')

    # Adicionar um frame para o conteúdo
    frame = tk.Frame(window, bg="lightgray")
    frame.pack(pady=10, padx=10, expand=True)

    # Adicionar texto e campos de entrada
    tk.Label(frame, text="Username:", bg="lightgray", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    username_entry = tk.Entry(frame, font=("Arial", 10))
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Password:", bg="lightgray", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = tk.Entry(frame, show="*", font=("Arial", 10))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Função de login
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "ATEC" and password == "PI0923":
            messagebox.showinfo("Success", "Bem-vindo rei!")
            window.destroy()  # Fechar a janela após o login
        else:
            username_entry.delete(0, tk.END)  # Limpar o campo de username
            password_entry.delete(0, tk.END)  # Limpar o campo de senha

    # Adicionar o botão de login
    login_button = tk.Button(frame, text="Login", command=login, font=("Arial", 10), bg="lightgrey", width=10)
    login_button.grid(row=2, columnspan=2, pady=10)

    # Iniciar janela
    window.mainloop()

janela_1()
janela_2()
