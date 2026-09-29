from pathlib import Path
from grafo.construcao import construir
from grafo.conferencia import conferir
from grafo.leitura import indexar, ler_pares
from grafo.lista import GrafoLista

# Lendo o dataset do Karate Club q baixei
caminho_arquivo = Path("dados/karate.edges")
pares_lidos, relatorio_leitura = ler_pares(caminho_arquivo)

# Criando os indices para construir o grafo (tirando de string pra int)
dicionario_indices = indexar(pares_lidos)

# Criando o grafo com Lista pq a densidade desse grafo é baixa
meu_grafo_karate, qtd_repetidas = construir(pares_lidos, dicionario_indices, GrafoLista)

print("--- RELATÓRIO DO DATASET KARATE CLUB ---")
print("Dados da leitura do arquivo txt:", relatorio_leitura)
print("Arestas ignoradas/repetidas:", qtd_repetidas)
print("\nInformações do Grafo (função conferir):")
dados_conferencia = conferir(meu_grafo_karate)

for chave, valor in dados_conferencia.items():
    print(f"{chave}: {valor}")
