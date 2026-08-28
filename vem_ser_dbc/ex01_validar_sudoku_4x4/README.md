# Exercício 01 — Validar Sudoku 4x4 (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada uma grade 4x4 de inteiros, retorne True se for uma solução válida: cada linha, cada coluna e cada bloco 2x2 contêm exatamente os dígitos 1–4, sem repetição. Qualquer grade incompleta, com tamanho errado ou com valores fora de 1–4 é inválida.

## Parâmetros e Tipos Esperados
- Assinatura: `def validar_sudoku_4x4(grid: list) -> bool:`

## Formato do Retorno
- bool: True se solução 4x4 válida

## Casos de Exemplo
```python
    (([[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],), True),
    (([[1, 1, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 5], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (([[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],), True),
    (([[1, 1, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 5], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 0], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3], [3, 4, 1], [2, 1, 4]],), False),
    (([],), False),
```

## Edge Cases / Extremos
Grade válida resolvida; duplicado em linha; duplicado em bloco 2x2; valor fora de 1–4 (5 ou 0); tamanho errado (não 4x4); grade vazia.

## Abordagem / Dica
Valide linhas, colunas e os 4 blocos 2x2 comparando cada sequência com {1,2,3,4}. Cheque o tamanho (4x4) primeiro.

## Complexidade
- Tempo O(16), espaço O(1)

## Assinatura Canônica
- **Python**: `def validar_sudoku_4x4(grid: list) -> bool:`
- **TypeScript**: `export function validarSudoku4x4(grid: number[][]): boolean {`

> Stub para editar: `ex01_validar_sudoku_4x4/solution_ex01_validar_sudoku_4x4.py` (Python) e `solution.ts` (TS).

