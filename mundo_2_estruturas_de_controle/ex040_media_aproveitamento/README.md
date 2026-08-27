# EX40 — Média e Aproveitamento

## Descrição
Crie um programa que leia duas notas de um aluno, calcule a média e mostre o aproveitamento, de acordo com a tabela: média menor que 5 → Reprovado; média entre 5 (inclusive) e 7 (exclusive) → Recuperação; média maior ou igual a 7 → Aprovado.

## Parâmetros e Tipos
- `n1` (float) — primeira nota (0 a 10).
- `n2` (float) — segunda nota (0 a 10).

## Retorno
`str` — `"Reprovado"`, `"Recuperacao"` ou `"Aprovado"` conforme a média.

## Casos de Exemplo
```python
media_aproveitamento(4, 4) -> "Reprovado"
media_aproveitamento(4, 6) -> "Recuperacao"
media_aproveitamento(5, 8) -> "Recuperacao"
media_aproveitamento(7, 7) -> "Aprovado"
media_aproveitamento(8, 10) -> "Aprovado"
```

## Restrições / Edge Cases
- Faixas: média < 5 → `Reprovado`; 5 ≤ média < 7 → `Recuperacao`; média ≥ 7 → `Aprovado`.
- Notas assumidas entre 0 e 10.

## Assinatura canônica

```python
def media_aproveitamento(n1: float, n2: float) -> str:
```

```typescript
mediaAproveitamento(n1: number, n2: number): string
```
