import random
import time
from grafo.matriz import GrafoMatriz
from grafo.lista import GrafoLista
from grafo.triangulos import contar_triangulos

def criar_grafo_aleatorio(n, densidade, classe_grafo):
    # cria o grafo
    meu_grafo = classe_grafo(n)
    
    # percorre todas as combinações de vertices
    for i in range(n):
        for j in range(i + 1, n):
            # adiciona a aresta com base na densidade
            if random.random() < densidade:
                meu_grafo.inserir_aresta(i, j)
                
    return meu_grafo

def main():
    n = 2000
    valores_densidade = [0.001, 0.05, 0.5]
    tipos_de_grafo = [
        ('Lista de Adjacência', GrafoLista),
        ('Matriz de Adjacência', GrafoMatriz)
    ]
    
    for densidade in valores_densidade:
        for nome_tipo, classe in tipos_de_grafo:
            
            # fixa a semente para dar o mesmo grafo nas duas estruturas
            random.seed(42)
            
            grafo_teste = criar_grafo_aleatorio(n, densidade, classe)
            
            lista_tempos = []
            
            # roda 3 vezes para pegar a mediana depois
            for rodada in range(3):
                t_inicio = time.perf_counter()
                contar_triangulos(grafo_teste)
                t_fim = time.perf_counter()
                
                tempo_gasto = t_fim - t_inicio
                lista_tempos.append(tempo_gasto)
                
            # pegar o valor do meio (mediana)
            lista_tempos.sort()
            tempo_mediana = lista_tempos[1]
            
            # calculando o espaço
            if nome_tipo == 'Matriz de Adjacência':
                espaco_ocupado = n * n
            else:
                espaco_ocupado = n + 2 * grafo_teste.tamanho()
                
            # imprime o resultado dessa rodada
            print(f"Densidade: {densidade} | Tipo: {nome_tipo}")
            print(f" -> Tempo mediano: {tempo_mediana:.5f} s")
            print(f" -> Espaço na memória: {espaco_ocupado} posições\n")

if __name__ == "__main__":
    main()
