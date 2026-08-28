# EX44 — Condição de pagamento

## Descrição
Calcule o valor a ser pago por um produto conforme o preço normal e a condição escolhida: `dinheiro` → 10% de desconto; `cartao_avista` → 5% de desconto; `2x` → preço normal; `3x_mais` → 20% de juros.

## Parâmetros e Tipos
- `preco` (float) — preço normal do produto.
- `condicao` (str) — uma das chaves canônicas: `dinheiro`, `cartao_avista`, `2x`, `3x_mais`.

## Retorno
`float` — valor final a pagar conforme a condição.

## Casos de Exemplo
```python
valor_final(100, 'dinheiro')      -> 90.0
valor_final(100, 'cartao_avista') -> 95.0
valor_final(100, '2x')            -> 100.0
valor_final(100, '3x_mais')       -> 120.0
valor_final(80, 'dinheiro')       -> 72.0
```

## Casos de Teste (todos, incluindo extremos)
```python
# valida
((100, 'dinheiro'), 90.0), ((100, 'cartao_avista'), 95.0),
((100, '2x'), 100.0), ((100, '3x_mais'), 120.0), ((80, 'dinheiro'), 72.0),
# extremos
((0, 'dinheiro'), 0.0), ((80, 'cartao_avista'), 76.0),
((200, '2x'), 200.0), ((200, '3x_mais'), 240.0),
((50, 'dinheiro'), 45.0), ((10, 'cartao_avista'), 9.5),
# invalidas -> ValueError
['parcelado', '', 'cheque', 'DINHEIRO']
```

## Edge Cases / Extremos
- Preço zero → 0.0 em todas as condições.
- `cartao_avista` com preços quebrados (10 → 9.5) verifica multiplicação por 0.95.
- Condições desconhecidas (inclusive vazia, com letra maiúscula ou qualquer outra string) → `ValueError`. Chaves são **sensíveis a caixa**.

## Abordagem / Dica
Mapear cada condição para o fator: `0.9`, `0.95`, `1.0`, `1.2`. `switch`/`if` com `default`/`else` lançando `ValueError`.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def valor_final(preco: float, condicao: str) -> float:`
- **TypeScript**: `export function valorFinal(preco: number, condicao: string): number`

> Stub para editar: `ex044_condicao_pagamento/solution_ex044_condicao_pagamento.py` (Python) e `solution.ts` (TS).
