def ler_pares(caminho):
    # le os txt ignorando os comentarios
    arquivo = open(caminho, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    
    lista_de_pares = []
    
    # estatisticas da leitura
    info = {'linhas_totais': 0, 'linhas_ignoradas': 0, 'lacos': 0}
    
    for l in linhas:
        info['linhas_totais'] += 1
        
        texto_limpo = l.strip()
        if texto_limpo == '' or texto_limpo.startswith('#'):
            info['linhas_ignoradas'] += 1
            continue
            
        partes = texto_limpo.split()
        vertice_u = partes[0]
        vertice_v = partes[1]
        
        if vertice_u == vertice_v:
            info['lacos'] += 1
            continue
            
        lista_de_pares.append((vertice_u, vertice_v))
        
    return lista_de_pares, info

def indexar(pares):
    # converte os nomes (tipo 'a', 'b') para numeros 0, 1, 2...
    dicionario = {}
    contador = 0
    
    for u, v in pares:
        if u not in dicionario:
            dicionario[u] = contador
            contador += 1
        if v not in dicionario:
            dicionario[v] = contador
            contador += 1
            
    return dicionario
