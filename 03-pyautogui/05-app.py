import tkinter as tk
from tkinter import ttk

def add_student(name, email):
    """Adiciona um aluno à tabela."""
    if name and email:
        tree.insert("", "end", values=(name, email))
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        print("Por favor, preencha ambos os campos: Nome e Email.")

root = tk.Tk()
root.title("Cadastro de Alunos")

tree = ttk.Treeview(root, columns=("Nome", "Email"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Email", text="Email")

tree.pack()

label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=(10, 0))  
entry_email = tk.Entry(root)
entry_email.pack(pady=(0, 10))


button_add = tk.Button(root, text="Adicionar", command=lambda: add_student(entry_nome.get(), entry_email.get()))
button_add.pack()

root.mainloop()

#1585, 286 1582, 341 1603, 375