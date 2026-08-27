# EX055 — Maior e menor peso

**Enunciado (Curso em Vídeo, DESAFIO 055):**
> Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

## Descrição
Dada uma lista de pesos (ex.: de cinco pessoas), retorne o maior e o menor valor.

## Parâmetros e Tipos
- `pesos` — `list[float]`: lista com os pesos lidos.

## Retorno
- `tuple[float, float]`: **`(maior peso, menor peso)`**, nesta ordem.

## Casos de Exemplo
```python
maior_menor_peso([70.5, 80.0, 55.3, 90.2, 62.1])  # (90.2, 55.3)
maior_menor_peso([50.0, 50.0])                    # (50.0, 50.0)
maior_menor_peso([100.0, 20.0, 40.0])             # (100.0, 20.0)
```

## Restrições / Edge Cases
- Valores **sempre retornam `(maior, menor)`** (não importa a ordem da lista).
- Empates (todos iguais): maior e menor são o mesmo valor.

## Assinatura canônica
```python
def maior_menor_peso(pesos: list[float]) -> tuple[float, float]
```
```typescript
export function maiorMenorPeso(pesos: number[]): [number, number]
```
