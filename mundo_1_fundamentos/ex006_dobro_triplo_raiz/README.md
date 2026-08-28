# Exercício 006 — Dobro, Triplo e Raiz Quadrada

## Descrição do Problema
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

## Parâmetros e Tipos Esperados
- `n: float` — número de entrada (deve ser >= 0 para raiz quadrada real).

## Formato do Retorno
- `tuple[float, float, float]` na ordem `(dobro, triplo, raiz)`:
  - `dobro = n * 2`
  - `triplo = n * 3`
  - `raiz = n ** 0.5`

## Casos de Exemplo
```
Input: 9   Output: (18.0, 27.0, 3.0)
Input: 4   Output: (8.0, 12.0, 2.0)
Input: 0   Output: (0.0, 0.0, 0.0)
```

## Casos de Teste (todos, incluindo extremos)
```
((9,), (18.0, 27.0, 3.0))
((4,), (8.0, 12.0, 2.0))
((0,), (0.0, 0.0, 0.0))
((2,), (4.0, 6.0, 1.4142135623730951))
((7,), (14.0, 21.0, 2.6457513110645907))
((16,), (32.0, 48.0, 4.0))
((1,), (2.0, 3.0, 1.0))
((0.5,), (1.0, 1.5, 0.7071067811865476))```

## Edge Cases / Extremos
Quadrados perfeitos (0, 1, 4, 9, 16) dão raiz inteira exata. Raízes não exatas (`2`, `7`, `0.5`) têm dígitos irracionais — comparar com tolerância (`pytest.approx` / igualdade de doubles em TS). Zero é a borda mínima (raiz = 0). Para `n < 0` a raiz não é real (fora do domínio da spec).

## Abordagem / Dica
Calcule `n * 2`, `n * 3` e `n ** 0.5` diretamente e retorne na ordem `(dobro, triplo, raiz)`. Para raízes não exatas não arredonde prematuramente; compare com aproximação.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def dobro_triplo_raiz(n: float) -> tuple[float, float, float]:`
- **TypeScript**: `export function dobroTriploRaiz(n: number): [number, number, number] {`

> Stub para editar: `ex006_dobro_triplo_raiz/solution_ex006_dobro_triplo_raiz.py` (Python) e `solution.ts` (TS).
