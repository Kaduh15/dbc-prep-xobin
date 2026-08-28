# Exercício 03 — Anagrama

## Descrição do Problema
Dadas duas strings, retorne True se uma for um anagrama da outra (mesmas letras, ignorando espaços e caixa).

## Parâmetros e Tipos Esperados
- a: str, b: str

## Formato do Retorno
- bool: True se são anagramas

## Casos de Exemplo
```python
# (args) -> esperado
    (('listen', 'silent'), True),
    (('triangle', 'integral'), True),
    (('cat', 'dog'), False),
    (('hello', 'hello'), True),
    (('', ''), True),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('listen', 'silent'), True),
    (('triangle', 'integral'), True),
    (('cat', 'dog'), False),
    (('hello', 'hello'), True),
    (('', ''), True),
    (('a', 'b'), False),
    (('anagram', 'nag a ram'), True),
    (('python', 'java'), False),
```

## Edge Cases / Extremos
Duas strings vazias (são anagramas); strings iguais; comprimentos diferentes; espaços no meio de um dos lados; uma letra vs outra.

## Abordagem / Dica
Ordene as letras (após remover espaços e minúsculas) e compare: anagramas têm o mesmo multiconjunto de caracteres.

## Complexidade
- Tempo O(a·log a + b·log b) com ordenação, espaço O(a+b)

## Assinatura Canônica
- **Python**: `def anagrama(a: str, b: str) -> bool:`
- **TypeScript**: `export function anagrama(a: string, b: string): boolean {`

> Stub para editar: `ex03_anagrama/solution_ex03_anagrama.py` (Python) e `solution.ts` (TS).

