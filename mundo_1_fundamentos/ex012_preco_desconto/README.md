# Exercício 012 — Preço com Desconto

## Descrição do Problema
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

## Parâmetros e Tipos Esperados
- `preco: float` — preço original do produto (>= 0).
- `desconto: float = 0.05` — taxa de desconto (padrão 5%, fracionário).

## Formato do Retorno
- `float`: o preço com desconto, `preco * (1 - desconto)`.

## Assinatura Canônica
- **Python**: `preco_com_desconto(preco: float, desconto: float = 0.05) -> float`
- **TypeScript**: `precoComDesconto(preco: number, desconto: number = 0.05): number`

## Casos de Exemplo
```
Input: (100)            -> desconto padrão 5%
Output: 95.0

Input: (80)             -> desconto padrão 5%
Output: 76.0

Input: (100, 0.10)      -> desconto de 10%
Output: 90.0

Input: (0, 0.05)
Output: 0.0
```

## Restrições / Edge Cases
- Desconto padrão de 5% (0.05), conforme o enunciado.
- A taxa é fracionária (10% = 0.10).
- Comparações com float devem usar tolerância quando houver arredondamento.