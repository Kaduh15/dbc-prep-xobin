# EX016 — Porção Inteira

## Descrição
Receba um número **real** qualquer e retorne apenas a sua **porção inteira** (parte inteira).

## Parâmetros e Tipos
- `numero` (`float`): número real a ser decomposto.

## Formato do Retorno
`int` — a parte inteira do número (truncada em direção a zero).

## Casos de Exemplo
```python
parte_inteira(6.127)  # 6
parte_inteira(100.5)  # 100
parte_inteira(-3.9)   # -3
```

## Restrições / Edge Cases
- Para números negativos, trunca em direção a zero (`int(-3.9) == -3`), não para menos infinito.
- Se o valor já é inteiro (ex.: `7.0`), o retorno é esse inteiro (`7`).

## Assinaturas canônicas
- **Python**: `parte_inteira(numero: float) -> int`
- **TypeScript**: `parteInteira(numero: number): number`