# Exercício 07 — Maior e Menor

## Descrição do Problema
Dada uma lista de números, retorne a tupla/array (maior, menor). Para lista vazia, retorne None/null.

## Parâmetros e Tipos Esperados
- nums: list[int]

## Formato do Retorno
- tuple[int, int] (maior, menor) ou None

## Casos de Exemplo
```python
# (args) -> esperado
    (([3, 1, 4, 1, 5],), (5, 1)),
    (([],), None),
    (([7],), (7, 7)),
    (([-1, -5, -3],), (-1, -5)),
    (([0, 0],), (0, 0)),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([3, 1, 4, 1, 5],), (5, 1)),
    (([],), None),
    (([7],), (7, 7)),
    (([-1, -5, -3],), (-1, -5)),
    (([0, 0],), (0, 0)),
    (([100, 5, 200],), (200, 5)),
```

## Edge Cases / Extremos
Lista vazia (None/null); um único elemento (maior=menor); negativos; zeros repetidos; valores grandes/pequenos na mesma lista.

## Abordagem / Dica
Varrer uma vez mantendo max e min; trate o caso vazio antes.

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def maior_menor(nums: list) -> tuple | None:`
- **TypeScript**: `export function maiorMenor(nums: number[]): [number, number] | null {`

> Stub para editar: `ex07_maior_menor/solution_ex07_maior_menor.py` (Python) e `solution.ts` (TS).

