"""
Renomeador de PDFs
=================

Renomeia todos os arquivos PDF de uma pasta em sequência numérica
com prefixo definido pelo usuário. Ordena numericamente baseado nos números
presentes nos nomes originais e permite começar a contagem em qualquer valor.

Requisitos:
- Python 3.x
- Bibliotecas padrão: os, re

Autor: Emily Pereira
"""

import os
import re

# CONFIGURAÇÕES
pasta = r"C:\caminho\da\pasta"              # Pasta com PDFs
prefixo = "NF "                             # Prefixo dos arquivos
contador_inicial = 16545                    # Número inicial da sequência
zeros = 5                                   # Dígitos com zero à esquerda

def renomear_pdfs(pasta, prefixo, contador_inicial, zeros=0):
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")]

    if not arquivos:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return

    arquivos_ordenados = sorted(
        arquivos,
        key=lambda x: int(re.search(r'\d+', x).group())
    )

    for i, nome_arquivo in enumerate(arquivos_ordenados, start=contador_inicial):
        novo_nome = f"{prefixo}{i:0{zeros}d}.pdf" if zeros > 0 else f"{prefixo}{i}.pdf"
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)

        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {nome_arquivo} → {novo_nome}")
        except PermissionError:
            print(f"⚠ Arquivo em uso, não renomeado: {nome_arquivo}")
        except Exception as e:
            print(f"⚠ Erro ao renomear {nome_arquivo}: {e}")

    print("Processo de renomeação concluído.")

if __name__ == "__main__":
    renomear_pdfs(pasta, prefixo, contador_inicial, zeros)
