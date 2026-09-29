# Relatório - Atividade Capítulo 3

## Item 3: Matriz de incidência

Tirando a aresta $ce$ do grafo da Figura 3.1, sobram as arestas: $ab, ac, bc, bd, cd, de, ef$.
Fiz a matriz de incidência de $G - ce$ à mão, ficou assim:

|   | ab | ac | bc | bd | cd | de | ef | Soma dos graus |
|---|----|----|----|----|----|----|----|----------------|
| a |  1 |  1 |  0 |  0 |  0 |  0 |  0 | 2              |
| b |  1 |  0 |  1 |  1 |  0 |  0 |  0 | 3              |
| c |  0 |  1 |  1 |  0 |  1 |  0 |  0 | 3              |
| d |  0 |  0 |  0 |  1 |  1 |  1 |  0 | 3              |
| e |  0 |  0 |  0 |  0 |  0 |  1 |  1 | 2              |
| f |  0 |  0 |  0 |  0 |  0 |  0 |  1 | 1              |

**O que mudou em relação à matriz original?**
O vértice `c` perdeu 1 grau (passou de 4 para 3) e o vértice `e` perdeu 1 grau (passou de 3 para 2). Além disso, sumiu a coluna `ce` inteira da tabela, e é por isso que cada uma dessas linhas perdeu um '1'. O resto continua igual porque a soma da coluna dá sempre 2 (só liga 2 pontos).

---

## Itens 4 e 5: Tempos e Memória

Gerei os grafos com $n = 2000$ e rodei o script `medir.py`. Anotei as medianas dos tempos de 3 rodadas.
Na Matriz a última demorou demais, deixei rodando um tempão e fiz uma estimativa baseada nos loops!

| Densidade | Tipo de Grafo        | Tempo Mediano (s) | Espaço (posições) |
|-----------|----------------------|-------------------|-------------------|
| 0.001     | Lista de Adjacência  | 0.0006            | 5820              |
| 0.001     | Matriz de Adjacência | 0.2450            | 4000000           |
| 0.05      | Lista de Adjacência  | 0.4535            | 201638            |
| 0.05      | Matriz de Adjacência | ~15.000           | 4000000           |
| 0.5       | Lista de Adjacência  | ~45.000           | 1999250           |
| 0.5       | Matriz de Adjacência | Demorou muito     | 4000000           |

---

## Item 6: Análise dos Resultados

**1. Qual implementação foi mais rápida e por quê?**
A **Lista de Adjacência** ganhou disparado, principalmente nas densidades baixinhas (0.001 e 0.05). O motivo é que no `for` da lista a gente só olha os vizinhos que realmente existem, enquanto na Matriz o `for` tem que olhar todos os 2000 vértices pra ver se tem o número '1' na posição, perdendo mó tempo olhando zeros.

**2. A ordem muda conforme a densidade cresce?**
Na real não muda, a Lista continuou ganhando (ou pelo menos empatando) mesmo quando chegou na densidade de 0.5. Isso acontece porque mesmo quando o grafo tá super cheio (metade de chance de ter aresta), ainda assim você percorre só a metade do tamanho varrendo os vizinhos, em vez de percorrer tudo na Matriz. 

**3. Concorda com o custo teórico?**
Concorda sim! O custo teórico da Lista é $O(n + \sum d(v)^2)$ (tabela do livro) que cresce com a densidade, e o da Matriz é $O(n^2 + mn)$ que já tem um custo base de $n^2$ muito alto pra começar. No espaço (memória) ficou mais claro ainda: a Matriz cravou em $4.000.000$ espaços fixos desde o primeiro teste (que é $n^2$), e a lista foi subindo de 5 mil pra 2 milhões conforme as arestas ($n + 2m$) aumentavam.

---

## Item 7: Conjunto de Dados Público

Resolvi testar o **Zachary's Karate Club** (é uma rede de um clube de karate que brigaram e se dividiram em dois).
Rodando no `karate_pipeline.py`, peguei essas estatísticas:

* **n (vértices)**: 34
* **m (arestas)**: 78
* **Densidade**: 0.139 (aprox 13.9%)
* **Problemas (laços/linhas ignoradas)**: 0

Como a densidade deu em torno de 13%, é um grafo bem **esparso**. Então foi melhor rodar ele com a Lista de Adjacência pra gastar menos memória.
