# Exercício 008 — Conversão de Metros para Centímetros e Milímetros

## Descrição do Problema
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

## Parâmetros e Tipos Esperados
- `metros: float` — valor em metros (>= 0).

## Formato do Retorno
- `tuple[float, float]` na ordem `(centimetros, milimetros)`:
  - `centimetros = metros * 100`
  - `milimetros = metros * 1000`

## Assinatura Canônica
- **Python**: `converter_metros(metros: float) -> tuple[float, float]`
- **TypeScript**: `converterMetros(metros: number): [number, number]`

## Casos de Exemplo
```
Input: 1
Output: (100.0, 1000.0)

Input: 2.5
Output: (250.0, 2500.0)

Input: 0
Output: (0.0, 0.0)
```

## Restrições / Edge Cases
- Capacidade com metros decimais.
- Valor zero retorna zeros.