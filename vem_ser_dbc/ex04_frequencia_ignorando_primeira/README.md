# Exercício 04 — Frequência Ignorando a Primeira Ocorrência (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma string, retorne um dicionário com cada caractere e sua frequência DESCONTANDO a primeira ocorrência (ou seja, ocorrências−1), apenas para caracteres que aparecem 2+ vezes.

## Parâmetros e Tipos Esperados
- Assinatura: `def frequencia_ignorando_primeira(texto: str) -> dict:`

## Formato do Retorno
- dict: {caractere: ocorrências−1} p/ ocorrências ≥2

## Casos de Exemplo
```python
    (('',), {}),
    (('abc',), {}),
    (('aab',), {'a': 1}),
    (('aaaa',), {'a': 3}),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('',), {}),
    (('abc',), {}),
    (('aab',), {'a': 1}),
    (('aaaa',), {'a': 3}),
    (('banana',), {'a': 2, 'n': 1}),
    (('aa bb',), {'a': 1, 'b': 1}),
```

## Edge Cases / Extremos
String vazia; todas as letras únicas; letras repetidas; repetições múltiplas; espaços contam como caractere.

## Abordagem / Dica
Conte o total por caractere; o resultado é {c: total−1} descartando os que ficam ≤0.

## Complexidade
- Tempo O(n), espaço O(k)

## Assinatura Canônica
- **Python**: `def frequencia_ignorando_primeira(texto: str) -> dict:`
- **TypeScript**: `export function frequenciaIgnorandoPrimeira(texto: string): Record<string, number> {`

> Stub para editar: `ex04_frequencia_ignorando_primeira/solution_ex04_frequencia_ignorando_primeira.py` (Python) e `solution.ts` (TS).

