import tkinter as tk
from tkinter import messagebox
import sqlite3

# Configuração da Base de Dados
db_name = "usuarios.db"

def setup_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
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
    conn.commit()
    conn.close()

setup_database()

# Funções
def login():
    user = entry_user.get()
    password = entry_password.get()

    if not user.isalpha():
        messagebox.showerror("Erro", "O utilizador só pode conter letras.")
        return
    if not password.isdigit():
        messagebox.showerror("Erro", "A password só pode conter números.")
        return

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE user = ? AND password = ?", (user, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
        janela_login.destroy()
        registo()
    else:
        messagebox.showerror("Erro", "Utilizador ou password incorretos.")

def criar_user():
    user = entry_user_registo.get()
    password = entry_password_registo.get()
    nome = entry_nome.get()
    apelido = entry_apelido.get()
    codigo_postal = entry_codigo_postal.get()
    telemovel = entry_telemovel.get()
    email = entry_email.get()

    if not user.isalpha():
        messagebox.showerror("Erro", "O utilizador só pode conter letras.")
        return
    if not password.isdigit():
        messagebox.showerror("Erro", "A password só pode conter números.")
        return
    if len(codigo_postal.split("-")) != 2 or not all(part.isdigit() for part in codigo_postal.split("-")):
        messagebox.showerror("Erro", "O código postal deve estar no formato CP4-CP3.")
        return
    if len(telemovel) != 9 or not telemovel.isdigit():
        messagebox.showerror("Erro", "O telemóvel deve conter exatamente 9 dígitos.")
        return

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO usuarios (user, password, nome, apelido, codigo_postal, telemovel, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user, password, nome, apelido, codigo_postal, telemovel, email))
        conn.commit()
        messagebox.showinfo("Sucesso", "Utilizador criado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "O utilizador já existe.")
    conn.close()

def registo():
    janela_registo = tk.Tk()
    janela_registo.title("Registo")

    # Formulário de Registo
    global entry_user_registo, entry_password_registo, entry_nome, entry_apelido, entry_codigo_postal, entry_telemovel, entry_email

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

    tk.Label(janela_registo, text="Código Postal (CP4-CP3):").grid(row=4, column=0)
    entry_codigo_postal = tk.Entry(janela_registo)
    entry_codigo_postal.grid(row=4, column=1)

    tk.Label(janela_registo, text="Telemóvel:").grid(row=5, column=0)
    entry_telemovel = tk.Entry(janela_registo)
    entry_telemovel.grid(row=5, column=1)

    tk.Label(janela_registo, text="Email:").grid(row=6, column=0)
    entry_email = tk.Entry(janela_registo)
    entry_email.grid(row=6, column=1)

    # Botões
    tk.Button(janela_registo, text="Criar", command=criar_user).grid(row=7, column=0)
    tk.Button(janela_registo, text="Fechar", command=janela_registo.destroy).grid(row=7, column=1)

    janela_registo.mainloop()

# Interface de Login
janela_login = tk.Tk()
janela_login.title("Login")

tk.Label(janela_login, text="Utilizador:").grid(row=0, column=0)
entry_user = tk.Entry(janela_login)
entry_user.grid(row=0, column=1)

tk.Label(janela_login, text="Password:").grid(row=1, column=0)
entry_password = tk.Entry(janela_login, show="*")
entry_password.grid(row=1, column=1)

tk.Button(janela_login, text="Login", command=login).grid(row=2, column=0, columnspan=2)

# Adicionar opção para registo
def abrir_registo():
    janela_login.destroy()
    registo()

tk.Button(janela_login, text="Criar conta", command=abrir_registo).grid(row=3, column=0, columnspan=2)

janela_login.mainloop()
