# Exercício 10 — Fibonacci

## Descrição do Problema
Dado um inteiro n ≥ 0, retorne o n-ésimo termo da sequência de Fibonacci (F0=0, F1=1).

## Parâmetros e Tipos Esperados
- n: int (n >= 0)

## Formato do Retorno
- int: F_n (F0=0)

## Casos de Exemplo
```python
# (args) -> esperado
    ((0,), 0),
    ((1,), 1),
    ((2,), 1),
    ((5,), 5),
    ((10,), 55),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((0,), 0),
    ((1,), 1),
    ((2,), 1),
    ((5,), 5),
    ((10,), 55),
    ((6,), 8),
```

## Edge Cases / Extremos
F0=0; F1=1; termos iniciais (2,5,6); um termo de meio (ex.: F10=55) para conferir a enumeração a partir de 0.

## Abordagem / Dica
Itere atualizando (a,b) = (b, a+b); F_n é o valor após n passos.

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def fibonacci(n: int) -> int:`
- **TypeScript**: `export function fibonacci(n: number): number {`

> Stub para editar: `ex10_fibonacci/solution_ex10_fibonacci.py` (Python) e `solution.ts` (TS).

