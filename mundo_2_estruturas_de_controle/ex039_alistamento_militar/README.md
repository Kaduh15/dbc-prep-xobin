# EX39 — Alistamento Militar

## Descrição
Faça um programa que, de acordo com a idade, informe se o jovem ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento (idade padrão: 18 anos).

## Parâmetros e Tipos
- `idade` (int) — idade do jovem em anos.

## Retorno
`str` — `"faltam X anos"` se `idade < 18` (X = 18 - idade), `"hora de se alistar"` se `idade == 18`, `"ja passou X anos"` se `idade > 18` (X = idade - 18).

## Casos de Exemplo
```python
situacao_alistamento(16) -> "faltam 2 anos"
situacao_alistamento(17) -> "faltam 1 ano"
situacao_alistamento(18) -> "hora de se alistar"
situacao_alistamento(21) -> "ja passou 3 anos"
situacao_alistamento(30) -> "ja passou 12 anos"
```

## Restrições / Edge Cases
- Idade padrão de alistamento: **18 anos**.
- Para `idade < 18`, X = `18 - idade`; para `idade > 18`, X = `idade - 18`.

## Assinatura canônica

```python
def situacao_alistamento(idade: int) -> str:
```

```typescript
situacaoAlistamento(idade: number): string
```
