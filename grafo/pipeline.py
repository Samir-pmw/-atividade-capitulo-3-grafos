from grafo.leitura import ler_pares, indexar
from grafo.construcao import construir
from grafo.conferencia import conferir
from grafo.lista import GrafoLista

def main():
    print("Testando o pipeline...")
    pares, infos_leitura = ler_pares("dados/exemplo.edges")
    indice = indexar(pares)
    
    grafo_teste, descartadas = construir(pares, indice, GrafoLista)
    
    print("Leitura:", infos_leitura)
    print("Arestas repetidas descartadas:", descartadas)
    
    resultado = conferir(grafo_teste)
    print("Resultado final do grafo:", resultado)

if __name__ == "__main__":
    main()
