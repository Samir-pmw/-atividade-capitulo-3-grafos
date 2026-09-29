import pytest
from grafo.matriz import GrafoMatriz
from grafo.lista import GrafoLista
from grafo.triangulos import contar_triangulos

# arestas do grafo da figura 3.1
lista_de_arestas = [
    (0, 1), (0, 2),  # a-b, a-c
    (1, 2), (1, 3),  # b-c, b-d
    (2, 3), (2, 4),  # c-d, c-e
    (3, 4),          # d-e
    (4, 5)           # e-f
]

def validar_basico(meu_grafo):
    for u, v in lista_de_arestas:
        meu_grafo.inserir_aresta(u, v)
        
    assert meu_grafo.ordem() == 6
    assert meu_grafo.tamanho() == 8
    
    graus_dos_vertices = []
    for v in meu_grafo.vertices():
        graus_dos_vertices.append(meu_grafo.grau(v))
        
    graus_dos_vertices.sort(reverse=True)
    assert graus_dos_vertices == [4, 3, 3, 3, 2, 1]
    
    # lema do aperto de mao
    assert sum(graus_dos_vertices) == 2 * meu_grafo.tamanho()
    
    # tem que dar 3 triangulos
    qtd = contar_triangulos(meu_grafo)
    assert qtd == 3

def test_matriz():
    g = GrafoMatriz(6)
    validar_basico(g)

def test_lista():
    g = GrafoLista(6)
    validar_basico(g)
