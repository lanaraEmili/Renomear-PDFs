# Renomeador de PDFs

Este script em Python permite renomear arquivos PDF em uma pasta, organizando-os em **sequência numérica** a partir de um número inicial definido pelo usuário.

---

## Funcionalidades

- Lista todos os arquivos PDF de uma pasta.
- Ordena os arquivos numericamente com base nos números presentes no nome.
- Renomeia os arquivos em sequência, começando a contagem a partir de um número definido pelo usuário.
- Gera nomes padronizados com prefixo, por exemplo: `NF 16545.pdf`, `NF 16546.pdf`, etc.

---

## Requisitos

- Python 3.x
- Sistema operacional: Windows, macOS ou Linux
- Biblioteca padrão do Python (`os`, `re`) — não precisa instalar nada adicional.

---

## Como usar

1. Coloque o script na mesma pasta onde estão os PDFs **ou modifique o caminho** no código:
   ```python
   pasta = r"C:\caminho\da\pasta"  # Altere para o caminho desejado

2. Abra o **terminal** ou **PowerShell** na pasta do script.

3. Execute o script:
   ```python
   python renomear_pdf.py


5. Os PDFs serão renomeados em sequência numérica.

Exemplo
Antes:
 ```python
  NF 1.pdf
  NF 2.pdf
  NF 10.pdf
  NF 3.pdf

  ```

Depois: (contador inicial = 16545)
  ```python
  NF 16545.pdf
  NF 16546.pdf
  NF 16547.pdf
  NF 16548.pdf
