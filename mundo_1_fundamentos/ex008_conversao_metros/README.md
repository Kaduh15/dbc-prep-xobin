# Exercício 008 — Conversão de Metros para Centímetros e Milímetros

## Descrição do Problema
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

## Parâmetros e Tipos Esperados
- `metros: float` — valor em metros (>= 0).

## Formato do Retorno
- `tuple[float, float]` na ordem `(centimetros, milimetros)`:
  - `centimetros = metros * 100`
  - `milimetros = metros * 1000`

## Casos de Exemplo
```
Input: 1    Output: (100.0, 1000.0)
Input: 2.5  Output: (250.0, 2500.0)
Input: 0    Output: (0.0, 0.0)
```

## Casos de Teste (todos, incluindo extremos)
```
((1,), (100.0, 1000.0))
((2.5,), (250.0, 2500.0))
((0,), (0.0, 0.0))
((0.5,), (50.0, 500.0))
((0.25,), (25.0, 250.0))
((10,), (1000.0, 10000.0))
((1.5,), (150.0, 1500.0))```

## Edge Cases / Extremos
Valor zero retorna `(0.0, 0.0)`. Valores fracionários (`0.25`, `0.5`, `1.5`) — multiplicações por 100/1000 preservam exatidão nesses casos. Ordem do retorno: centímetros (`*100`) primeiro, depois milímetros (`*1000`).

## Abordagem / Dica
Multiplicação direta por `100` (cm) e `1000` (mm), na ordem `(cm, mm)`. Para decimais `0.5/0.25` os produtos são exatos; compare com tolerância quando necessário.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def converter_metros(metros: float) -> tuple[float, float]:`
- **TypeScript**: `export function converterMetros(metros: number): [number, number] {`

> Stub para editar: `ex008_conversao_metros/solution_ex008_conversao_metros.py` (Python) e `solution.ts` (TS).
