from grafo.base import Grafo

class GrafoLista(Grafo):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.quantidade_arestas = 0
        
        # cria a lista com um set vazio pra cada vertice
        self.lista_adj = []
        for i in range(num_vertices):
            self.lista_adj.append(set())

    def ordem(self):
        return self.num_vertices

    def tamanho(self):
        return self.quantidade_arestas

    def vizinhos(self, v):
        # retorna a lista de vizinhos direto (bem mais rapido)
        return self.lista_adj[v]

    def grau(self, v):
        # posso só dar um len em vez de contar no for igual a matriz
        return len(self.lista_adj[v])

    def tem_aresta(self, u, v):
        return v in self.lista_adj[u]

    def inserir_aresta(self, u, v):
        if u == v:
            print("nao tem laco")
            return
            
        if v in self.lista_adj[u]:
            return
            
        self.lista_adj[u].add(v)
        self.lista_adj[v].add(u)
        self.quantidade_arestas += 1
