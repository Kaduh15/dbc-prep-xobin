# Exercício 065 — Média, maior e menor valores

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores, o maior e o menor valor lido. (No programa original o usuário decide se quer continuar digitando.)

## Parâmetros e Tipos

- ``numeros`` (``list[int]``): lista de valores inteiros digitados (pelo menos um).

## Retorno

``tuple[float, int, int]`` — ``(media, maior, menor)``: média aritmética dos valores, o maior valor e o menor valor.

## Casos de Exemplo

```
    estatisticas([7, 5, 8, 3]) -> (5.75, 8, 3)
    estatisticas([10])         -> (10.0, 10, 10)
    estatisticas([2, 9, 4])    -> (5.0, 9, 2)
    estatisticas([5, 5, 5, 5]) -> (5.0, 5, 5)
```

## Casos de Teste (todos, incluindo extremos)

```python
    ([7, 5, 8, 3],) -> (5.75, 8, 3),
    ([10],) -> (10.0, 10, 10),
    ([2, 9, 4],) -> (5.0, 9, 2),
    ([5, 5, 5, 5],) -> (5.0, 5, 5),
    ([-5, 0, 5],) -> (0.0, 5, -5),
    ([7, 7, 7],) -> (7.0, 7, 7),
    ([3],) -> (3.0, 3, 3),
    ([],) -> (0.0, 0, 0)
```

## Edge Cases / Extremos

- Média é a soma dividida pela quantidade (ponto flutuante).
- Lista vazia -> ``(0.0, 0, 0)``.
- Lista com 1 elemento -> média = maior = menor.
- Valores negativos e todos iguais também são cobertos pelos extremos.

## Abordagem / Dica

Se vazio, devolva o caso neutro. Caso contrário, some todos e divida pela quantidade para a média e use um único passe (ou ``max``/``min``) para os extremos.

## Complexidade

Tempo ``O(n)``; espaço ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List, Tuple


def estatisticas(numeros: List[int]) -> Tuple[float, int, int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function estatisticas(numeros: number[]): [number, number, number] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex065_media_maior_menor/solution_ex065_media_maior_menor.py` (Python) e `solution.ts` (TS).
