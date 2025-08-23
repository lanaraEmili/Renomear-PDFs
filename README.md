# 📄 Renomeador de PDFs

Um **script em Python** para renomear arquivos PDF em uma pasta, organizando-os em **sequência numérica** a partir de um número inicial definido pelo usuário.  

![Python Logo](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white) ![File PDF](https://img.shields.io/badge/Tipo-PDF-red) 
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)

---


## ⚡ Funcionalidades

- 📂 Lista todos os PDFs de uma pasta.  
- 🔢 Ordena numericamente pelo número presente no nome.  
- 📝 Renomeia os arquivos com prefixo definido e sequência numérica.  
- 0️⃣ Suporta números com **zeros à esquerda**.  
- ⚠️ Evita erros se arquivos estiverem abertos, mostrando alerta no terminal.

---

## 🛠️ Requisitos

- Python 3.x  
- Bibliotecas padrão: `os`, `re`  

---

## 🚀 Como usar

1. Coloque o script na mesma pasta onde estão os PDFs **ou modifique o caminho** no código:
   ```python
   pasta = r"C:\caminho\da\pasta"  # Altere para o caminho desejado

2. Abra o **terminal** ou **PowerShell** na pasta do script.

3. Execute o script:
   ```python
   python renomear_pdf.py


5. Os PDFs serão renomeados em sequência numérica.

🔄 Exemplo de Entrada e Saída

Antes:
 ```
NF 1.pdf
NF 2.pdf
NF 10.pdf
NF 3.pdf
  ```      
Depois:
 ```      
 NF 16545.pdf
 NF 16546.pdf
 NF 16547.pdf
 NF 16548.pdf
 ```

---

## ⚙️ Configurações

Prefixo dos arquivos:

```prefixo = "NF " ```

Número inicial da sequência:

``contador_inicial = 16545``

Zeros à esquerda (opcional):

``novo_nome = f"{prefixo}{i:05}.pdf"``

---

## 📝 Observações

Feche todos os PDFs antes de executar.

Arquivos em uso podem gerar PermissionError.

Pode ser adaptado para gerar logs ou ignorar arquivos em uso.


---
