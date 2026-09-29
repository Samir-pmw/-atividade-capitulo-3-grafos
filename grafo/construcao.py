def construir(pares_lidos, indice_nome_numero, tipo_do_grafo):
    # descobre quantos vertices tem
    qtd_vertices = len(indice_nome_numero)
    
    # cria o grafo
    meu_grafo = tipo_do_grafo(qtd_vertices)
    
    arestas_ignoradas = 0
    tamanho_agora = 0
    
    for u, v in pares_lidos:
        # pega os numeros em vez das letras
        id_u = indice_nome_numero[u]
        id_v = indice_nome_numero[v]
        
        meu_grafo.inserir_aresta(id_u, id_v)
        
        # se nao mudou o tamanho, era repetida
        if meu_grafo.tamanho() == tamanho_agora:
            arestas_ignoradas += 1
        else:
            tamanho_agora = meu_grafo.tamanho()
            
    return meu_grafo, arestas_ignoradas
