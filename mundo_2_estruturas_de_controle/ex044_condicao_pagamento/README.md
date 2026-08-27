# EX44 — Condição de Pagamento

## Descrição
Elabore um programa que calcule o valor a ser pago por um produto, considerando o preço normal e a condição de pagamento escolhida, de acordo com a tabela: à vista dinheiro/cheque → 10% de desconto; à vista no cartão → 5% de desconto; em até 2x no cartão → preço normal; 3x ou mais no cartão → 20% de juros.

## Parâmetros e Tipos
- `preco` (float) — preço normal do produto.
- `condicao` (str) — uma das condições: `dinheiro`, `cartao_avista`, `2x` ou `3x_mais`.

## Retorno
`float` — valor final a pagar conforme a condição escolhida.

## Casos de Exemplo
```python
valor_final(100, 'dinheiro')     -> 90.0
valor_final(100, 'cartao_avista')-> 95.0
valor_final(100, '2x')           -> 100.0
valor_final(100, '3x_mais')      -> 120.0
valor_final(80, 'dinheiro')      -> 72.0"
```

## Restrições / Edge Cases
- Chaves canônicas: `dinheiro`=10% off; `cartao_avista`=5% off; `2x`=preço normal; `3x_mais`=20% juros.
- Condição desconhecida lança `ValueError`.

## Assinatura canônica

```python
def valor_final(preco: float, condicao: str) -> float:
```

```typescript
valorFinal(preco: number, condicao: string): number
```
