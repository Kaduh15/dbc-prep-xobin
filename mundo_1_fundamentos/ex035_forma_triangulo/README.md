# Ex 035 — Forma triângulo

**Enunciado original (Curso em Vídeo / Guanabara):** “Leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.”

## Descrição
Dados três comprimentos de segmentos de reta, determina se é possível formar um triângulo pela desigualdade triangular.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| a | float | Comprimento da primeira reta. |
| b | float | Comprimento da segunda reta. |
| c | float | Comprimento da terceira reta. |

## Formato do Retorno
Booleano: `True` se os três segmentos formam triângulo (`a < b + c` e `b < a + c` e `c < a + b`); senão `False`.

## Assinatura canônica
```python
def forma_triangulo(a: float, b: float, c: float) -> bool:
```
```ts
export function formaTriangulo(a: number, b: number, c: number): boolean
```

## Casos de Exemplo
```py
f(3, 4, 5)  ->  True
```
```py
f(1, 2, 3)  ->  False
```
```py
f(10, 1, 1)  ->  False
```
```py
f(5.5, 5.5, 5.5)  ->  True
```
```py
f(7, 2, 4)  ->  False
```

## Casos de Teste (todos, incluindo extremos)
```py
    (3, 4, 5),  # -> True
    (1, 2, 3),  # -> False
    (10, 1, 1),  # -> False
    (5.5, 5.5, 5.5),  # -> True
    (7, 2, 4),  # -> False
    (2, 3, 4),  # -> True
    (1, 1, 1),  # -> True
    (2, 2, 4),  # -> False
    (3, 3, 6),  # -> False
    (5, 5, 10),  # -> False
    (1, 1, 2),  # -> False
    (1, 1, 1.999),  # -> True
    (0.1, 0.1, 0.1),  # -> True
    (3, 3, 5.999),  # -> True
```

## Edge Cases / Extremos
Caso degenerado (soma de dois lados igual ao terceiro, ex.: 1,2,3) **não** forma triângulo (desigualdade estrita). Um lado >= soma dos outros dois -> `False`. Lados decimais e pontos-limite (1,1,1.999) formam triângulo; (1,1,2) não.

## Abordagem / Dica
Aplicar a desigualdade triangular nas três permutações e combinar com `and`.

## Complexidade
- Tempo O(1), espaço O(1)
