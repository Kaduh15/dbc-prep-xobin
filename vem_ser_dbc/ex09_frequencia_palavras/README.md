# Exercício 09 — Frequência de Palavras (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma frase, retorne um dicionário com a contagem de cada palavra (case-insensitive, ignorando pontuação).

## Parâmetros e Tipos Esperados
- Assinatura: `def frequencia_palavras(frase: str) -> dict:`

## Formato do Retorno
- dict: {palavra: contagem}

## Casos de Exemplo
```python
    (('',), {}),
    (('ola ola',), {'ola': 2}),
    (('Ola OLA ola',), {'ola': 3}),
    (('casa, jardim! casa.',), {'casa': 2, 'jardim': 1}),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('',), {}),
    (('ola ola',), {'ola': 2}),
    (('Ola OLA ola',), {'ola': 3}),
    (('casa, jardim! casa.',), {'casa': 2, 'jardim': 1}),
    (('a b c',), {'a': 1, 'b': 1, 'c': 1}),
    (('olá mundo, olá',), {'olá': 2, 'mundo': 1}),
```

## Edge Cases / Extremos
Frase vazia (→ {}); case-insensitive (Ola/ola); pontuação ignorada; palavra única repetida; acentos (olá).

## Abordagem / Dica
Normalize para minúsculas, extraia sequências de letras (regex) e conte cada ocorrência.

## Complexidade
- Tempo O(n), espaço O(k)

## Assinatura Canônica
- **Python**: `def frequencia_palavras(frase: str) -> dict:`
- **TypeScript**: `export function frequenciaPalavras(frase: string): Record<string, number> {`

> Stub para editar: `ex09_frequencia_palavras/solution_ex09_frequencia_palavras.py` (Python) e `solution.ts` (TS).

