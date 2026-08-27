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
custo_aluguel(8, 720)  # 588.0
custo_aluguel(5, 100)  # 315.0
custo_aluguel(1, 0)    # 60.0
```

## Restrições / Edge Cases
- `km` pode ser fracionário (ex.: metros/vários decimais).
- Com `dias = 0` e `km = 0`, o custo é `0.0`.
- Aceita valores não negativos para `dias`.

## Assinaturas canônicas
- **Python**: `custo_aluguel(dias: int, km: float) -> float`
- **TypeScript**: `custoAluguel(dias: number, km: number): number`