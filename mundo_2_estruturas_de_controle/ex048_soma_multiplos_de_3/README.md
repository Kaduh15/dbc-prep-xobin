# EX48 — Soma dos múltiplos de 3

## Descrição
Calcule a soma entre todos os números múltiplos de 3 no intervalo de `inicio` até `fim` (inclusive).

## Parâmetros e Tipos
- `inicio` (int, opcional) — limite inferior, padrão `1`.
- `fim` (int, opcional) — limite superior, padrão `500`.

## Retorno
`int` — soma de todos os múltiplos de 3 em `[inicio, fim]`.

## Casos de Exemplo
```python
soma_multiplos_de_3()      -> 41583
soma_multiplos_de_3(1, 10) -> 18
soma_multiplos_de_3(5, 12) -> 27
soma_multiplos_de_3(1, 6)  -> 9
```

## Casos de Teste (todos, incluindo extremos)
```python
((), 41583),
((1, 10), 18), ((5, 12), 27), ((1, 6), 9), ((3, 3), 3),
# extremos
((0, 10), 18),   # 0, 3, 6, 9
((10, 15), 27),  # 12, 15
((1, 3), 3),
((100, 100), 0), # 100 nao e multiplo de 3
```

## Edge Cases / Extremos
- Soma padrão `()` = 3+6+9+...+498 = **41583**.
- `0` é múltiplo de 3 e entra quando `inicio <= 0` (`(0, 10)` → 0+3+6+9 = 18).
- Ponto único que é múltiplo → o próprio número (`(3, 3)` → 3).
- Ponto único que não é múltiplo → 0 (`(100, 100)`).

## Abordagem / Dica
Iterar em `range(inicio, fim + 1)` somando quando `n % 3 == 0`. Alternativa O(1) via progressão aritmética da razão 3.

## Complexidade
- Tempo O(n) (ou O(1) com PA), espaço O(1), com `n = fim - inicio + 1`.

## Assinatura Canônica
- **Python**: `def soma_multiplos_de_3(inicio: int = 1, fim: int = 500) -> int:`
- **TypeScript**: `export function somaMultiplosDe3(inicio: number = 1, fim: number = 500): number`

> Stub para editar: `ex048_soma_multiplos_de_3/solution_ex048_soma_multiplos_de_3.py` (Python) e `solution.ts` (TS).
