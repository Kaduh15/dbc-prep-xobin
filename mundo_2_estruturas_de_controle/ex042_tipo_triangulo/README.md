# EX42 — Tipo de triângulo

## Descrição
Verifique se três retas formam um triângulo (cada lado deve ser **menor** que a soma dos outros dois) e classifique: `equilatero` (três lados iguais), `isosceles` (dois lados iguais) ou `escaleno` (todos diferentes). Se não formam triângulo, retorna `invalido`.

## Parâmetros e Tipos
- `a` (float) — primeira reta.
- `b` (float) — segunda reta.
- `c` (float) — terceira reta.

## Retorno
`str` — `"equilatero"`, `"isosceles"`, `"escaleno"` ou `"invalido"`.

## Casos de Exemplo
```python
tipo_triangulo(2, 2, 2) -> "equilatero"
tipo_triangulo(3, 3, 5) -> "isosceles"
tipo_triangulo(3, 4, 5) -> "escaleno"
tipo_triangulo(1, 1, 3) -> "invalido"
tipo_triangulo(10, 2, 3) -> "invalido"
```

## Casos de Teste (todos, incluindo extremos)
```python
# valida
((2, 2, 2), 'equilatero'), ((3, 3, 5), 'isosceles'), ((3, 4, 5), 'escaleno'),
((1, 1, 3), 'invalido'), ((10, 2, 3), 'invalido'),
# extremos / borda
((3, 3, 3), 'equilatero'), ((2, 2, 1), 'isosceles'),
((7, 4, 4), 'isosceles'), ((5, 4, 3), 'escaleno'),
((2, 3, 5), 'invalido'),   # degenerado: 2 + 3 == 5
((1, 2, 3), 'invalido'), ((1, 1, 2), 'invalido'),
```

## Edge Cases / Extremos
- Triângulos degenerados (`2+3 == 5`, `1+2 == 3`, `1+1 == 2`) são **inválidos** porque a condição é `lado < soma` (estrita).
- Equilátero também atende `a == b == c` antes do teste de dois iguais (evita classificar como isósceles).
- Catetos em ordem trocada (`5,4,3`) seguem escaleno.

## Abordagem / Dica
1. Validar `a < b + c and b < a + c and c < a + b`; caso contrário → `invalido`.
2. `a == b == c` → `equilatero`; `a == b or b == c or a == c` → `isosceles`; senão `escaleno`.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def tipo_triangulo(a: float, b: float, c: float) -> str:`
- **TypeScript**: `export function tipoTriangulo(a: number, b: number, c: number): string`

> Stub para editar: `ex042_tipo_triangulo/solution_ex042_tipo_triangulo.py` (Python) e `solution.ts` (TS).
