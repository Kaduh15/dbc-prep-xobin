# Exercício 04 — Two Sum (Soma de Dois)

## Descrição do Problema
Dada uma lista de números e um alvo, retorne os índices (i<j) do PRIMEIRO par cuja soma é igual ao alvo. Retorne None/[] se não existir.

## Parâmetros e Tipos Esperados
- nums: list[int], alvo: int.

## Formato do Retorno
- list[int] (2 índices) ou None

## Casos de Exemplo
```text
[
    ([[2, 7, 11, 15], 9], [0, 1]),
    ([[3, 2, 4], 6], [1, 2]),
    ([[3, 3], 6], [0, 1]),
    ([[], 5], None),
    ([[1, 2, 3], 99], None)
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def two_sum(nums: list, alvo: int) -> list | None:`
- Assinatura em TypeScript: `export function twoSum(nums: number[], alvo: number): number[] | null {`
