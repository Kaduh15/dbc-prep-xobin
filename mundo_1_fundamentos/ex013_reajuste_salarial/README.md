# EX013 — Reajuste Salarial

## Descrição
Um funcionário recebeu um aumento de **15%** sobre o salário atual. Calcule e retorne o novo salário.

## Parâmetros e Tipos
- `salario` (`float`): salário atual do funcionário, em reais (R$).

## Formato do Retorno
`float` — novo salário após o aumento de 15% (`salario * 1.15`).

## Casos de Exemplo
```python
calcula_aumento(1000)    # 1150.0
calcula_aumento(2600)    # 2990.0
calcula_aumento(1250)    # 1437.5
calcula_aumento(0)       # 0.0
calcula_aumento(-100)    # -115.0  (a fórmula é aplicada mesmo para salário negativo)
```

## Edge Cases / Extremos
- O valor é multiplicado exatamente por `1.15` (aumento de 15%); qualquer entrada produz `entrada * 1.15`.
- `salario = 0` ⟹ `0.0`; nunca quebra.
- Salário negativo é um caso válido segundo a fórmula (`-100` ⟹ `-115.0`); a função não valida o domínio, apenas aplica o reajuste.
- Valores fracionários (`1234.56`) seguem a mesma regra (arredondamento de ponto flutuante).
- Casos adicionados: `-100 → -115.0`, `1234.56 → 1419.744`, `1 → 1.15`, `10000 → 11500.0`.

## Abordagem / Dica
`return salario * 1.15`. Não há arredondamento manual nem validação de domínio: a fórmula linear é aplicada diretamente à entrada.

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `calcula_aumento(salario: float) -> float`
- **TypeScript**: `calculaAumento(salario: number): number`

Stub de partida (Python):
```python
def calcula_aumento(salario: float) -> float:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function calculaAumento(salario: number): number {
  throw new Error("Not implemented");
}
```
