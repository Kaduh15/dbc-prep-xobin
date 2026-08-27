# Exercício 09 — Fatorial

## Descrição do Problema
Calcule n! = n*(n-1)*...*1. Por definição, 0! = 1.

## Parâmetros e Tipos Esperados
- n: int (>= 0).

## Formato do Retorno
- int

## Casos de Exemplo
```text
[
    ([0], 1),
    ([1], 1),
    ([5], 120),
    ([6], 720),
    ([10], 3628800)
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def fatorial(n: int) -> int:`
- Assinatura em TypeScript: `export function fatorial(n: number): number {`
