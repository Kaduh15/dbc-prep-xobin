# Ex 031 — Preço da passagem

**Enunciado original (Curso em Vídeo / Guanabara):** “Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.”

## Descrição
Calcula o preço da passagem conforme a distância: R$ 0,50/km para distâncias de até 200 km, e R$ 0,45/km para distâncias acima de 200 km.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| distancia_km | float | Distância da viagem em quilômetros. |

## Formato do Retorno
Float com o preço da passagem em R$.
- `0.50 * d` se `d <= 200`; senão `0.45 * d`.

## Casos de Exemplo
```py
preco_passagem(50)  ->  25.0
```
```py
preco_passagem(200)  ->  100.0
```
```py
preco_passagem(201)  ->  90.45
```
```py
preco_passagem(500)  ->  225.0
```
```py
preco_passagem(0)  ->  0.0
```
## Restrições / Edge Cases
- O limite de 200 km usa a tarifa de R$ 0,50 (inclusive).
- Acima de 200 km, R$ 0,45/km.

## Assinatura canônica
```python
def preco_passagem(distancia_km: float) -> float:
```
```ts
export function precoPassagem(distanciaKm: number): number
```
