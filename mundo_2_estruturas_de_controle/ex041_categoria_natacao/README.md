# EX41 — Categoria de natação

## Descrição
A Confederação Nacional de Natação precisa de um programa que, dada a idade de um atleta, mostre sua categoria: **≤ 9** → `Mirim`; **≤ 14** → `Infantil`; **≤ 19** → `Junior`; **≤ 20** → `Senior`; **> 20** → `Master`.

## Parâmetros e Tipos
- `idade` (int) — idade do atleta em anos.

## Retorno
`str` — `Mirim`, `Infantil`, `Junior`, `Senior` ou `Master`.

## Casos de Exemplo
```python
categoria_natacao(9)  -> "Mirim"
categoria_natacao(14) -> "Infantil"
categoria_natacao(17) -> "Junior"
categoria_natacao(19) -> "Junior"
categoria_natacao(20) -> "Senior"
categoria_natacao(25) -> "Master"
```

## Casos de Teste (todos, incluindo extremos)
```python
((9,), 'Mirim'), ((14,), 'Infantil'),
((17,), 'Junior'), ((19,), 'Junior'), ((20,), 'Senior'), ((25,), 'Master'),
# extremos / borda
((0,), 'Mirim'), ((5,), 'Mirim'), ((8,), 'Mirim'),
((10,), 'Infantil'), ((15,), 'Junior'), ((21,), 'Master'), ((30,), 'Master'),
```

## Edge Cases / Extremos
- Limites superiores exatos: 9 → Mirim, 14 → Infantil, 19 → Junior, 20 → Senior.
- Acima de 20 (21, 30) → Master.
- Borda inferior (idade 0) → Mirim.

## Abordagem / Dica
Encadear comparações `<=` na ordem `<9` → `<14` → `<19` → `<20` → senão `Master`. Usar `<=` para incluir os limites superiores.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def categoria_natacao(idade: int) -> str:`
- **TypeScript**: `export function categoriaNatacao(idade: number): string`

> Stub para editar: `ex041_categoria_natacao/solution_ex041_categoria_natacao.py` (Python) e `solution.ts` (TS).
