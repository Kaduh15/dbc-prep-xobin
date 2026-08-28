# Exercício 007 — Média de Duas Notas

## Descrição do Problema
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

## Parâmetros e Tipos Esperados
- `n1: float` — primeira nota (0 a 10).
- `n2: float` — segunda nota (0 a 10).

## Formato do Retorno
- `float`: a média aritmética `(n1 + n2) / 2`.

## Casos de Exemplo
```
Input: (7, 7)      Output: 7.0
Input: (5.5, 8.5)  Output: 7.0
Input: (10, 2)     Output: 6.0
Input: (0, 0)      Output: 0.0
```

## Casos de Teste (todos, incluindo extremos)
```
((7, 7), 7.0)
((5.5, 8.5), 7.0)
((10, 2), 6.0)
((0, 0), 0.0)
((1, 9), 5.0)
((8.5, 7.5), 8.0)
((0, 10), 5.0)
((6.25, 6.25), 6.25)```

## Edge Cases / Extremos
Notas iguais produzem a própria nota. Notas decimais (ex.: `5.5 + 8.5 = 14`). Média de extremos (`0` e `10`) vale `5.0`. Notas fracionárias idênticas (`6.25`) dão exatamente `6.25`. Dois zeros dão `0.0`.

## Abordagem / Dica
Média aritmética simples: `(n1 + n2) / 2`. Use parênteses para somar antes de dividir. Para decimais compare com tolerância quando houver arredondamento binário.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def media_notas(n1: float, n2: float) -> float:`
- **TypeScript**: `export function mediaNotas(n1: number, n2: number): number {`

> Stub para editar: `ex007_media_notas/solution_ex007_media_notas.py` (Python) e `solution.ts` (TS).
