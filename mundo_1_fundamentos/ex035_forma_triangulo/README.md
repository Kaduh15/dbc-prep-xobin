# Ex 035 — Forma triângulo

**Enunciado original (Curso em Vídeo / Guanabara):** “Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.”

## Descrição
Dados três comprimentos de segmentos de reta, determina se é possível formar um triângulo. Forma triângulo **se, e somente se**, cada lado for menor que a soma dos outros dois.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| a | float | Comprimento da primeira reta. |
| b | float | Comprimento da segunda reta. |
| c | float | Comprimento da terceira reta. |

## Formato do Retorno
Booleano: `True` se os três segmentos formam um triângulo; caso contrário `False`.
Condição: `a < b + c` **e** `b < a + c` **e** `c < a + b`.

## Casos de Exemplo
```py
forma_triangulo(3, 4, 5)  ->  True
forma_triangulo(1, 2, 3)  ->  False
forma_triangulo(10, 1, 1)  ->  False
forma_triangulo(5.5, 5.5, 5.5)  ->  True
forma_triangulo(7, 2, 4)  ->  False
```

## Restrições / Edge Cases
- Caso degenerado (soma de dois lados igual ao terceiro, ex.: 1,2,3) **não** forma triângulo.
- Aceita lados com decimais (float).

## Assinatura canônica
```python
def forma_triangulo(a: float, b: float, c: float) -> bool:
```
```ts
export function formaTriangulo(a: number, b: number, c: number): boolean
```