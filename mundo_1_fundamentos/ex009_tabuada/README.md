# Exercício 009 — Tabuada

## Descrição do Problema
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

## Parâmetros e Tipos Esperados
- `n: int` — número inteiro cuja tabuada será exibida.

## Formato do Retorno
- `list[int]`: uma lista com 10 elementos contendo `n * 1, n * 2, ..., n * 10`.

## Assinatura Canônica
- **Python**: `tabuada(n: int) -> list[int]`
- **TypeScript**: `tabuada(n: number): number[]`

## Casos de Exemplo
```
Input: 7
Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

Input: 2
Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Input: 0
Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Restrições / Edge Cases
- Trabalha com números negativos (tabuada negativa).
- Número zero retorna uma lista de dez zeros.