# EX017 — Hipotenusa

## Descrição
Dados o comprimento do **cateto oposto** e do **cateto adjacente** de um triângulo retângulo, calcule o comprimento da **hipotenusa**.

## Parâmetros e Tipos
- `cateto_oposto` (`float`): cateto oposto ao ângulo reto.
- `cateto_adjacente` (`float`): cateto adjacente.

## Formato do Retorno
`float` — hipotenusa: `sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)`.

## Casos de Exemplo
```python
hipotenusa(3, 4)    # 5.0
hipotenusa(6, 8)    # 10.0
hipotenusa(5, 12)   # 13.0
hipotenusa(1, 1)    # 1.4142135623730951
hipotenusa(0, 6)    # 6.0
hipotenusa(0, 0)    # 0.0  (caso limite)
```

## Edge Cases / Extremos
- Trincas pitagóricas conhecidas (3-4-5, 6-8-10, 5-12-13, 7-24-25, 20-21-29) retornam inteiros exatos.
- Cateto nulo: `hipotenusa(0, 6) = 6`; ambos nulos ⟹ `0.0` (degenerado).
- O resultado é sempre ≥ cada cateto.
- Casos adicionados: `(0,0) → 0.0`, `(7,24) → 25`, `(20,21) → 29`.

## Abordagem / Dica
Use `math.sqrt` (Python) / `Math.sqrt` (TypeScript) da soma dos quadrados: `sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)`. Compare com tolerância.

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `hipotenusa(cateto_oposto: float, cateto_adjacente: float) -> float`
- **TypeScript**: `hipotenusa(catetoOposto: number, catetoAdjacente: number): number`

Stub de partida (Python):
```python
def hipotenusa(cateto_oposto: float, cateto_adjacente: float) -> float:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function hipotenusa(catetoOposto: number, catetoAdjacente: number): number {
  throw new Error("Not implemented");
}
```
