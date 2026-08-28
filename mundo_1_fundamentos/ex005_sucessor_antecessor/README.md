# Exercício 005 — Sucessor e Antecessor

## Descrição do Problema
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

## Parâmetros e Tipos Esperados
- `n: int` — número inteiro de entrada (pode ser negativo).

## Formato do Retorno
- `tuple[int, int]` na ordem `(antecessor, sucessor)`, ou seja `(n - 1, n + 1)`.

## Casos de Exemplo
```
Input: 10   Output: (9, 11)
Input: 0    Output: (-1, 1)
Input: -5   Output: (-6, -4)
```

## Casos de Teste (todos, incluindo extremos)
```
((10,), (9, 11))
((0,), (-1, 1))
((-5,), (-6, -4))
((1,), (0, 2))
((2,), (1, 3))
((-1,), (-2, 0))
((100,), (99, 101))
((-100,), (-101, -99))```

## Edge Cases / Extremos
Zero é um caso de borda válido (antecessor/sucessor de 0 são ±1). Negativos: antecessor é 'mais negativo' e sucessor é 'menos negativo'. Ordem do retorno é importante: `(n-1, n+1)` e não o inverso.

## Abordagem / Dica
Atenção à ordem do retorno: primeiro antecessor (`n-1`), depois sucessor (`n+1`). É uma operação O(1) de aritmética de inteiros.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def sucessor_antecessor(n: int) -> tuple[int, int]:`
- **TypeScript**: `export function sucessorAntecessor(n: number): [number, number] {`

> Stub para editar: `ex005_sucessor_antecessor/solution_ex005_sucessor_antecessor.py` (Python) e `solution.ts` (TS).
