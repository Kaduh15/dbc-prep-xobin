# EX015 — Aluguel de Carro

## Descrição
Um carro alugado custa **R$ 60,00 por dia** e **R$ 0,15 por Km rodado**. Calcule o preço total a pagar dado o número de dias e os Km percorridos.

## Parâmetros e Tipos
- `dias` (`int`): quantidade de dias de aluguel.
- `km` (`float`): quilômetros percorridos.

## Formato do Retorno
`float` — valor total a pagar: `dias * 60 + km * 0.15`.

## Casos de Exemplo
```python
custo_aluguel(8, 720)   # 588.0
custo_aluguel(5, 100)   # 315.0
custo_aluguel(1, 0)     # 60.0
custo_aluguel(0, 0)     # 0.0
custo_aluguel(2, 50.5)  # 127.575
```

## Edge Cases / Extremos
- `km` pode ser fracionário (ex.: `50.5`, `0.1`); o produto `km * 0.15` preserva os decimais.
- Com `dias = 0` e `km = 0`, o custo é `0.0`.
- Valor mínimo `dias = 0, km = 1` ⟹ `0.15`; apenas o custo por km.
- Casos adicionados: `(0,1) → 0.15`, `(1,1) → 60.15`, `(3,0.1) → 180.015`, `(10,1000) → 810.0`.

## Abordagem / Dica
`return dias * 60 + km * 0.15`. Cuidado com `0.1` representado em ponto flutuante: use `pytest.approx`/`toBeCloseTo` para comparar.

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `custo_aluguel(dias: int, km: float) -> float`
- **TypeScript**: `custoAluguel(dias: number, km: number): number`

Stub de partida (Python):
```python
def custo_aluguel(dias: int, km: float) -> float:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function custoAluguel(dias: number, km: number): number {
  throw new Error("Not implemented");
}
```
