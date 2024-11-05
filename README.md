<p align="center">

  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Yara-R/Grafeno?color=353949">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Yara-R/Grafeno">

  <a href="https://github.com/Yara-R/Les-Observablees-IquHACK2024/commits/main/">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Yara-R/Grafeno">
  </a>

   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

</p>

# Grafeno

Grafeno é um projeto desenvolvido como parte da disciplina de Teoria dos Grafos do 5º período da CESAR School ensinada pelo professor Breno Alencar. O objetivo do projeto é criar uma interface gráfica que facilite a interação e visualização de grafos, permitindo a criação e consulta de propriedades fundamentais de grafos de maneira intuitiva.

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

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Yara-R/grafeno.git
   ```
   
2. Navegue até o diretório do projeto:
   ```bash
   cd grafeno
   ```
   
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

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
