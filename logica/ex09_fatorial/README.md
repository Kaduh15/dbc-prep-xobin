# Exercício 09 — Fatorial

## Descrição do Problema
Dado um inteiro n ≥ 0, retorne n! (produto 1×2×…×n, com 0! = 1).

## Parâmetros e Tipos Esperados
- n: int (n >= 0)

## Formato do Retorno
- int: n!

## Casos de Exemplo
```python
# (args) -> esperado
    ((0,), 1),
    ((1,), 1),
    ((5,), 120),
    ((3,), 6),
    ((2,), 2),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((0,), 1),
    ((1,), 1),
    ((5,), 120),
    ((3,), 6),
    ((2,), 2),
    ((6,), 720),
```

## Edge Cases / Extremos
0! = 1 (caso-base); 1! = 1; números pequenos (2,3,5); fatoriais intermediários (6!=720).

## Abordagem / Dica
Produto acumulado de 1 a n; defina o caso-base 0! = 1.

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def fatorial(n: int) -> int:`
- **TypeScript**: `export function fatorial(n: number): number {`

> Stub para editar: `ex09_fatorial/solution_ex09_fatorial.py` (Python) e `solution.ts` (TS).

