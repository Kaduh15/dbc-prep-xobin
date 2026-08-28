# EX016 — Porção Inteira

## Descrição
Receba um número **real** qualquer e retorne apenas a sua **porção inteira** (parte inteira).

## Parâmetros e Tipos
- `numero` (`float`): número real a ser decomposto.

## Formato do Retorno
`int` — a parte inteira do número (truncada em direção a zero).

## Casos de Exemplo
```python
parte_inteira(6.127)   # 6
parte_inteira(100.5)   # 100
parte_inteira(-3.9)    # -3   (trunca em direção a zero)
parte_inteira(7.0)     # 7
parte_inteira(0.999)   # 0
parte_inteira(-0.5)    # 0  (truncamento, não arredondamento)
```

## Edge Cases / Extremos
- Para números negativos, trunca **em direção a zero**: `int(-3.9) == -3`, não para menos infinito.
- Se o valor já é inteiro (ex.: `7.0`), o retorno é esse inteiro (`7`).
- Frações menores que 1 (`0.999`, `-0.5`) truncam para `0`.
- Casos adicionados: `-0.5 → 0`, `0.0 → 0`, `-2.0 → -2`, `1.9 → 1`, `123.99 → 123`, `-123.99 → -123`.

## Abordagem / Dica
Em Python, `int(numero)` trunca em direção a zero (resultado exato para valores com magnitude < 2^53). No TypeScript use `Math.trunc(numero)`, que também trunca em direção a zero (diferente de `Math.floor`, que vai para menos infinito).

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `parte_inteira(numero: float) -> int`
- **TypeScript**: `parteInteira(numero: number): number`

Stub de partida (Python):
```python
def parte_inteira(numero: float) -> int:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function parteInteira(numero: number): number {
  throw new Error("Not implemented");
}
```
