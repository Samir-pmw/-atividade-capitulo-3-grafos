from grafo.base import Grafo

class GrafoMatriz(Grafo):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.quantidade_arestas = 0
        
        # cria a matriz de adjacencia preenchida com zeros
        self.matriz = []
        for i in range(num_vertices):
            linha = [0] * num_vertices
            self.matriz.append(linha)

    def ordem(self):
        return self.num_vertices

    def tamanho(self):
        return self.quantidade_arestas

    def vizinhos(self, v):
        # procura na linha inteira do vertice v quem é vizinho
        lista_vizinhos = []
        for u in range(self.num_vertices):
            if self.matriz[v][u] == 1:
                lista_vizinhos.append(u)
        return lista_vizinhos

    def tem_aresta(self, u, v):
        return self.matriz[u][v] == 1

    def inserir_aresta(self, u, v):
        if u == v:
            print("ops, nao pode ter laço")
            return
            
        if self.matriz[u][v] == 1:
            return  # ja existe
            
        # coloca 1 nas duas posicoes porque é nao orientado
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1
        self.quantidade_arestas += 1
