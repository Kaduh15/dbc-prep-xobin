# EX37 — Conversão de bases

## Descrição
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão: **1** para binário, **2** para octal e **3** para hexadecimal. Converte o número para a base escolhida (resultado **sem prefixo**, em **minúsculas**).

## Parâmetros e Tipos
- `numero` (int) — número inteiro não negativo a ser convertido.
- `base` (int) — 1 (binário), 2 (octal) ou 3 (hexadecimal).

## Retorno
`str` — representação do número na base escolhida, sem prefixo (`0b`/`0o`/`0x`) e com dígitos hexadecimais em minúsculas.

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

## Casos de Teste (todos, incluindo extremos)
```python
# valida
((10, 1), '1010'), ((10, 2), '12'), ((10, 3), 'a'),
((255, 1), '11111111'), ((255, 2), '377'), ((255, 3), 'ff'),
((0, 2), '0'),
# extremos
((0, 1), '0'), ((0, 3), '0'),
((16, 1), '10000'), ((16, 3), '10'),
((31, 1), '11111'), ((8, 2), '10'),
((1000, 3), '3e8'),
# invalidas -> ValueError
[(10, 0), (10, 4), (10, 9), (10, -1)]
```

## Edge Cases / Extremos
- Número `0` em qualquer base → `"0"`.
- Saída **sem prefixo** e **minúscula** (`ff` e não `0xFF` / `FF`).
- `base` fora de `{1, 2, 3}` → `ValueError`.
- Conversões de potências de 2 (16), de 8 (8) e valores altos (1000 → `3e8`) validam hexa minúsculo com letras.

## Abordagem / Dica
Mapear base → função nativa (`bin`/`oct`/`hex` em Python, `numero.toString(r)` em TS) e descartar o prefixo com `[2:]` (Python). Validar a base **antes** de converter e lançar erro para valores fora de {1, 2, 3}.

## Complexidade
- Tempo O(log n), espaço O(log n).

## Assinatura Canônica
- **Python**: `def converter_base(numero: int, base: int) -> str:`
- **TypeScript**: `export function converterBase(numero: number, base: number): string`

> Stub para editar: `ex037_conversao_base/solution_ex037_conversao_base.py` (Python) e `solution.ts` (TS).
