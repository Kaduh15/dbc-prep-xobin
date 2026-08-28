# Exercício 003 — Soma de Dois Números

## Descrição do Problema
Crie um programa que leia dois números e mostre a soma entre eles.

## Parâmetros e Tipos Esperados
- `a: float` — primeiro número (int ou float; o retorno é float).
- `b: float` — segundo número.

## Formato do Retorno
- `float`: a soma `a + b`.

## Casos de Exemplo
```
Input: (2, 5)      Output: 7.0
Input: (-3, 8)     Output: 5.0
Input: (1.5, 2.5)  Output: 4.0
Input: (0, 0)      Output: 0.0
```

## Casos de Teste (todos, incluindo extremos)
```
((2, 5), 7.0)
((-3, 8), 5.0)
((1.5, 2.5), 4.0)
((0, 0), 0.0)
((-4, -6), -10.0)
((0, 5), 5.0)
((-1.25, 2.75), 1.5)
((10, 0), 10.0)```

## Edge Cases / Extremos
Suporta números negativos (soma de dois negativos é mais negativa). Soma com zero (identidade aditiva: `a + 0 = a`). Soma de decimais exatos; cuidado com arredondamento binário (ex.: `0.1 + 0.2` não é exatamente `0.3`).

## Abordagem / Dica
Retorne simplesmente `a + b`. Para casos decimais compare com tolerância (`pytest.approx` / `toBeCloseTo`) quando necessário.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def somar(a: float, b: float) -> float:`
- **TypeScript**: `export function somar(a: number, b: number): number {`

> Stub para editar: `ex003_soma/solution_ex003_soma.py` (Python) e `solution.ts` (TS).
