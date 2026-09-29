def contar_triangulos(grafo):
    # contar quantos triangulos tem
    # tem q tomar cuidado pra nao contar o mesmo triangulo duas vezes
    total = 0
    
    for u in grafo.vertices():
        for v in grafo.vizinhos(u):
            # forca u < v pra nao repetir
            if v <= u:
                continue
                
            for w in grafo.vizinhos(v):
                # forca v < w
                if w <= v:
                    continue
                    
                # se fechar o ciclo, é um triangulo
                if grafo.tem_aresta(u, w):
                    total += 1
                    
    return total
