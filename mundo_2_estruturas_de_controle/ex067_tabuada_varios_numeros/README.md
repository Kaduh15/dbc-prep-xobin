# Exercício 067 — Tabuada de vários números

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

## Parâmetros e Tipos

- ``n`` (``int``): número para o qual a tabuada deve ser exibida. Valor negativo sinaliza a interrupção do programa.

## Retorno

``list[int] | None`` — para ``n >= 0``, lista com os 11 valores de ``n * 0`` até ``n * 10``. Para ``n < 0``, retorna ``None`` (sinaliza parada).

## Casos de Exemplo

```
    tabuada(7)   -> [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
    tabuada(5)   -> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    tabuada(-3)  -> None
    tabuada(0)   -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Casos de Teste (todos, incluindo extremos)

```python
    (7,) -> [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70],
    (5,) -> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    (-3,) -> None,
    (0,) -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    (1,) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    (12,) -> [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120],
    (-1,) -> None
```

## Edge Cases / Extremos

- A tabuada cobre multiplicadores ``0..10`` (**11** elementos).
- ``n == 0`` -> ``[0]*11``.
- ``n < 0`` (qualquer negativo) -> ``None`` (sinal de encerramento).
- ``n == 1`` -> ``[0..10]``.

## Abordagem / Dica

Se ``n < 0`` devolva ``None``. Caso contrário gere ``n*i`` para ``i`` em ``0..10`` (ex.: list comprehension ou ``Array.from``).

## Complexidade

Tempo ``O(11)`` = ``O(1)`` (tamanho fixo); espaço ``O(11)`` = ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List, Optional


def tabuada(n: int) -> Optional[List[int]]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function tabuada(n: number): number[] | null {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex067_tabuada_varios_numeros/solution_ex067_tabuada_varios_numeros.py` (Python) e `solution.ts` (TS).
