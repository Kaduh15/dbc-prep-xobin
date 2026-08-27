# EX41 — Categoria de Natação

## Descrição
A Confederação Nacional de Natação precisa de um programa que, dado a idade do atleta, mostre sua categoria, de acordo com a tabela: até 9 anos → Mirim; até 14 anos → Infantil; até 19 anos → Junior; até 20 anos → Senior; acima de 20 anos → Master.

## Parâmetros e Tipos
- `idade` (int) — idade do atleta em anos.

## Retorno
`str` — categoria conforme a tabela: `Mirim`, `Infantil`, `Junior`, `Senior` ou `Master`.

## Casos de Exemplo
```python
categoria_natacao(9)  -> "Mirim"
categoria_natacao(14) -> "Infantil"
categoria_natacao(17) -> "Junior"
categoria_natacao(19) -> "Junior"
categoria_natacao(20) -> "Senior"
categoria_natacao(25) -> "Master"
```

## Restrições / Edge Cases
- Faixas exatas: ≤9 `Mirim`; ≤14 `Infantil`; ≤19 `Junior`; ≤20 `Senior`; >20 `Master`.

## Assinatura canônica

```python
def categoria_natacao(idade: int) -> str:
```

```typescript
categoriaNatacao(idade: number): string
```
