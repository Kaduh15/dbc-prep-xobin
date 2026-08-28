# Ex 033 — Maior e menor de três

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia três números e mostre qual é o maior e qual é o menor.”

## Descrição
Dados três números inteiros, retorna o maior e o menor deles.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| a | int | Primeiro número. |
| b | int | Segundo número. |
| c | int | Terceiro número. |

## Formato do Retorno
Tupla `(maior, menor)` com o maior e o menor valor informado.

## Assinatura canônica
```python
def maior_e_menor(a: int, b: int, c: int) -> tuple[int, int]:
```
```ts
export function maiorEMenor(a: number, b: number, c: number): [number, number]
```

## Casos de Exemplo
```py
f(3, 7, 5)  ->  (7, 3)
```
```py
f(1, 2, 3)  ->  (3, 1)
```
```py
f(-1, -5, -2)  ->  (-1, -5)
```
```py
f(9, 9, 9)  ->  (9, 9)
```

## Casos de Teste (todos, incluindo extremos)
```py
    (3, 7, 5),  # -> (7, 3)
    (1, 2, 3),  # -> (3, 1)
    (9, 5, 1),  # -> (9, 1)
    (-1, -5, -2),  # -> (-1, -5)
    (9, 9, 9),  # -> (9, 9)
    (5, 5, 3),  # -> (5, 3)
    (3, 5, 5),  # -> (5, 3)
    (5, 3, 5),  # -> (5, 3)
    (1, 1, 1),  # -> (1, 1)
    (0, 0, 7),  # -> (7, 0)
    (7, 5, 7),  # -> (7, 5)
    (-3, -3, -1),  # -> (-1, -3)
```

## Edge Cases / Extremos
Empates: dois valores iguais ao maior/menor não alteram o resultado; todos iguais -> maior == menor. Negativos e zeros cobertos.

## Abordagem / Dica
Determinar maior e menor com `max`/`min` (Python) ou `Math.max`/`Math.min` (JS).

## Complexidade
- Tempo O(1), espaço O(1)
