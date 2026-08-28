# Exercício 06 — Contar Caracteres

## Descrição do Problema
Dada uma string, retorne um dicionário/mapa contando quantas vezes cada caractere aparece (espaços e pontuação contam).

## Parâmetros e Tipos Esperados
- texto: str

## Formato do Retorno
- dict: {caractere: contagem}

## Casos de Exemplo
```python
# (args) -> esperado
    (('banana',), {'b': 1, 'a': 3, 'n': 2}),
    (('',), {}),
    (('a',), {'a': 1}),
    (('ab a',), {'a': 2, 'b': 1, ' ': 1}),
    (('aba',), {'a': 2, 'b': 1}),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('banana',), {'b': 1, 'a': 3, 'n': 2}),
    (('',), {}),
    (('a',), {'a': 1}),
    (('ab a',), {'a': 2, 'b': 1, ' ': 1}),
    (('aba',), {'a': 2, 'b': 1}),
```

## Edge Cases / Extremos
String vazia (retorna {}); um único caractere; espaços e símbolos contam; caracteres repetidos; todos iguais.

## Abordagem / Dica
Itere e incremente um acumulador por caractere (d.get em Python; ?? em TS).

## Complexidade
- Tempo O(n), espaço O(k) (k = caracteres distintos)

## Assinatura Canônica
- **Python**: `def contar_caracteres(texto: str) -> dict:`
- **TypeScript**: `export function contarCaracteres(texto: string): Record<string, number> {`

> Stub para editar: `ex06_contar_caracteres/solution_ex06_contar_caracteres.py` (Python) e `solution.ts` (TS).

