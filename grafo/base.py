from abc import ABC, abstractmethod

class Grafo(ABC):

    @abstractmethod
    def ordem(self):
        pass

    @abstractmethod
    def tamanho(self):
        pass

    @abstractmethod
    def vizinhos(self, v):
        pass

    @abstractmethod
    def tem_aresta(self, u, v):
        pass

    @abstractmethod
    def inserir_aresta(self, u, v):
        pass

    def vertices(self):
        return range(self.ordem())

    def grau(self, v):
        # conta quantos vizinhos tem
        soma = 0
        for _ in self.vizinhos(v):
            soma += 1
        return soma
