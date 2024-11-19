<p align="center">

  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Yara-R/Grafeno">

  <a href="https://github.com/Yara-R/Les-Observablees-IquHACK2024/commits/main/">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Yara-R/Grafeno">
  </a>

   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

</p>

# Grafeno

Grafeno é um projeto desenvolvido como parte da disciplina de Teoria dos Grafos do 5º período da CESAR School ensinada pelo professor [Breno Alencar](https://www.linkedin.com/in/brenoalencar/). O objetivo do projeto é criar uma interface gráfica que facilite a interação e visualização de grafos, permitindo a criação e consulta de propriedades fundamentais de grafos de maneira intuitiva.

## Funcionalidades

A interface gráfica de Grafeno permite ao usuário:

- **Adicionar vértices e arestas**:
  - Interagir com o sistema para criar um grafo inserindo um item de cada vez (vértices e arestas)
  - Interagir com o sistema para criar um grafo inserindo as informações em lote, ou seja, tudo de uma vez só, como um um grande string com as informações de todos os vértices e arestas
  - O usuário poderá criar grafos direcionados ou não-direcionados, e grafos valorados ou não-valorados

- **Consultar propriedades do grafo**:
  - O sistema deve ser capaz de imprimir/visualizar o grafo
  - O sistema pode informar a Ordem e Tamanho do Grafo criado
  - Para um dado vértice o sistema pode informar a lista de vértices adjacentes.
  - Para um dado vértice o sistema pode informar o grau daquele vértice.
 
- **Analisar relações entre vértices**:
  - Dado um par de vértices, o sistema pode informar se os dois vértices são adjacentes ou não
  - Dado um par de vértices, o sistema pode informar o caminho mais curto entre eles e o seu custo
    

## Requisitos

Para executar o projeto Grafeno, é necessário ter:

- Python 3.8+
- Bibliotecas adicionais (neo4j, NetworkX, Matplotlib, tkinter)
- Neo4j Desktop para o banco de dados

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Yara-R/grafeno.git
   ```
   
2. Navegue até o diretório do projeto:
   ```bash
   cd Grafeno
   ```
   
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

 ## Configurando o Neo4j Desktop

1. **Baixe e Instale o Neo4j Desktop**:
   - Acesse [o site do Neo4j](https://neo4j.com/download/) e baixe a versão mais recente do Neo4j Desktop.
   - Após o download, instale o Neo4j Desktop seguindo as instruções do instalador.

2. **Abra o Neo4j Desktop**:
   - Ao abrir pela primeira vez, será solicitado que você crie uma conta Neo4j ou faça login.

3. **Criando um Novo Projeto**:
   - Na tela inicial do Neo4j Desktop, clique em **New Project** e dê um nome ao seu projeto (por exemplo, "Grafeno").

4. **Criando um Novo Banco de Dados Local**:
   - Dentro do projeto, clique em **Add Database** e escolha a opção **Local DBMS**.
   - Dê um nome para o banco de dados, escolha a versão desejada (recomendada: a mais recente compatível) e crie uma senha segura.
   - **Anote essa senha**, pois será usada para se conectar ao banco de dados a partir do código.

5. **Inicie o Banco de Dados**:
   - Após criar o banco de dados, clique em **Start** para inicializá-lo. Aguarde até que ele indique que está "Running".

6. **Visualize o banco de dados no seu navegador**:
   - Acesse no seu navegador `http://localhost:7474/browser/`
   - O URL padrão para conectar ao banco local é `bolt://localhost:7687`.
   - Usuário padrão: `neo4j`
   - Senha: a senha que você criou no passo 4.

8. **Configurando o Código com as Credenciais**:
   - Abra o arquivo do código e substitua as credenciais na linha de inicialização:
     ```python
     app = GraphApp("bolt://localhost:7687", "neo4j", "sua_senha")
     ```
   - Troque `"sua_senha"` pela senha que configurou no Neo4j.


## Uso

Após a instalação, execute o programa com o seguinte comando:

```bash
python3 grafeno.py
```

A interface gráfica será aberta, permitindo que você interaja com o grafo conforme as funcionalidades descritas.

## Licença

Este projeto é distribuído sob a licença MIT. Para mais detalhes, consulte o arquivo `LICENSE`.

---

Esse projeto é uma iniciativa acadêmica da CESAR School para o estudo prático de Teoria dos Grafos, com foco no desenvolvimento de uma ferramenta interativa que facilita a compreensão e manipulação de grafos.
