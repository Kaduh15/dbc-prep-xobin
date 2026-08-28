# Exercício 012 — Preço com Desconto

## Descrição do Problema
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

## Parâmetros e Tipos Esperados
- `preco: float` — preço original do produto (>= 0).
- `desconto: float = 0.05` — taxa de desconto (padrão 5%, fracionário).

## Formato do Retorno
- `float`: o preço com desconto, `preco * (1 - desconto)`.

## Casos de Exemplo
```
Input: (100)            -> desconto padrão 5%, Output: 95.0
Input: (80)             -> desconto padrão 5%, Output: 76.0
Input: (100, 0.10)      -> desconto de 10%,   Output: 90.0
Input: (0, 0.05)        Output: 0.0
```

## Casos de Teste (todos, incluindo extremos)
```
((100, 0.05), 95.0)   ((80, 0.05), 76.0)   ((100, 0.10), 90.0)
((0, 0.05), 0.0)       ((100,), 95.0)       ((200, 0.05), 190.0)
((50, 0.10), 45.0)     ((100, 0.00), 100.0) ((1, 1.0), 0.0)
((1, 0.5), 0.5)
- Caso `(100,)` exercita o desconto padrão de 5%. Taxa de 100% zera o preço.```

## Edge Cases / Extremos
Desconto padrão de `5%` (`0.05`). A taxa é fracionária: 10% = `0.10`. Taxa `0` devolve o preço original. Taxa `1.0` (100%) zera o preço. Taxa `0.5` (50%) devolve a metade. Comparações com float devem usar tolerância quando houver arredondamento.

## Abordagem / Dica
Retorne `preco * (1 - desconto)`. O parâmetro `desconto` tem default `0.05`; omiti-lo aplica 5%. Para taxas fracionárias exatas (0, 0.05, 0.1, 0.5, 1.0) o resultado é exato; use tolerância apenas se precisar de segurança com floats.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def preco_com_desconto(preco: float, desconto: float = 0.05) -> float:`
- **TypeScript**: `export function precoComDesconto(preco: number, desconto: number = 0.05): number {`

> Stub para editar: `ex012_preco_desconto/solution_ex012_preco_desconto.py` (Python) e `solution.ts` (TS).
