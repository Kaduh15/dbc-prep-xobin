# EX018 — Seno, Cosseno e Tangente

## Descrição
Receba um ângulo em **graus** e retorne os valores de **seno**, **cosseno** e **tangente** desse ângulo.

## Parâmetros e Tipos
- `angulo` (`float`): ângulo em graus.

## Formato do Retorno
Tupla `(seno, cosseno, tangente)` de `float` (`tuple[float, float, float]`), nessa ordem.

## Casos de Exemplo
```python
trigonometria(0)   # (0.0, 1.0, 0.0)
trigonometria(30)  # (0.5, 0.866025..., 0.577350...)
trigonometria(45)  # (0.707106..., 0.707106..., 1.0)
trigonometria(60)  # (0.866025..., 0.5, 1.732050...)
trigonometria(180) # (~0.0, -1.0, ~0.0)
```

## Edge Cases / Extremos
- O ângulo é fornecido em graus e convertido para radianos internamente (`math.radians` / `Math.PI/180`).
- Em `90°` (e `270°`) a tangente tende a infinito; esses pontos de borda ficam de fora do caso base.
- `180°` ⟹ `(≈0.0, -1.0, ≈0.0)`; o seno/tangente são valores de ponto flutuante muito pequenos, compare com tolerância.
- Casos adicionados: `180 → (≈0, -1, ≈0)`, `22.5 → (0.382683..., 0.923879..., 0.414213...)`.

## Abordagem / Dica
Converta para radianos e chame `math.sin/cos/tan` (Python) ou `Math.sin/cos/tan` (TypeScript). Retorne sempre a tupla `(seno, cosseno, tangente)`. Testes usam tolerância devido ao ponto flutuante.

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `trigonometria(angulo: float) -> tuple[float, float, float]`
- **TypeScript**: `trigonometria(angulo: number): [number, number, number]`

Stub de partida (Python):
```python
def trigonometria(angulo: float) -> tuple[float, float, float]:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function trigonometria(angulo: number): [number, number, number] {
  throw new Error("Not implemented");
}
```
