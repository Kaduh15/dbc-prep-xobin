# Exercício 07 — Maior e Menor da Lista

## Descrição do Problema
Dada uma lista de números, retorne (maior, menor). Lista vazia -> None.

## Parâmetros e Tipos Esperados
- nums: list[number].

## Formato do Retorno
- (maior, menor) ou None

## Casos de Exemplo
```text
[
    ([[3, 1, 4, 1, 5]], (5, 1)),
    ([[-1, 2, -3]], (2, -3)),
    ([[7]], (7, 7)),
    ([[]], None),
    ([[10, 10]], (10, 10))
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def maior_menor(nums: list) -> tuple | None:`
- Assinatura em TypeScript: `export function maiorMenor(nums: number[]): [number, number] | null {`
