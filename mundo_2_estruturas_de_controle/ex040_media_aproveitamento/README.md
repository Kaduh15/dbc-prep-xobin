# EX40 — Média e aproveitamento

## Descrição
Crie um programa que leia duas notas de um aluno, calcule a média e mostre o aproveitamento: média **< 5** → `Reprovado`; **5 ≤ média < 7** → `Recuperacao`; **média ≥ 7** → `Aprovado`.

## Parâmetros e Tipos
- `n1` (float) — primeira nota (0 a 10).
- `n2` (float) — segunda nota (0 a 10).

## Retorno
`str` — `"Reprovado"`, `"Recuperacao"` ou `"Aprovado"` conforme a média.

## Casos de Exemplo
```python
media_aproveitamento(4, 4)  -> "Reprovado"
media_aproveitamento(4, 6)  -> "Recuperacao"
media_aproveitamento(5, 8)  -> "Recuperacao"
media_aproveitamento(7, 7)  -> "Aprovado"
media_aproveitamento(8, 10) -> "Aprovado"
```

## Casos de Teste (todos, incluindo extremos)
```python
((4, 4), 'Reprovado'), ((4, 6), 'Recuperacao'),
((5, 8), 'Recuperacao'), ((7, 7), 'Aprovado'), ((8, 10), 'Aprovado'),
# extremos / borda
((5, 5), 'Recuperacao'),   # media == 5 (limite inferior inclusivo)
((6, 7), 'Recuperacao'),   # media == 6.5
((8, 6), 'Aprovado'),      # media == 7 (limite inclusive)
((0, 0), 'Reprovado'),     # media == 0
((10, 10), 'Aprovado'),    # media == 10
((3, 6), 'Reprovado'),     # media == 4.5
```

## Edge Cases / Extremos
- Média exatamente **5** → `Recuperacao` (5 é inclusivo em `5 ≤ média < 7`).
- Média exatamente **7** → `Aprovado` (7 é inclusivo em `média ≥ 7`).
- Notas mínimas (0/0) e máximas (10/10).

## Abordagem / Dica
`media = (n1 + n2) / 2`; comparar com as faixas usando `<` para o limite superior e a ramificação `Reprovado` → `Recuperacao` → `Aprovado`.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def media_aproveitamento(n1: float, n2: float) -> str:`
- **TypeScript**: `export function mediaAproveitamento(n1: number, n2: number): string`

> Stub para editar: `ex040_media_aproveitamento/solution_ex040_media_aproveitamento.py` (Python) e `solution.ts` (TS).
