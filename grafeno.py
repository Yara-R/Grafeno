import tkinter as tk
from tkinter import simpledialog, messagebox
from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphApp:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.create_interface()

    def close(self):
        self.driver.close()
        plt.close()

    def delete_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        messagebox.showinfo("Informação", "Grafo deletado.")

    def add_vertex(self):
        vertex = simpledialog.askstring("Adicionar Vértice", "Nome do vértice:")
        if vertex:
            with self.driver.session() as session:
                session.run("MERGE (n:Node {name: $name})", name=vertex)
            messagebox.showinfo("Informação", f"Vértice '{vertex}' adicionado.")

    def add_edge(self):
        source = simpledialog.askstring("Adicionar Aresta", "Vértice de origem:")
        target = simpledialog.askstring("Adicionar Aresta", "Vértice de destino:")
        weight = simpledialog.askstring("Adicionar Aresta", "Peso (deixe em branco para não valorado):")
        directed = simpledialog.askstring("Adicionar Aresta", "Direcionado? (s/n):").strip().lower() == 's'
        
        weight = float(weight) if weight else None

        with self.driver.session() as session:
            session.run("MERGE (a:Node {name: $source})", source=source)
            session.run("MERGE (b:Node {name: $target})", target=target)

            if directed:
                if weight is not None:
                    session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                "MERGE (a)-[r:REL {weight: $weight, directed: true}]->(b)",
                                source=source, target=target, weight=weight)
                else:
                    session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                "MERGE (a)-[r:REL {directed: true}]->(b)",
                                source=source, target=target)
            else:
                if weight is not None:
                    session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                "MERGE (a)-[r:REL {weight: $weight, directed: false}]-(b)",
                                source=source, target=target, weight=weight)
                else:
                    session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                "MERGE (a)-[r:REL {directed: false}]-(b)",
                                source=source, target=target)

        messagebox.showinfo("Informação", f"Aresta de '{source}' para '{target}' adicionada.")


    def add_edges_in_batch(self):
        edges_input = simpledialog.askstring("Adicionar Arestas em Lote", "Digite arestas no formato 'v1,v2,peso,s/n' (use 's' para direcionado e 'n' para não direcionado) e separe por ponto e vírgula:")
        edges = [tuple(edge.split(',')) for edge in edges_input.split(';')]

        with self.driver.session() as session:
            for edge in edges:
                source, target = edge[0], edge[1]
                weight = float(edge[2]) if len(edge) > 2 and edge[2] else None
                directed = edge[3].strip().lower() == 's' if len(edge) > 3 else False

                session.run("MERGE (a:Node {name: $source})", source=source)
                session.run("MERGE (b:Node {name: $target})", target=target)

                if directed:
                    if weight is not None:
                        session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                    "MERGE (a)-[r:REL {weight: $weight, directed: true}]->(b)",
                                    source=source, target=target, weight=weight)
                    else:
                        session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                    "MERGE (a)-[r:REL {directed: true}]->(b)",
                                    source=source, target=target)
                else:
                    if weight is not None:
                        session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                    "MERGE (a)-[r:REL {weight: $weight, directed: false}]-(b)",
                                    source=source, target=target, weight=weight)
                    else:
                        session.run("MATCH (a:Node {name: $source}), (b:Node {name: $target}) "
                                    "MERGE (a)-[r:REL {directed: false}]-(b)",
                                    source=source, target=target)

            messagebox.showinfo("Informação", "Arestas adicionadas com sucesso.")


    def get_adjacent_vertices(self):
        vertex = simpledialog.askstring("Vértices adjacentes", "Nome do vértice: ")
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n:Node {name: $vertex})-[:REL]-(adj)
                RETURN adj.name AS adjacent
            """, vertex=vertex)
            
            adjacents = [record["adjacent"] for record in result]
            if adjacents:
                messagebox.showinfo("Informação", f"Vértices adjacentes de '{vertex}': {adjacents}")
            else:
                messagebox.showinfo(f"Nenhum vértice adjacente encontrado para '{vertex}'.")



    def get_vertex_degree(self):
        vertex_name = simpledialog.askstring("Grau de um Vértice", "Digite o nome do vértice:")
        if not vertex_name:
            messagebox.showwarning("Atenção", "Nome do vértice não pode ser vazio.")
            return

        with self.driver.session() as session:
            result = session.run("MATCH (n:Node {name: $vertex})-[r]-() RETURN count(r) AS degree", vertex=vertex_name)
            degree = result.single()

        if degree is None:
            messagebox.showinfo("Grau de um Vértice", f"O vértice '{vertex_name}' não foi encontrado.")
        else:
            messagebox.showinfo("Grau de um Vértice", f"O grau do vértice '{vertex_name}' é: {degree['degree']}")


    def get_order_and_size(self):
        with self.driver.session() as session:
            order = session.run("MATCH (n) RETURN count(n) AS order").single()["order"]
            size = session.run("MATCH ()-[r]->() RETURN count(r) AS size").single()["size"]
        messagebox.showinfo("Informação", f"Ordem: {order}, Tamanho: {size}")

    def display_graph(self):
        with self.driver.session() as session:
            directed_edges = session.run("MATCH (a:Node)-[r:REL]->(b:Node) WHERE r.directed = true RETURN count(r) > 0 AS has_directed")
            is_directed = directed_edges.single()["has_directed"]

            G = nx.DiGraph() if is_directed else nx.Graph()

            nodes = session.run("MATCH (n:Node) RETURN n.name AS name")
            for record in nodes:
                G.add_node(record["name"])

            if is_directed:
                edges = session.run("MATCH (a:Node)-[r:REL]->(b:Node) WHERE r.directed = true RETURN a.name AS source, b.name AS target, r.weight AS weight")
            else:
                edges = session.run("MATCH (a:Node)-[r:REL]-(b:Node) RETURN a.name AS source, b.name AS target, r.weight AS weight")

            for record in edges:
                source = record["source"]
                target = record["target"]
                weight = record["weight"] if record["weight"] is not None else 0
                G.add_edge(source, target, weight=weight)

        root = tk.Tk()
        root.title("Visualização do Grafo")

        pos = nx.spring_layout(G)  # Layout dos nós
        edge_labels = nx.get_edge_attributes(G, 'weight')

        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=15, arrows=is_directed)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        canvas = FigureCanvasTkAgg(fig, master=root)  # A figura será exibida na janela do Tkinter
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        button_close = tk.Button(root, text="Fechar", command=root.destroy)
        button_close.pack()

        root.mainloop()

    def check_adjacency(self):
        vertex1 = simpledialog.askstring("Verificar Adjacência", "Primeiro vértice:")
        vertex2 = simpledialog.askstring("Verificar Adjacência", "Segundo vértice:")
        with self.driver.session() as session:
            result = session.run("MATCH (a {name: $v1})-[r]->(b {name: $v2}) RETURN r", v1=vertex1, v2=vertex2)
            adjacent = result.single() is not None
        messagebox.showinfo("Resultado", f"Os vértices {vertex1} e {vertex2} são adjacentes: {adjacent}")

    def shortest_path(self):
        source = simpledialog.askstring("Caminho Mais Curto", "Vértice de origem:")
        target = simpledialog.askstring("Caminho Mais Curto", "Vértice de destino:")
        with self.driver.session() as session:
            result = session.run(
                "MATCH (start:Node {name: $source}), (end:Node {name: $target}), "
                "p = shortestPath((start)-[*]-(end)) "
                "RETURN length(p) AS length, nodes(p) AS path",
                source=source, target=target
            )
            record = result.single()
        if record:
            length = record["length"]
            path = [node["name"] for node in record["path"]]
            messagebox.showinfo("Caminho Mais Curto", f"Caminho mais curto de {source} para {target}: Comprimento = {length}, Caminho = {path}")
        else:
            messagebox.showinfo("Caminho Mais Curto", f"Nenhum caminho encontrado de {source} para {target}.")

    def create_interface(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Manipulação de Grafos")

        options = [
            ("Adicionar Vértice", self.add_vertex),
            ("Adicionar Aresta", self.add_edge),
            ("Adicionar Arestas em Lote", self.add_edges_in_batch), 
            ("Ordem e Tamanho do Grafo", self.get_order_and_size),
            ("Lista de Adjacência", self.get_adjacent_vertices),  
            ("Mostra Grafo", self.display_graph), 
            ("Grau de um Vértice", self.get_vertex_degree), 
            ("Verificar se Dois Vértices São Adjacentes", self.check_adjacency),
            ("Caminho Mais Curto entre Dois Vértices", self.shortest_path),
            ("Deletar o Grafo", self.delete_all),
            ("Sair", self.root.quit)
        ]

        for text, command in options:
            button = tk.Button(self.root, text=text, command=command)
            button.pack(fill="x", padx=5, pady=5)

        self.root.mainloop()

app = GraphApp("bolt://localhost:7687", "neo4j", "TeoriaDosGrafos")
