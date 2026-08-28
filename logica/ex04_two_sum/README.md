# Exercício 04 — Two Sum

## Descrição do Problema
Dada uma lista de inteiros nums e um alvo, retorne os índices [i, j] com i<j do PRIMEIRO par cuja soma é o alvo; None/[] se não houver.

## Parâmetros e Tipos Esperados
- nums: list[int], alvo: int

## Formato do Retorno
- list[int] (2 índices) ou None

## Casos de Exemplo
```python
# (args) -> esperado
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([], 5), None),
    (([1, 2, 3], 99), None),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([], 5), None),
    (([1, 2, 3], 99), None),
    (([-1, -2, -3], -3), [0, 1]),
    (([0, 0, 1], 0), [0, 1]),
    (([5, 5, 5], 10), [0, 1]),
    (([1], 1), None),
```

## Edge Cases / Extremos
Lista vazia e com um único elemento (sem par → None); alvo com negativos; zeros/duplicados (0+0 e 5+5); sem par possível; par no começo da lista.

## Abordagem / Dica
Força bruta O(n²) com dois laços é o suficiente; para O(n) use um dicionário guardando o complemento esperado visto.

## Complexidade
- Tempo O(n²) força bruta / O(n) com hash, espaço O(1) / O(n)

## Assinatura Canônica
- **Python**: `def two_sum(nums: list, alvo: int) -> list | None:`
- **TypeScript**: `export function twoSum(nums: number[], alvo: number): number[] | null {`

> Stub para editar: `ex04_two_sum/solution_ex04_two_sum.py` (Python) e `solution.ts` (TS).

