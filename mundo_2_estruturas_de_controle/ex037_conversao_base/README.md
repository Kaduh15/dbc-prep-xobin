# EX37 — Conversão de Bases

## Descrição
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. Converta o número para a base escolhida (resultado sem prefixo, em minúsculas).

## Parâmetros e Tipos
- `numero` (int) — número inteiro positivo (>= 0) a ser convertido.
- `base` (int) — 1 para binário, 2 para octal, 3 para hexadecimal.

## Retorno
`str` — representação do número na base escolhida, sem prefixo (`0b`/`0o`/`0x`), com dígitos hexadecimais em minúsculas.

## Casos de Exemplo
```python
converter_base(10, 1)  -> "1010"
converter_base(10, 2)  -> "12"
converter_base(10, 3)  -> "a"
converter_base(255, 1) -> "11111111"
converter_base(255, 2) -> "377"
converter_base(255, 3) -> "ff"
converter_base(0, 3)   -> "0"
```

## Restrições / Edge Cases
- A saída deve ser **sem prefixo** e **minúsculas**.
- Número 0 em qualquer base é `"0"`.
- `base` fora de {1, 2, 3} deve lançar `ValueError`.

## Assinatura canônica

```python
def converter_base(numero: int, base: int) -> str:
```

```typescript
converterBase(numero: number, base: number): string
```
