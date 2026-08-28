# Ex 029 — Multa por velocidade

**Enunciado original (Curso em Vídeo / Guanabara):** “Leia a velocidade de um carro. Se ultrapassar 80 km/h, mostre que foi multado; a multa custa R$ 7,00 por cada km acima do limite.”

## Descrição
Se a velocidade ultrapassar 80 km/h, multa de R$ 7,00/km acima do limite; caso contrário, multa zero.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| velocidade | float | Velocidade registrada do carro (km/h). |

## Formato do Retorno
Float com o valor da multa: `(velocidade - 80) * 7` se `velocidade > 80`; senão `0.0`.

## Assinatura canônica
```python
def multa_velocidade(velocidade: float) -> float:
```
```ts
export function multaVelocidade(velocidade: number): number
```

## Casos de Exemplo
```py
f(80,)  ->  0.0
```
```py
f(81,)  ->  7.0
```
```py
f(90,)  ->  70.0
```
```py
f(200,)  ->  840.0
```
```py
f(79.9,)  ->  0.0
```

## Casos de Teste (todos, incluindo extremos)
```py
    (80,),  # -> 0.0
    (81,),  # -> 7.0
    (90,),  # -> 70.0
    (200,),  # -> 840.0
    (79.9,),  # -> 0.0
    (-5,),  # -> 0.0
    (0,),  # -> 0.0
    (81.5,),  # -> 10.5
    (80.5,),  # -> 3.5
    (100,),  # -> 140.0
    (79,),  # -> 0.0
```

## Edge Cases / Extremos
Apenas velocidades **estritamente maiores** que 80 geram multa (80 exato = multa zero). Velocidades negativas e zero retornam `0.0`. Decimais acima do limite (ex.: 81.5 -> R$ 10.50) são suportados.

## Abordagem / Dica
Condicional: se `velocidade > 80`, `(velocidade - 80) * 7`; senão `0.0`.

## Complexidade
- Tempo O(1), espaço O(1)
