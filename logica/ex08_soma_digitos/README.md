# Exercício 08 — Soma dos Dígitos

## Descrição do Problema
Dado um inteiro, retorne a soma dos dígitos do seu valor absoluto.

## Parâmetros e Tipos Esperados
- n: int

## Formato do Retorno
- int: soma dos dígitos de |n|

## Casos de Exemplo
```python
# (args) -> esperado
    ((123,), 6),
    ((0,), 0),
    ((-45,), 9),
    ((9,), 9),
    ((1000,), 1),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((123,), 6),
    ((0,), 0),
    ((-45,), 9),
    ((9,), 9),
    ((1000,), 1),
    ((7,), 7),
```

## Edge Cases / Extremos
Zero (soma 0); dígito único; números negativos (usa valor absoluto); com zeros internos (1000); dezenas/hábitos comuns.

## Abordagem / Dica
Tome o valor absoluto, converta para string e some cada caractere como dígito. Negativos usam a magnitude.

## Complexidade
- Tempo O(log n), espaço O(log n)

## Assinatura Canônica
- **Python**: `def soma_digitos(n: int) -> int:`
- **TypeScript**: `export function somaDigitos(n: number): number {`

> Stub para editar: `ex08_soma_digitos/solution_ex08_soma_digitos.py` (Python) e `solution.ts` (TS).

