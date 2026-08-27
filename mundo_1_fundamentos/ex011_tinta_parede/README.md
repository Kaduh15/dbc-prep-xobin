# Exercício 011 — Pintura de Parede

## Descrição do Problema
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

## Parâmetros e Tipos Esperados
- `largura: float` — largura da parede em metros (>= 0).
- `altura: float` — altura da parede em metros (>= 0).

## Formato do Retorno
- `tuple[float, float]` na ordem `(area, litros)`:
  - `area = largura * altura` (m²)
  - `litros = area / 2`

## Assinatura Canônica
- **Python**: `calcular_tinta(largura: float, altura: float) -> tuple[float, float]`
- **TypeScript**: `calcularTinta(largura: number, altura: number): [number, number]`

## Casos de Exemplo
```
Input: (2, 2)
Output: (4.0, 2.0)

Input: (7, 4)
Output: (28.0, 14.0)

Input: (0, 5)
Output: (0.0, 0.0)
```

## Restrições / Edge Cases
- Cada litro cobre exatamente 2 m².
- Dimensões podem ser decimais.
- Área zero implica zero litros.