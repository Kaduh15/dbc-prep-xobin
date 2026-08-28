# Exercício 10 — Média Móvel (Janela Deslizante) (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma lista de números e um tamanho de janela, retorne a lista das médias de cada janela consecutiva de `janela` elementos, na ordem. Janela inválida (≤0 ou > tamanho) → lista vazia.

## Parâmetros e Tipos Esperados
- Assinatura: `def media_movel(valores: list, janela: int) -> list:`

## Formato do Retorno
- list[float]: médias das janelas

## Casos de Exemplo
```python
    (([1, 2, 3, 4], 2), [1.5, 2.5, 3.5]),
    (([5], 1), [5.0]),
    (([1, 2, 3], 3), [2.0]),
    (([1, 2, 3], 4), []),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([1, 2, 3, 4], 2), [1.5, 2.5, 3.5]),
    (([5], 1), [5.0]),
    (([1, 2, 3], 3), [2.0]),
    (([1, 2, 3], 4), []),
    (([], 2), []),
    (([1, 2, 3], 0), []),
    (([1, 2, 3, 4], 3), [2.0, 3.0]),
    (([-1, -2, -3, -4], 2), [-1.5, -2.5, -3.5]),
```

## Edge Cases / Extremos
Janela 1 (cada elemento); janela igual ao tamanho; janela > tamanho (→ []); janela ≤ 0 (→ []); lista vazia; valores negativos.

## Abordagem / Dica
Para i em 0..n−janela, some a janela `valores[i:i+janela]` e divida por `janela`. Sliding window.

## Complexidade
- Tempo O(n·janela), espaço O(n)

## Assinatura Canônica
- **Python**: `def media_movel(valores: list, janela: int) -> list:`
- **TypeScript**: `export function mediaMovel(valores: number[], janela: number): number[] {`

> Stub para editar: `ex10_media_movel/solution_ex10_media_movel.py` (Python) e `solution.ts` (TS).

