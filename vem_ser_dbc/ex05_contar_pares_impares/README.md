# Exercício 05 — Contar Pares e Ímpares (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma lista de inteiros, retorne (quantidade de pares, quantidade de ímpares).

## Parâmetros e Tipos Esperados
- Assinatura: `def contar_pares_impares(nums: list) -> tuple:`

## Formato do Retorno
- tuple[int,int]: (pares, ímpares)

## Casos de Exemplo
```python
    (([],), (0, 0)),
    (([1],), (0, 1)),
    (([2],), (1, 0)),
    (([1, 2, 3, 4],), (2, 2)),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([],), (0, 0)),
    (([1],), (0, 1)),
    (([2],), (1, 0)),
    (([1, 2, 3, 4],), (2, 2)),
    (([0],), (1, 0)),
    (([-2, -3, -4],), (2, 1)),
    (([2, 4, 6],), (3, 0)),
```

## Edge Cases / Extremos
Lista vazia (→ (0,0)); zero (é par); negativos; todos pares; todos ímpares.

## Abordagem / Dica
Conte os pares com `x % 2 == 0` (0 é par; negativos seguem a mesma regra) e derive os ímpares.

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def contar_pares_impares(nums: list) -> tuple:`
- **TypeScript**: `export function contarParesImpares(nums: number[]): [number, number] {`

> Stub para editar: `ex05_contar_pares_impares/solution_ex05_contar_pares_impares.py` (Python) e `solution.ts` (TS).

