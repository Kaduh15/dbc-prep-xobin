# Ex 031 — Preço da passagem

**Enunciado original (Curso em Vídeo / Guanabara):** “Desenvolva um programa que pergunte a distância de uma viagem em km e calcule o preço da passagem: R$ 0,50/km para viagens de até 200 km e R$ 0,45/km para as mais longas.”

## Descrição
Calcula o preço da passagem conforme a distância: R$ 0,50/km até 200 km; R$ 0,45/km acima.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| distancia_km | float | Distância da viagem em km. |

## Formato do Retorno
Float: `0.50 * d` se `d <= 200`; senão `0.45 * d`.

## Assinatura canônica
```python
def preco_passagem(distancia_km: float) -> float:
```
```ts
export function precoPassagem(distanciaKm: number): number
```

## Casos de Exemplo
```py
f(50,)  ->  25.0
```
```py
f(200,)  ->  100.0
```
```py
f(201,)  ->  90.45
```
```py
f(500,)  ->  225.0
```
```py
f(0,)  ->  0.0
```

## Casos de Teste (todos, incluindo extremos)
```py
    (50,),  # -> 25.0
    (200,),  # -> 100.0
    (201,),  # -> 90.45
    (500,),  # -> 225.0
    (0,),  # -> 0.0
    (199.9,),  # -> 99.95
    (1000,),  # -> 450.0
    (199,),  # -> 99.5
    (1,),  # -> 0.5
    (250,),  # -> 112.5
```

## Edge Cases / Extremos
Limite de 200 km usa a tarifa de R$ 0,50 (inclusive: 200 -> R$ 100,00). Logo acima usa R$ 0,45/km (201 -> R$ 90,45). Distâncias decimais e distância zero suportadas.

## Abordagem / Dica
Condicional de tarifa por faixa e multiplicação pela distância.

## Complexidade
- Tempo O(1), espaço O(1)
