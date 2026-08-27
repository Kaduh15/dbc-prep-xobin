# EX013 — Reajuste Salarial

## Descrição
Um funcionário recebeu um aumento de **15%** sobre o salário atual. Calcule e retorne o novo salário.

## Parâmetros e Tipos
- `salario` (`float`): salário atual do funcionário, em reais (R$).

## Formato do Retorno
`float` — novo salário após o aumento de 15% (`salario * 1.15`).

## Casos de Exemplo
```python
calcula_aumento(1000)   # 1150.0
calcula_aumento(2600)   # 2990.0
calcula_aumento(1250)   # 1437.5
```

## Restrições / Edge Cases
- O valor é multiplicado exatamente por `1.15` (aumento de 15%).
- Salários menores que zero não fazem sentido no contexto; o retorno segue a fórmula.
- Para `salario = 0`, o resultado é `0.0`.

## Assinaturas canônicas
- **Python**: `calcula_aumento(salario: float) -> float`
- **TypeScript**: `calculaAumento(salario: number): number`