# Exercício 005 — Sucessor e Antecessor

## Descrição do Problema
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

## Parâmetros e Tipos Esperados
- `n: int` — número inteiro de entrada (pode ser negativo).

## Formato do Retorno
- `tuple[int, int]` na ordem `(antecessor, sucessor)`, ou seja `(n - 1, n + 1)`.

## Assinatura Canônica
- **Python**: `sucessor_antecessor(n: int) -> tuple[int, int]`
- **TypeScript**: `sucessorAntecessor(n: number): [number, number]`

## Casos de Exemplo
```
Input: 10
Output: (9, 11)

Input: 0
Output: (-1, 1)

Input: -5
Output: (-6, -4)
```

## Restrições / Edge Cases
- Suporta números negativos e o zero.
- Atenção à ordem do retorno: primeiro antecessor, depois sucessor.