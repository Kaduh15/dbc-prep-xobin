# Exercício 07 — Soma da Borda de uma Matriz (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma matriz 2D (retangular), retorne a soma de todos os elementos da borda (primeira/última linha, primeira/última coluna), contando cada canto uma vez.

## Parâmetros e Tipos Esperados
- Assinatura: `def soma_borda_matriz(matriz: list) -> int:`

## Formato do Retorno
- int: soma da borda

## Casos de Exemplo
```python
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 40),
    (([[5]],), 5),
    (([[1, 2], [3, 4]],), 10),
    (([],), 0),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 40),
    (([[5]],), 5),
    (([[1, 2], [3, 4]],), 10),
    (([],), 0),
    (([[]],), 0),
    (([[1, 2, 3, 4]],), 10),
    (([[-1, -2], [-3, -4]],), -10),
```

## Edge Cases / Extremos
Matriz vazia ou com linhas vazias (→ 0); matriz 1x1 (a borda é a própria célula); uma única linha; matriz 2x2 (tudo é borda); valores negativos.

## Abordagem / Dica
Percorra as células onde linha ∈ {0, n−1} OU coluna ∈ {0, m−1}; some apenas essas. Trate matriz vazia.

## Complexidade
- Tempo O(n·m), espaço O(1)

## Assinatura Canônica
- **Python**: `def soma_borda_matriz(matriz: list) -> int:`
- **TypeScript**: `export function somaBordaMatriz(matriz: number[][]): number {`

> Stub para editar: `ex07_soma_borda_matriz/solution_ex07_soma_borda_matriz.py` (Python) e `solution.ts` (TS).

