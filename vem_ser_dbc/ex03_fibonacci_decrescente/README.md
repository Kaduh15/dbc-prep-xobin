# Exercício 03 — Fibonacci Decrescente até um Limite (Vem Ser DBC / Xobin)

## Descrição do Problema
Dado um limite, retorne a lista das distintas potências/termos de Fibonacci (F0=0, F1=1…) estritamente menores que o limite, em ordem DECRESCENTE.

## Parâmetros e Tipos Esperados
- Assinatura: `def fibonacci_decrescente(limite: int) -> list:`

## Formato do Retorno
- list[int]: termos de Fibonacci < limite, decrescente

## Casos de Exemplo
```python
    ((1,), [0]),
    ((2,), [1, 0]),
    ((3,), [2, 1, 0]),
    ((6,), [5, 3, 2, 1, 0]),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((1,), [0]),
    ((2,), [1, 0]),
    ((3,), [2, 1, 0]),
    ((6,), [5, 3, 2, 1, 0]),
    ((0,), []),
    ((-5,), []),
    ((10,), [8, 5, 3, 2, 1, 0]),
```

## Edge Cases / Extremos
Limite 0 ou negativo (→ vazio); limite 1 (só [0]); limite 2 (→ [1,0]); os termos de Fibonacci têm o 1 duplicado (deve virar único).

## Abordagem / Dica
Gere os termos enquanto < limite (ignorando o duplicado do 1), remova duplicatas e ordene do maior para o menor.

## Complexidade
- Tempo O(limite), espaço O(limite)

## Assinatura Canônica
- **Python**: `def fibonacci_decrescente(limite: int) -> list:`
- **TypeScript**: `export function fibonacciDecrescente(limite: number): number[] {`

> Stub para editar: `ex03_fibonacci_decrescente/solution_ex03_fibonacci_decrescente.py` (Python) e `solution.ts` (TS).

