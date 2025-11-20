import PyPDF2
import os #     sistema operacional

merger = PyPDF2.PdfMerger()
listar_arquivos = os.listdir("automacao") 
#    lista diretório

for arquivo in listar_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"automacao/{arquivo}") 
#   .append() para inserir dentro do vetor

merger.write("apostilas_mescladas.pdf") 
#  executa a ação de juntar e salvar os arquivos em um único arquivo de saída.
