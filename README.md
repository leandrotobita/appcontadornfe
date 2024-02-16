# Contador de Produtos XML
<img src="topo.jpg" >

## Estudo de Caso: Desenvolvimento do Contador de Produtos XML

### Contexto:

Diante da necessidade de lidar com a contagem de produtos em arquivos XML de Nota Fiscal Eletrônica (NF-e), identificamos a oportunidade de criar uma solução automatizada para calcular a soma da coluna qCom. Isso se mostrou essencial para agilizar o processo de verificação de mercadorias, especialmente em casos onde não havia o campo de quantidade total nas notas fiscais.

### Processo de Pensamento:

* Análise da Necessidade: Inicialmente, examinamos os desafios enfrentados ao lidar com grandes volumes de mercadorias e a dependência de contagens manuais de linhas em arquivos XML de NF-e.

* Identificação de Requisitos: Definimos os requisitos essenciais para o Contador de Produtos XML, incluindo a capacidade de selecionar arquivos XML, calcular a soma da coluna qCom e exibir o resultado ao usuário.

* Seleção de Tecnologias: Optamos por utilizar Python para o desenvolvimento do aplicativo devido à sua versatilidade e Tkinter para criar a interface de usuário. A biblioteca PIL foi escolhida para facilitar a manipulação de arquivos de imagem, garantindo uma experiência de usuário aprimorada.

### Desafios Enfrentados:

* Processamento de Arquivos XML: Lidar com a estrutura complexa dos arquivos XML de NF-e e extrair as informações relevantes de forma eficiente representou um desafio técnico significativo.

*Integração de Bibliotecas Externas: Garantir a integração suave da biblioteca PIL para manipulação de imagens com o restante do aplicativo exigiu cuidados adicionais de implementação e testes.

### Superando os Desafios:

* Análise Detalhada da Estrutura XML: Investimos tempo na compreensão detalhada da estrutura dos arquivos XML de NF-e e desenvolvemos algoritmos robustos para extrair e calcular a soma da coluna qCom de forma precisa.

* Testes Rigorosos: Realizamos testes extensivos para garantir a precisão e confiabilidade do Contador de Produtos XML em uma variedade de cenários de uso.

### Resultados:

O Contador de Produtos XML oferece uma solução eficaz e eficiente para calcular a soma da coluna qCom em arquivos XML de NF-e. Simplificou significativamente o processo de verificação de mercadorias, especialmente em casos onde a quantidade total não estava disponível nas notas fiscais. Além disso, proporcionou uma maior precisão e agilidade nas operações de contagem de produtos, contribuindo para uma gestão mais eficaz do inventário.

## Tecnologias Usadas

- **Python**: Linguagem de programação utilizada para desenvolver o aplicativo.
- **Tkinter**: Biblioteca gráfica do Python para criar interfaces de usuário.
- **PIL (Python Imaging Library)**: Biblioteca Python para abrir, manipular e salvar muitos formatos de imagem diferentes.

## Funcionalidades

- Permite ao usuário selecionar um arquivo XML de NF-e.
- Calcula a soma da coluna qCom (quantidade comercial) dos itens presentes no arquivo XML.
- Exibe o resultado da soma da coluna qCom ao usuário.

## Configuração e Execução

### Pré-requisitos

- Python instalado na máquina.

### Instalação

1. Clone o repositório para sua máquina local:

git clone https://github.com/leandrotobita/appcontadornfe.git

2. Navegue até o diretório onde o código está localizado:

cd appcontadornfe

3. Instale as dependências necessárias usando o seguinte comando:

pip install Pillow

4. Execute o código Python:

python contador_nfe.py


<img src="tela.jpg" alt="Tela Inicial" >

