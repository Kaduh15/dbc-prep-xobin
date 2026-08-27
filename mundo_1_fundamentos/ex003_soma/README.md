# Exercício 003 — Soma de Dois Números

## Descrição do Problema
Crie um programa que leia dois números e mostre a soma entre eles.

## Parâmetros e Tipos Esperados
- `a: float` — primeiro número (int ou float; o retorno é float).
- `b: float` — segundo número.

## Formato do Retorno
- `float`: a soma `a + b`.

## Assinatura Canônica
- **Python**: `somar(a: float, b: float) -> float`
- **TypeScript**: `somar(a: number, b: number): number`

## Casos de Exemplo
```
Input: (2, 5)
Output: 7.0

Input: (-3, 8)
Output: 5.0

Input: (1.5, 2.5)
Output: 4.0

Input: (0, 0)
Output: 0.0
```

## Restrições / Edge Cases
- Suporta números negativos e decimais.
- Soma de zeros retorna 0.0.