# Exercício 02 — Palíndromo

## Descrição do Problema
Dada uma string, retorne True se ela for um palíndromo, ignorando maiúsculas, espaços e pontuação (só letras a-z e dígitos 0-9 contam).

## Parâmetros e Tipos Esperados
- texto: str

## Formato do Retorno
- bool: True se palíndromo

## Casos de Exemplo
```python
# (args) -> esperado
    (('arara',), True),
    (('A man a plan a canal Panama',), True),
    (('hello',), False),
    (('',), True),
    (('Ana',), True),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('arara',), True),
    (('A man a plan a canal Panama',), True),
    (('hello',), False),
    (('',), True),
    (('Ana',), True),
    (('12321',), True),
    (('a',), True),
    (('ab',), False),
```

## Edge Cases / Extremos
String vazia (é palíndromo); um único caractere; palíndromo com espaços/pontuação; dígitos; caixa mista (Ana/ana); string não simétrica.

## Abordagem / Dica
Normalize (lowercase + remova tudo que não for a-z/0-9) e compare a string com sua inversão. É simétrico por construção.

## Complexidade
- Tempo O(n), espaço O(n)

## Assinatura Canônica
- **Python**: `def palindromo(texto: str) -> bool:`
- **TypeScript**: `export function palindromo(texto: string): boolean {`

> Stub para editar: `ex02_palindromo/solution_ex02_palindromo.py` (Python) e `solution.ts` (TS).

