# Atividade de Teoria dos Grafos (Capítulo 3)

Repositório pra entregar o trabalho prático da matéria de Grafos. O objetivo foi testar na prática a diferença de guardar um grafo numa Matriz de Adjacência ou numa Lista de Adjacência, e ver qual demora menos tempo rodando um código de contar triângulos.

## O que tem aqui:
- `grafo/`: O pacote principal com as classes `GrafoMatriz` e `GrafoLista`, além de um monte de arquivo pra ler txt (`leitura.py`, `construcao.py`, etc).
- `testes/`: Pasta que verifica se o grafo do livro tá dando os valores certos de vértices e arestas.
- `medir.py`: O script pesado que gera grafos de tamanho 2000 e roda o cronômetro pra ver quem ganha.
- `karate_pipeline.py`: Um teste final lendo o dataset Zachary's Karate Club.
- `relatorio.md`: Arquivo markdown com as tabelas de resposta das questões teóricas!

## Como rodar o projeto

1. Pra rodar os testes basiquinhos:
```bash
python -m pytest testes/test_grafo.py
```

2. Pra rodar o teste de tempo (cuidado que a matriz pesada trava):
```bash
python medir.py
```
