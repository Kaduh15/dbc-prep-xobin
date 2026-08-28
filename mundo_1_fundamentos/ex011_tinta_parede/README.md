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

## Casos de Exemplo
```
Input: (2, 2)   Output: (4.0, 2.0)
Input: (7, 4)   Output: (28.0, 14.0)
Input: (0, 5)   Output: (0.0, 0.0)
```

## Casos de Teste (todos, incluindo extremos)
```
((2, 2), (4.0, 2.0))
((7, 4), (28.0, 14.0))
((0, 5), (0.0, 0.0))
((2.5, 4), (10.0, 5.0))
((3, 3), (9.0, 4.5))
((4, 2.5), (10.0, 5.0))
((0.5, 0.5), (0.25, 0.125))```

## Edge Cases / Extremos
Cada litro cobre exatamente 2 m² (`litros = area / 2`). Área zero (largura ou altura 0) implica zero litros. Dimensões decimais (`0.5×0.5`) dão área e litros fracionários exatos nesses casos. Ordem do retorno: `(area, litros)`.

## Abordagem / Dica
Calcule `area = largura * altura` e depois `litros = area / 2`. Considere ler a largeza primeiro — caso troque os operandos a área é a mesma (comutativa), mas a ordem do retorno não muda.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def calcular_tinta(largura: float, altura: float) -> tuple[float, float]:`
- **TypeScript**: `export function calcularTinta(largura: number, altura: number): [number, number] {`

> Stub para editar: `ex011_tinta_parede/solution_ex011_tinta_parede.py` (Python) e `solution.ts` (TS).
