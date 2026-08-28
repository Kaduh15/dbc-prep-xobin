# EX36 — Aprovação de empréstimo bancário

## Descrição
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. Dados o valor da casa, o salário do comprador e o prazo em anos, calcula-se a prestação mensal (`valor_casa / (anos * 12)`) e o empréstimo é aprovado somente se a prestação **não exceder 30% do salário** (limite inclusivo).

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| valor_casa | float | Valor do imóvel em R$. |
| salario | float | Salário mensal do comprador em R$. |
| anos | int | Prazo do financiamento em anos (inteiro, > 0). |

## Formato do Retorno
- `prestacao_mensal(valor_casa, anos)` → `float` (prestação mensal = `valor_casa / (anos * 12)`).
- `aprova_emprestimo(valor_casa, salario, anos)` → `bool` (`True` se `prestacao <= salario * 0.30`).

## Casos de Exemplo
```python
prestacao_mensal(100000, 20)          -> 416.6666666666667
aprova_emprestimo(100000, 2000, 20)   -> True
aprova_emprestimo(200000, 2000, 20)   -> False
aprova_emprestimo(120000, 5000, 10)   -> True
aprova_emprestimo(80000, 1500, 10)    -> False
```

## Casos de Teste (todos, incluindo extremos)
```python
# prestacao_mensal
((100000, 20), 416.6666666666667),
((30000, 1), 2500.0),
((240000, 20), 1000.0),
((12000, 1), 1000.0),
((100, 1), 8.333333333333334),
((0, 5), 0.0),
((600000, 50), 1000.0),
# aprova_emprestimo
((100000, 2000, 20), True),
((200000, 2000, 20), False),
((120000, 5000, 10), True),
((80000, 1500, 10), False),
((72000, 2000, 10), True),   # prestacao == 30% do salario (limite exato)
((30000, 2000, 5), True),    # prestacao (500) < 30% (600)
((60000, 2000, 5), False),   # prestacao (1000) > 30% (600)
((72001, 2000, 10), False),  # ligeiramente acima do limite
((1000, 0, 10), False),      # salario zero
```

## Edge Cases / Extremos
- Prestação exatamente igual a 30% do salário → **aprovado** (limite inclusivo, `<=`).
- Prestação um centavo acima do limite → reprovado (ex.: `72001`).
- Salário zero → qualquer prestação positiva é reprovada.
- `anos == 1` (12 meses) e prazos longos (50 anos) verificam a divisão por 12.
- Valor da casa zero → prestação 0 e aprovação (não coberta por divisão por zero, `anos > 0`).

## Abordagem / Dica
1. `prestacao = valor_casa / (anos * 12)`.
2. Comparar `prestacao <= salario * 0.30`. Usar `<=` para tornar o limite inclusivo.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def prestacao_mensal(valor_casa: float, anos: int) -> float:` e `def aprova_emprestimo(valor_casa: float, salario: float, anos: int) -> bool:`
- **TypeScript**: `export function prestacaoMensal(valorCasa: number, anos: number): number` e `export function aprovaEmprestimo(valorCasa: number, salario: number, anos: number): boolean`

> Stub para editar: `ex036_emprestimo_bancario/solution_ex036_emprestimo_bancario.py` (Python) e `solution.ts` (TS).
