# EX39 — Alistamento militar

## Descrição
Faça um programa que, de acordo com a idade, informe se o jovem ainda vai se alistar ao serviço militar, se é a hora exata ou se já passou do tempo (idade padrão: **18 anos**).

## Parâmetros e Tipos
- `idade` (int) — idade do jovem em anos.

## Retorno
`str` — `"faltam X anos"` se `idade < 18` (X = 18 - idade), `"hora de se alistar"` se `idade == 18`, `"ja passou X anos"` se `idade > 18` (X = idade - 18). Para X == 1, usa-se o singular `"ano"`.

## Casos de Exemplo
```python
situacao_alistamento(16) -> "faltam 2 anos"
situacao_alistamento(17) -> "faltam 1 ano"
situacao_alistamento(18) -> "hora de se alistar"
situacao_alistamento(21) -> "ja passou 3 anos"
situacao_alistamento(30) -> "ja passou 12 anos"
```

## Casos de Teste (todos, incluindo extremos)
```python
((16,), 'faltam 2 anos'), ((17,), 'faltam 1 ano'),
((18,), 'hora de se alistar'), ((21,), 'ja passou 3 anos'), ((30,), 'ja passou 12 anos'),
# extremos
((0,), 'faltam 18 anos'), ((1,), 'faltam 17 anos'),
((19,), 'ja passou 1 ano'), ((25,), 'ja passou 7 anos'), ((100,), 'ja passou 82 anos'),
```

## Edge Cases / Extremos
- Idade exatamente 18 → `"hora de se alistar"`.
- Diferença de 1 ano usa o **singular** (`"1 ano"`, ex.: 17 → `"faltam 1 ano"`; 19 → `"ja passou 1 ano"`).
- Idade 0 (borda inferior) e idades altas (100) verificam o cálculo da diferença.

## Abordagem / Dica
Comparar com 18 em três ramos (`<`, `==`, `>`). Formatar com singular/plural conforme a diferença seja 1 ou não.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def situacao_alistamento(idade: int) -> str:`
- **TypeScript**: `export function situacaoAlistamento(idade: number): string`

> Stub para editar: `ex039_alistamento_militar/solution_ex039_alistamento_militar.py` (Python) e `solution.ts` (TS).
