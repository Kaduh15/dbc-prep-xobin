# Exercício 06 — Detectar Duplicatas (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma lista de inteiros, retorne True se algum valor aparece mais de uma vez.

## Parâmetros e Tipos Esperados
- Assinatura: `def detectar_duplicatas(nums: list) -> bool:`

## Formato do Retorno
- bool: True se há duplicata

## Casos de Exemplo
```python
    (([],), False),
    (([1],), False),
    (([1, 2, 3],), False),
    (([1, 1],), True),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([],), False),
    (([1],), False),
    (([1, 2, 3],), False),
    (([1, 1],), True),
    (([1, 2, 3, 2],), True),
    (([0, -1, 0],), True),
```

## Edge Cases / Extremos
Lista vazia; um só elemento; todos únicos; duplicatas no meio; zeros/negativos repetidos.

## Abordagem / Dica
Compare len(lista) com len(set(lista)): diferença indica duplicata.

## Complexidade
- Tempo O(n), espaço O(n)

## Assinatura Canônica
- **Python**: `def detectar_duplicatas(nums: list) -> bool:`
- **TypeScript**: `export function detectarDuplicatas(nums: number[]): boolean {`

> Stub para editar: `ex06_detectar_duplicatas/solution_ex06_detectar_duplicatas.py` (Python) e `solution.ts` (TS).

