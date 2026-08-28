# EX38 — Comparando números

## Descrição
Escreva um programa que leia dois números inteiros e os compare, mostrando qual é maior ou se são iguais.

## Parâmetros e Tipos
- `a` (int) — primeiro número.
- `b` (int) — segundo número.

## Retorno
`str` — `"primeiro maior"` se `a > b`, `"segundo maior"` se `b > a`, `"iguais"` se forem iguais.

## Casos de Exemplo
```python
comparar_numeros(5, 2)  -> "primeiro maior"
comparar_numeros(2, 5)  -> "segundo maior"
comparar_numeros(3, 3)  -> "iguais"
comparar_numeros(-1, 4) -> "segundo maior"
```

## Casos de Teste (todos, incluindo extremos)
```python
((5, 2), 'primeiro maior'), ((2, 5), 'segundo maior'),
((3, 3), 'iguais'), ((-1, 4), 'segundo maior'), ((-2, -2), 'iguais'),
# extremos
((0, 0), 'iguais'), ((-3, -7), 'primeiro maior'),
((5, -10), 'primeiro maior'), ((0, -1), 'primeiro maior'),
((-10, -20), 'primeiro maior'),
```

## Edge Cases / Extremos
- Igualdade (`a == b`) retorna exatamente `"iguais"`, inclusive com zeros e negativos.
- Aceita inteiros negativos (comparação direta com `<` / `>` funciona para negativos).
- `0 > -1` → `"primeiro maior"`.

## Abordagem / Dica
Basta comparar com `>` e `<` (ou `elif` na ordem `a > b`, `b > a`, senão `iguais`).

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def comparar_numeros(a: int, b: int) -> str:`
- **TypeScript**: `export function compararNumeros(a: number, b: number): string`

> Stub para editar: `ex038_comparar_numeros/solution_ex038_comparar_numeros.py` (Python) e `solution.ts` (TS).
