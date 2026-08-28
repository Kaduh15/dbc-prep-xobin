# Exercício 11 — Número Primo

## Descrição do Problema
Dado um inteiro, retorne True se for primo (divisível só por 1 e por ele mesmo).

## Parâmetros e Tipos Esperados
- n: int

## Formato do Retorno
- bool: True se primo

## Casos de Exemplo
```python
# (args) -> esperado
    ((0,), False),
    ((1,), False),
    ((2,), True),
    ((3,), True),
    ((4,), False),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((0,), False),
    ((1,), False),
    ((2,), True),
    ((3,), True),
    ((4,), False),
    ((9,), False),
    ((97,), True),
    ((25,), False),
```

## Edge Cases / Extremos
0 e 1 (não primos); 2 e 3 (primos); quadrados perfeitos (4, 9, 25 → não primos); primo grande (97); composto ímpar (9).

## Abordagem / Dica
Números < 2 não são primos; teste divisores até √n — se algum dividir, não é primo.

## Complexidade
- Tempo O(√n), espaço O(1)

## Assinatura Canônica
- **Python**: `def numero_primo(n: int) -> bool:`
- **TypeScript**: `export function numeroPrimo(n: number): boolean {`

> Stub para editar: `ex11_numero_primo/solution_ex11_numero_primo.py` (Python) e `solution.ts` (TS).

