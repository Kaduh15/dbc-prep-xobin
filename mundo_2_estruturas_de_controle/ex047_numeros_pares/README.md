# EX47 — Números pares no intervalo

## Descrição
Mostre todos os números pares no intervalo de `inicio` até `fim` (inclusive), em ordem crescente.

## Parâmetros e Tipos
- `inicio` (int, opcional) — limite inferior, padrão `1`.
- `fim` (int, opcional) — limite superior, padrão `50`.

## Retorno
`list[int]` — todos os números pares em `[inicio, fim]`, em ordem crescente.

## Casos de Exemplo
```python
numeros_pares()       -> [2, 4, 6, ..., 48, 50]
numeros_pares(1, 10)  -> [2, 4, 6, 8, 10]
numeros_pares(15, 25) -> [16, 18, 20, 22, 24]
numeros_pares(3, 3)   -> []
```

## Casos de Teste (todos, incluindo extremos)
```python
((), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),
((1, 10), [2, 4, 6, 8, 10]),
((15, 25), [16, 18, 20, 22, 24]),
((3, 3), []), ((2, 8), [2, 4, 6, 8]),
# extremos
((0, 6), [0, 2, 4, 6]), ((1, 1), []), ((7, 7), []), ((20, 30), [20, 22, 24, 26, 28, 30]),
```

## Edge Cases / Extremos
- Intervalo inclusivo nas duas pontas (`(2, 8)` inclui 2 e 8).
- `0` é par e aparece quando `inicio <= 0` (`(0, 6)` → `[0, 2, 4, 6]`).
- Sem pares no intervalo → lista vazia (`(3, 3)`, `(7, 7)`).

## Abordagem / Dica
Iterar em `range(inicio, fim + 1)` filtrando `n % 2 == 0`.

## Complexidade
- Tempo O(n), espaço O(n), com `n = fim - inicio + 1`.

## Assinatura Canônica
- **Python**: `def numeros_pares(inicio: int = 1, fim: int = 50) -> list[int]:`
- **TypeScript**: `export function numerosPares(inicio: number = 1, fim: number = 50): number[]`

> Stub para editar: `ex047_numeros_pares/solution_ex047_numeros_pares.py` (Python) e `solution.ts` (TS).
