import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
print(caminho) 
#   askdirectory pede ao usuário para selecionar uma pasta

lista_arquivos = os.listdir(caminho)
#   vai listar todos os arquivos da pasta que foi selecionada
print(lista_arquivos)

locais = {
    "imagens": [".png, ", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "docs": [".docx"]
}

#   "docs" = é o nome atribuído a pasta criada para os arquivos com .docx

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")