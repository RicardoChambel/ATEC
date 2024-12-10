import tkinter as tk
from tkinter import messagebox
import sqlite3

db_name = "users.db"
largura = 500
altura = 250

def setupDatabase():
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilizadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT UNIQUE NOT NULL,
        password INTEGER NOT NULL,
        nome TEXT,
        apelido TEXT,
        codigo_postal TEXT,
        telemovel TEXT,
        email TEXT
    )
    """)
    con.commit()
    con.close()

setupDatabase()

# Funções -------------------------------------------
def login():
    user = entry_user.get()
    password = entry_password.get()

    if (not user.isalpha()) and user:
        messagebox.showerror("Erro", "O utilizador só pode ter letras!")
        return
    if (not password.isdigit()) and password:
        print("-", password, "-")
        print("Tipo da password inserida: ", type(password))
        messagebox.showerror("Erro", "A password só pode ter numeros!")
        return

    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM utilizadores WHERE user = ? AND password = ?", (user, password))
    resultado = cursor.fetchone()
    con.close()

    if resultado!=None:
        janela_login.destroy()
        registo()

def criarUser():
    user = entry_user_registo.get()
    password = entry_password_registo.get()
    nome = entry_nome.get()
    apelido = entry_apelido.get()
    codigo_postal = entry_codigo_postal.get()
    telemovel = entry_telemovel.get()
    email = entry_email.get()

    if not user.isalpha():
        messagebox.showerror("Erro", "O utilizador só pode ter letras!")
        return
    if not password.isdigit():
        messagebox.showerror("Erro", "A password só pode ter números!")
        return
    if len(codigo_postal.split("-")) != 2 or not all(part.isdigit() for part in codigo_postal.split("-")):
        messagebox.showerror("Erro", "O código postal deve estar no formato 0000-000.")
        return
    if len(telemovel) != 9 or not telemovel.isdigit():
        messagebox.showerror("Erro", "O telemóvel deve ter exatamente 9 dígitos!")
        return

    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    try:
        cursor.execute("""
        INSERT INTO utilizadores (user, password, nome, apelido, codigo_postal, telemovel, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user, password, nome, apelido, codigo_postal, telemovel, email))
        con.commit()
        messagebox.showinfo("Sucesso", "Utilizador criado com sucesso!")
    except IOError:
        messagebox.showerror("Erro", f"Erro: {IOError}")
    con.close()

def atualizarUser():
    user = entry_user_registo.get()
    password = entry_password_registo.get()
    nome = entry_nome.get()
    apelido = entry_apelido.get()
    codigo_postal = entry_codigo_postal.get()
    telemovel = entry_telemovel.get()
    email = entry_email.get()

    if not user.isalpha():
        messagebox.showerror("Erro", "Utilizador inválido!")
        return

    if not password.isdigit():
        messagebox.showerror("Erro", "A password só pode ter números!")
        return

    if len(codigo_postal.split("-")) != 2 or not all(part.isdigit() for part in codigo_postal.split("-")):
        messagebox.showerror("Erro", "O código postal deve estar no formato 0000-000.")
        return

    if len(telemovel) != 9 or not telemovel.isdigit():
        messagebox.showerror("Erro", "O telemóvel deve ter exatamente 9 dígitos!")
        return

    try:
        con = sqlite3.connect(db_name)
        cursor = con.cursor()

        cursor.execute("""
        UPDATE utilizadores
        SET password = ?, nome = ?, apelido = ?, codigo_postal = ?, telemovel = ?, email = ?
        WHERE user = ?
        """, (password, nome, apelido, codigo_postal, telemovel, email, user))

        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Sucesso", "Utilizador atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Utilizador não encontrado!")

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao atualizar utilizador: {e}")
    finally:
        con.close()

