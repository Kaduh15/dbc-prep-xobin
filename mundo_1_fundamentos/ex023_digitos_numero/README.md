# EX023 — Dígitos de um Número

## Descrição
Receba um número inteiro entre **0 e 9999** e decomponha-o, retornando separadamente os dígitos de **unidade**, **dezena**, **centena** e **milhar**.

## Parâmetros e Tipos
- `numero` (`int`): número entre 0 e 9999.

## Formato do Retorno
Tupla `(unidade, dezena, centena, milhar)` — `tuple[int, int, int, int]`.

## Casos de Exemplo
```python
decompor_numero(1834)  # (4, 3, 8, 1)
decompor_numero(5)     # (5, 0, 0, 0)
decompor_numero(2764)  # (4, 6, 7, 2)
decompor_numero(0)     # (0, 0, 0, 0)
```

## Restrições / Edge Cases
- Números com menos de 4 dígitos têm posições superiores preenchidas com `0`.
- A entrada é restrita ao intervalo 0–9999.

## Assinaturas canônicas
- **Python**: `decompor_numero(numero: int) -> tuple[int, int, int, int]`
- **TypeScript**: `decomporNumero(numero: number): [number, number, number, number]`