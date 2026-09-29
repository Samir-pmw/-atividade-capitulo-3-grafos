def conferir(meu_grafo):
    # faz um resumo das estatisticas basicas
    n = meu_grafo.ordem()
    m = meu_grafo.tamanho()
    
    # somando todos os graus
    soma_dos_graus = 0
    isolados = 0
    
    for v in meu_grafo.vertices():
        grau_v = meu_grafo.grau(v)
        soma_dos_graus += grau_v
        
        if grau_v == 0:
            isolados += 1
            
    # calcular a densidade (m / maximo possivel)
    maximo_arestas = (n * (n - 1)) / 2
    dens = 0
    if maximo_arestas > 0:
        dens = m / maximo_arestas
        
    resumo = {
        'n': n,
        'm': m,
        'soma_graus': soma_dos_graus,
        'aperto_de_mao_ok': soma_dos_graus == (2 * m),
        'isolados': isolados,
        'densidade': dens
    }
    
    return resumo
