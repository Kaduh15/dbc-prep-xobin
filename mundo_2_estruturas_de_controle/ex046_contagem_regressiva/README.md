# EX46 — Contagem regressiva

## Descrição
Mostre uma contagem regressiva para o estouro de fogos, de `inicio` até `0`. A pausa de 1 segundo fica fora da função testável — a função retorna apenas a sequência.

## Parâmetros e Tipos
- `inicio` (int, opcional) — número de partida, padrão `10`.

## Retorno
`list[int]` — sequência decrescente de `inicio` até `0`, inclusive.

## Casos de Exemplo
```python
contagem_regressiva()  -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
contagem_regressiva(3) -> [3, 2, 1, 0]
contagem_regressiva(0) -> [0]
```

## Casos de Teste (todos, incluindo extremos)
```python
((), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
((3,), [3, 2, 1, 0]),
((0,), [0]),
# extremos
((1,), [1, 0]), ((5,), [5, 4, 3, 2, 1, 0]), ((2,), [2, 1, 0]),
```

## Edge Cases / Extremos
- Sempre inclui o `0`.
- Parâmetro padrão `inicio=10` é usado quando nenhum argumento é passado.
- `inicio == 0` retorna `[0]`; `inicio == 1` retorna `[1, 0]`.

## Abordagem / Dica
`range(inicio, -1, -1)` em Python (ou laço `for` decrescente em TS) gerando a lista inclusiva até 0.

## Complexidade
- Tempo O(n), espaço O(n), com `n = inicio + 1`.

## Assinatura Canônica
- **Python**: `def contagem_regressiva(inicio: int = 10) -> list[int]:`
- **TypeScript**: `export function contagemRegressiva(inicio: number = 10): number[]`

> Stub para editar: `ex046_contagem_regressiva/solution_ex046_contagem_regressiva.py` (Python) e `solution.ts` (TS).
