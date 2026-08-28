# Exercício 08 — Lucro Máximo de Ações (Vem Ser DBC / Xobin)

## Descrição do Problema
Dado um array de preços em dias consecutivos, retorne o maior lucro comprando em um dia e vendendo em um dia posterior. Se não houver lucro (sempre caindo/sem variação), retorne 0.

## Parâmetros e Tipos Esperados
- Assinatura: `def lucro_acoes(precos: list) -> int:`

## Formato do Retorno
- int: lucro máximo (0 se nenhum)

## Casos de Exemplo
```python
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
    (([],), 0),
    (([5],), 0),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
    (([],), 0),
    (([5],), 0),
    (([1, 2, 3, 4, 5],), 4),
    (([3, 3, 3],), 0),
    (([2, 10],), 8),
    (([10, 1],), 0),
```

## Edge Cases / Extremos
Array vazio/1 elemento (→ 0); preços sempre caindo (→ 0); preços iguais (→ 0); máxima alta após mínima; compra no primeiro dia.

## Abordagem / Dica
Mantenha o preço mínimo visto e o melhor lucro (preço atual − mínimo). Atualize em uma passada.

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def lucro_acoes(precos: list) -> int:`
- **TypeScript**: `export function lucroAcoes(precos: number[]): number {`

> Stub para editar: `ex08_lucro_acoes/solution_ex08_lucro_acoes.py` (Python) e `solution.ts` (TS).

