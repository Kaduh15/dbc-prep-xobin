# Exercício 006 — Dobro, Triplo e Raiz Quadrada

## Descrição do Problema
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

## Parâmetros e Tipos Esperados
- `n: float` — número de entrada (deve ser >= 0 para raiz quadrada real).

## Formato do Retorno
- `tuple[float, float, float]` na ordem `(dobro, triplo, raiz)`:
  - `dobro = n * 2`
  - `triplo = n * 3`
  - `raiz = n ** 0.5`

## Assinatura Canônica
- **Python**: `dobro_triplo_raiz(n: float) -> tuple[float, float, float]`
- **TypeScript**: `dobroTriploRaiz(n: number): [number, number, number]`

## Casos de Exemplo
```
Input: 9
Output: (18.0, 27.0, 3.0)

Input: 4
Output: (8.0, 12.0, 2.0)

Input: 0
Output: (0.0, 0.0, 0.0)
```

## Restrições / Edge Cases
- Para números negativos a raiz quadrada não é um número real.
- Testes de raiz/divisões devem usar comparação aproximada quando necessário.