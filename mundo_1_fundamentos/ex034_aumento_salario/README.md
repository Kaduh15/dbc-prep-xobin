# Ex 034 — Aumento de salário

**Enunciado original (Curso em Vídeo / Guanabara):** “Pergunte o salário de um funcionário e calcule o aumento: +10% para salários superiores a R$ 1250,00 e +15% para inferiores ou iguais.”

## Descrição
Calcula o novo salário após o aumento: +15% para salários menores ou iguais a R$ 1250,00; +10% acima. Resultado arredondado a 2 casas decimais.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| salario | float | Salário atual em R$. |

## Formato do Retorno
Float com o novo salário (`salario * 1.15` se `<= 1250`; senão `salario * 1.10`), arredondado a 2 casas.

## Assinatura canônica
```python
def novo_salario(salario: float) -> float:
```
```ts
export function novoSalario(salario: number): number
```

## Casos de Exemplo
```py
f(1000,)  ->  1150.0
```
```py
f(1250,)  ->  1437.5
```
```py
f(1250.01,)  ->  1375.01
```
```py
f(1500,)  ->  1650.0
```

## Casos de Teste (todos, incluindo extremos)
```py
    (1000,),  # -> 1150.0
    (1250,),  # -> 1437.5
    (1250.01,),  # -> 1375.01
    (1500,),  # -> 1650.0
    (800,),  # -> 920.0
    (0,),  # -> 0.0
    (2000,),  # -> 2200.0
    (10000,),  # -> 11000.0
    (10,),  # -> 11.5
```

## Edge Cases / Extremos
Exatamente R$ 1250,00 recebe aumento de 15% (inferiores **ou iguais**). Acima recebe 10%. Arredondamento a 2 casas (ex.: 1250.01 -> 1375.01, pois 1250.01×1.10 ≈ 1375.011).

## Abordagem / Dica
Condicional de percentual por faixa; multiplicar e arredondar a 2 casas (`round(…,2)` em Python / `Math.round(x*100)/100` em JS).

## Complexidade
- Tempo O(1), espaço O(1)
