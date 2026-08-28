# Exercício 009 — Tabuada

## Descrição do Problema
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

## Parâmetros e Tipos Esperados
- `n: int` — número inteiro cuja tabuada será exibida.

## Formato do Retorno
- `list[int]`: uma lista com 10 elementos contendo `n * 1, n * 2, ..., n * 10`.

## Casos de Exemplo
```
Input: 7   Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
Input: 2   Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Input: 0   Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Casos de Teste (todos, incluindo extremos)
```
((7,), [7, 14, 21, 28, 35, 42, 49, 56, 63, 70])
((2,), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
((0,), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
((-3,), [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30])
((1,), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
((10,), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
((-1,), [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
- Teste extra: `len(tabuada(5)) == 10` (sempre 10 elementos).```

## Edge Cases / Extremos
Número zero retorna uma lista de dez zeros (multiplicação por 0). Números negativos `-1`/`-3` produzem tabuada negativa de `-n*1` a `-n*10`. Elemento unitário `1` é a identidade `1..10`. A lista deve ter exatamente 10 elementos.

## Abordagem / Dica
Itere de `1` a `10` multiplicando por `n`. Em Python: `[n * i for i in range(1, 11)]`; em TS/JS: `Array.from({length: 10}, (_, i) => n * (i + 1))`. Guarde a quantidade fixa de 10 elementos.

## Complexidade
- Tempo O(10) = O(1), espaço O(10) = O(1).

## Assinatura Canônica
- **Python**: `def tabuada(n: int) -> list[int]:`
- **TypeScript**: `export function tabuada(n: number): number[] {`

> Stub para editar: `ex009_tabuada/solution_ex009_tabuada.py` (Python) e `solution.ts` (TS).
