import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox


def renomear_pdfs(pasta, contador_inicial):
    padrao_numero = re.compile(r'\d+')
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")]

    def extrai_numero(nome):
        match = padrao_numero.search(nome)
        return int(match.group()) if match else float('inf')

    arquivos_ordenados = sorted(arquivos, key=extrai_numero)

    erros = 0
    for i, nome_arquivo in enumerate(arquivos_ordenados, start=contador_inicial):
        novo_nome = f"NF {i}.pdf"
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        if os.path.exists(caminho_novo):
            erros += 1
            continue
        try:
            os.rename(caminho_antigo, caminho_novo)
        except Exception:
            erros += 1
    return len(arquivos_ordenados) - erros, erros


def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta.delete(0, tk.END)
        entry_pasta.insert(0, pasta)


def executar():
    pasta = entry_pasta.get()
    try:
        contador = int(entry_contador.get())
    except ValueError:
        messagebox.showerror("Erro", "Número inicial inválido!")
        return
    if not os.path.isdir(pasta):
        messagebox.showerror("Erro", "Pasta inválida!")
        return
    renomeados, erros = renomear_pdfs(pasta, contador)
    messagebox.showinfo(
        "Concluído", f"{renomeados} arquivos renomeados!\n{erros} erros.")


root = tk.Tk()
root.title("Renomear PDFs")

tk.Label(root, text="Pasta:").grid(row=0, column=0, sticky="e")
entry_pasta = tk.Entry(root, width=40)
entry_pasta.grid(row=0, column=1)
tk.Button(root, text="Selecionar",
          command=selecionar_pasta).grid(row=0, column=2)

tk.Label(root, text="Número inicial:").grid(row=1, column=0, sticky="e")
entry_contador = tk.Entry(root, width=10)
entry_contador.grid(row=1, column=1, sticky="w")
entry_contador.insert(0, "16545")

tk.Button(root, text="Renomear", command=executar).grid(
    row=2, column=1, pady=10)

root.mainloop()
