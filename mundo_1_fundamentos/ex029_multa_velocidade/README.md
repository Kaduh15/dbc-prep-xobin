# Ex 029 — Multa por velocidade

**Enunciado original (Curso em Vídeo / Guanabara):** “Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.”

## Descrição
Calcula o valor da multa de trânsito. Se a velocidade ultrapassar 80 km/h, multa de R$ 7,00 por km acima do limite; caso contrário, multa é zero.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| velocidade | float | Velocidade registrada do carro (km/h). |

## Formato do Retorno
Float com o valor da multa em R$.
- `(velocidade - 80) * 7` se velocidade > 80; senão `0.0`.

## Casos de Exemplo
```py
multa_velocidade(80)  ->  0.0
```
```py
multa_velocidade(81)  ->  7.0
```
```py
multa_velocidade(90)  ->  70.0
```
```py
multa_velocidade(200)  ->  840.0
```
```py
multa_velocidade(79.9)  ->  0.0
```
## Restrições / Edge Cases
- Apenas velocidades **estritamente maiores** que 80 geram multa.
- Velocidades negativas retornam `0.0` (não há multa).

## Assinatura canônica
```python
def multa_velocidade(velocidade: float) -> float:
```
```ts
export function multaVelocidade(velocidade: number): number
```
