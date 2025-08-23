import os
import re

pasta = r"C:\caminho\da\pasta"

# Lista apenas arquivos PDF
arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")]

# Ordena extraindo o número do nome
arquivos_ordenados = sorted(
    arquivos,
    key=lambda x: int(re.search(r'\d+', x).group())
)

# Renomeia em ordem numérica começando do 16455
contador_inicial = 16545

for i, nome_arquivo in enumerate(arquivos_ordenados, start=contador_inicial):
    novo_nome = f"NF {i}.pdf"  # vai gerar NF 16455, NF 16456, ...
    caminho_antigo = os.path.join(pasta, nome_arquivo)
    caminho_novo = os.path.join(pasta, novo_nome)
    os.rename(caminho_antigo, caminho_novo)

print("Arquivos renomeados com sucesso!")
