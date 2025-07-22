import tkinter as tk
from tkinter import messagebox, simpledialog
from database import criar_tabela, inserir_usuario, listar_usuarios

# Cria a tabela se não existir
criar_tabela()

ADMIN_SENHA = "admin123"  # senha do administrador

def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    
    if nome.strip() == "" or email.strip() == "":
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
        return

    inserir_usuario(nome, email)
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def mostrar_usuarios():
    senha = simpledialog.askstring("Senha de Admin", "Digite a senha do administrador:", show='*')
    if senha != ADMIN_SENHA:
        messagebox.showerror("Erro", "Senha incorreta!")
        return

    usuarios = listar_usuarios()
    if not usuarios:
        messagebox.showinfo("Usuários", "Nenhum usuário cadastrado.")
        return

    janela = tk.Toplevel(root)
    janela.title("Usuários Cadastrados")
    janela.geometry("400x300")

    listbox = tk.Listbox(janela, width=50, height=15)
    listbox.pack(pady=10)

    for nome, email in usuarios:
        listbox.insert(tk.END, f"{nome} - {email}")

# Interface Tkinter
root = tk.Tk()
root.title("Cadastro de Usuários")
root.geometry("350x300")

tk.Label(root, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(root, width=30)
entry_nome.pack()

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack()

btn_salvar = tk.Button(root, text="Salvar", command=salvar)
btn_salvar.pack(pady=10)

btn_ver_usuarios = tk.Button(root, text="Ver Usuários (Admin)", command=mostrar_usuarios)
btn_ver_usuarios.pack(pady=10)

root.mainloop()