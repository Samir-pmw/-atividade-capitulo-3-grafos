import networkx as nx
from pathlib import Path

from grafo.construcao import construir
from grafo.leitura import indexar, ler_pares
from grafo.lista import GrafoLista
from grafo.triangulos import contar_triangulos

# leitura normal que a gente fez
pares_lidos, relatorio_lixo = ler_pares(Path("dados/exemplo.edges"))
dicionario_indice = indexar(pares_lidos)
nosso_grafo, repetidas = construir(pares_lidos, dicionario_indice, GrafoLista)

# leitura usando a biblioteca pronta do networkx pra tirar a prova real
grafo_nx = nx.Graph()
for u, v in pares_lidos:
    grafo_nx.add_edge(dicionario_indice[u], dicionario_indice[v])

# nossa contagem
total_nosso = contar_triangulos(nosso_grafo)

# contagem do networkx (ele devolve num dicionario entao tem que somar e dividir por 3)
dicionario_triangulos_nx = nx.triangles(grafo_nx)
soma = 0
for v in dicionario_triangulos_nx.values():
    soma += v
total_nx = soma // 3

print("Total nosso:", total_nosso)
print("Total do NetworkX:", total_nx)
if total_nosso == total_nx:
    print("Sucesso! As implementações deram o mesmo valor.")
else:
    print("Ops, deu alguma diferença.")