def registo():
    global entry_user_registo, entry_password_registo, entry_nome, entry_apelido, entry_codigo_postal, entry_telemovel, entry_email

    janela_registo = tk.Tk()
    janela_registo.title("Registo")
    janela_registo.iconbitmap("icon.ico")
    x = (janela_registo.winfo_screenwidth()-largura)//2
    y = (janela_registo.winfo_screenheight()-altura)//2
    janela_registo.geometry(f"{largura}x{altura}+{x}+{y}")

    # LABELS E INPUT ------
    tk.Label(janela_registo, text="Utilizador:").grid(row=0, column=0)
    entry_user_registo = tk.Entry(janela_registo)
    entry_user_registo.grid(row=0, column=1)

    tk.Label(janela_registo, text="Password:").grid(row=1, column=0)
    entry_password_registo = tk.Entry(janela_registo)
    entry_password_registo.grid(row=1, column=1)

    tk.Label(janela_registo, text="Nome:").grid(row=2, column=0)
    entry_nome = tk.Entry(janela_registo)
    entry_nome.grid(row=2, column=1)

    tk.Label(janela_registo, text="Apelido:").grid(row=3, column=0)
    entry_apelido = tk.Entry(janela_registo)
    entry_apelido.grid(row=3, column=1)

    tk.Label(janela_registo, text="Código Postal (0000-000):").grid(row=4, column=0)
    entry_codigo_postal = tk.Entry(janela_registo)
    entry_codigo_postal.grid(row=4, column=1)

    tk.Label(janela_registo, text="Telemóvel:").grid(row=5, column=0)
    entry_telemovel = tk.Entry(janela_registo)
    entry_telemovel.grid(row=5, column=1)

    tk.Label(janela_registo, text="Email:").grid(row=6, column=0)
    entry_email = tk.Entry(janela_registo)
    entry_email.grid(row=6, column=1)
    
    # LISTA DE UTILIZADORES -----
    tk.Label(janela_registo, text="Utilizadores na database:").grid(row=0, column=2, padx=10, pady=5)
    listbox_utilizadores = tk.Listbox(janela_registo, height=10, width=30)
    listbox_utilizadores.grid(row=1, column=2, rowspan=6, padx=10, pady=5)

    def atualizarListaUtilizadores():
        # LIMPAR A LISTA QUE ESTÁ LÁ
        listbox_utilizadores.delete(0, tk.END)
        
        try:
            con = sqlite3.connect(db_name)
            cursor = con.cursor()
            cursor.execute("SELECT user FROM utilizadores")
            utilizadores = cursor.fetchall()

            # ADICIONAR CADA UTILIZADOR À LISTA
            for utilizador in utilizadores:
                listbox_utilizadores.insert(tk.END, utilizador[0])

            con.close()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao carregar utilizadores: {e}")

    # ATUALIZAR A LISTA AO INICIAR A JANELA
    atualizarListaUtilizadores()

    # BOTÕES -----
    tk.Button(janela_registo, text="Criar", command=criarUser).grid(row=7, column=0)
    tk.Button(janela_registo, text="Atualizar", command=atualizarUser).grid(row=7, column=1)
    tk.Button(janela_registo, text="Fechar", command=janela_registo.destroy).grid(row=7, column=2)


    janela_registo.mainloop()

def abrir_registo():
    janela_login.destroy()
    registo()

while True:
    # JANELA PRINCIPAL DO LOGIN ---------- 
    janela_login = tk.Tk()
    janela_login.title("Login")
    janela_login.iconbitmap("icon.ico")
    x = (janela_login.winfo_screenwidth()-largura)//2
    y = (janela_login.winfo_screenheight()-altura)//2
    janela_login.geometry(f"{largura}x{altura}+{x}+{y}")

    tk.Label(janela_login, text="Utilizador:").grid(row=0, column=0)
    entry_user = tk.Entry(janela_login)
    entry_user.grid(row=0, column=1)

    tk.Label(janela_login, text="Password:").grid(row=1, column=0)
    entry_password = tk.Entry(janela_login, show="*")
    entry_password.grid(row=1, column=1)

    # AQUI FIZ UMA LISTA PARA MOSTRAR OS UTILIZADORES QUE ESTÃO NA BASE DE DADOS
    tk.Label(janela_login, text="Utilizadores na database:").grid(row=0, column=2, padx=10, pady=5)
    listbox_utilizadores = tk.Listbox(janela_login, height=10, width=30)
    listbox_utilizadores.grid(row=1, column=2, rowspan=6, padx=10, pady=5)

    try:
        con = sqlite3.connect(db_name)
        cursor = con.cursor()
        cursor.execute("SELECT user, password FROM utilizadores")
        utilizadores = cursor.fetchall()

        for utilizador in utilizadores:
            listbox_utilizadores.insert(tk.END, f"Utilizador: {utilizador[0]} - Password: {utilizador[1]}")

        con.close()
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao carregar utilizadores: {e}")

    def sair():
        exit(0)

    tk.Button(janela_login, text="Login", command=login).grid(row=2, column=0, columnspan=2)
    tk.Button(janela_login, text="Criar conta", command=abrir_registo).grid(row=3, column=0, columnspan=2)
    tk.Button(janela_login, text="Sair", command=sair).grid(row=4, column=0, columnspan=2)

    janela_login.mainloop()
