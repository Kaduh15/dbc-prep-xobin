# Ex 036 — Aprovação de empréstimo

**Enunciado original (Curso em Vídeo / Guanabara):** “Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.”

## Descrição
Aprova um financiamento imobiliário. A prestação mensal é o valor da casa dividido pelo total de meses do financiamento, e o empréstimo é aprovado somente se a prestação não exceder 30% do salário mensal do comprador.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| valor_casa | float | Valor do imóvel em R$. |
| salario | float | Salário mensal do comprador em R$. |
| anos | int | Prazo do financiamento em anos (inteiro, > 0). |

## Formato do Retorno
Booleano `True` se o empréstimo é aprovado; `False` caso contrário.
- `prestacao = valor_casa / (anos * 12)`.
- Aprovado se `prestacao <= salario * 0.30`.

## Casos de Exemplo
```py
aprova_emprestimo(100000, 2000, 20)  ->  True
aprova_emprestimo(200000, 2000, 20)  ->  False
aprova_emprestimo(120000, 5000, 10)  ->  True
aprova_emprestimo(80000, 1500, 10)  ->  False
```

## Restrições / Edge Cases
- `anos` deve ser maior que zero (evitar divisão por zero).
- Aprovação inclui o caso em que a prestação é exatamente 30% do salário (limite inclusive).
- Valores são monetários em R$.

## Assinatura canônica
```python
def aprova_emprestimo(valor_casa: float, salario: float, anos: int) -> bool:
```
```ts
export function aprovaEmprestimo(valorCasa: number, salario: number, anos: number): boolean
```