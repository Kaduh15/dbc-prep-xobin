# Ex 034 — Aumento de salário

**Enunciado original (Curso em Vídeo / Guanabara):** “Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.”

## Descrição
Calcula o novo salário após o aumento: +15% para salários menores ou iguais a R$ 1250,00, e +10% para salários acima de R$ 1250,00.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| salario | float | Salário atual em R$. |

## Formato do Retorno
Float com o novo salário (valor + percentual de aumento).
- `salario * 1.15` se `salario <= 1250`; senão `salario * 1.10`.

## Casos de Exemplo
```py
novo_salario(1000)  ->  1150.0
```
```py
novo_salario(1250)  ->  1437.5
```
```py
novo_salario(1250.01)  ->  1375.01
```
```py
novo_salario(1500)  ->  1650.0
```
## Restrições / Edge Cases
- Exatamente R$ 1250,00 recebe o aumento de 15% (inferiores **ou iguais**).
- Acima de R$ 1250,00 recebe 10%.

## Assinatura canônica
```python
def novo_salario(salario: float) -> float:
```
```ts
export function novoSalario(salario: number): number
```
