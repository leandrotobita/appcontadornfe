from PIL import Image, ImageTk
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog

# Namespace
ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

# Função para extrair e somar a coluna qCom
def somar_qcom(xml_content):
    tree = ET.ElementTree(ET.fromstring(xml_content))
    soma_qcom = 0.0

    for det in tree.iterfind('.//nfe:det', namespaces=ns):
        qcom = det.find('.//nfe:qCom', namespaces=ns)
        if qcom is not None and qcom.text is not None:
            soma_qcom += float(qcom.text)

    return soma_qcom

# Função para obter o arquivo XML
def obter_arquivo_xml():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo XML", filetypes=[("Arquivos XML", "*.xml")])
    if caminho_arquivo:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        # Chama a função para obter a soma da coluna qCom
        soma_qcom = somar_qcom(xml_content)

        # Exibe o resultado
        resultado_label.config(text=f'A soma da coluna qCom é: {soma_qcom}')

# Criar janela
root = tk.Tk()
root.title("Contador de Produtos XML")
root.geometry("400x160")  # Definir largura e altura da janela

# Converter e carregar a imagem
imagem = Image.open("topo.jpg")
imagem = imagem.resize((400, 60))  # Redimensionar a imagem para 400x60px
imagem = ImageTk.PhotoImage(imagem)

# Adicionar imagem ao topo da janela
imagem_label = tk.Label(root, image=imagem)
imagem_label.pack()

# Botão para obter o arquivo XML
obter_arquivo_button = tk.Button(root, text="Obter Arquivo XML", command=obter_arquivo_xml)
obter_arquivo_button.pack(pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()

