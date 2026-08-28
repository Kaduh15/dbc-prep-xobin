# Exercício 12 — Contar Vogais

## Descrição do Problema
Dada uma string, retorne quantas vogais (a, e, i, o, u) ela tem, ignorando maiúsculas.

## Parâmetros e Tipos Esperados
- texto: str

## Formato do Retorno
- int: quantidade de vogais

## Casos de Exemplo
```python
# (args) -> esperado
    (('hello',), 2),
    (('',), 0),
    (('AEIOU',), 5),
    (('try',), 0),
    (('banana',), 3),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('hello',), 2),
    (('',), 0),
    (('AEIOU',), 5),
    (('try',), 0),
    (('banana',), 3),
    (('Olá',), 1),
```

## Edge Cases / Extremos
String vazia (0); sem vogais (consoantes); maiúsculas (AEIOU); vogais repetidas (banana); acentos não contam (á ≠ a).

## Abordagem / Dica
Baixe tudo para minúsculas e conte os caracteres que estão no conjunto "aeiou".

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def contar_vogais(texto: str) -> int:`
- **TypeScript**: `export function contarVogais(texto: string): number {`

> Stub para editar: `ex12_contar_vogais/solution_ex12_contar_vogais.py` (Python) e `solution.ts` (TS).

