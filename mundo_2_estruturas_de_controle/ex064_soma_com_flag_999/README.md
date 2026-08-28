# Exercício 064 — Soma com flag 999

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag.

## Parâmetros e Tipos

- ``numeros`` (``list[int]``): lista de números digitados; o valor 999 funciona como flag de parada.

## Retorno

``tuple[int, int]`` — ``(quantidade, soma)``: quantidade de números digitados (excluindo o flag 999) e soma desses números (ignorando o flag).

## Casos de Exemplo

```
    soma_ignorando_flag([2, 5, 999])    -> (2, 7)
    soma_ignorando_flag([1, 2, 3, 999]) -> (3, 6)
    soma_ignorando_flag([999])          -> (0, 0)
    soma_ignorando_flag([])             -> (0, 0)
```

## Casos de Teste (todos, incluindo extremos)

```python
    ([2, 5, 999],) -> (2, 7),
    ([1, 2, 3, 999],) -> (3, 6),
    ([999],) -> (0, 0),
    ([],) -> (0, 0),
    ([1, 999, 2],) -> (2, 3),
    ([999, 1, 999, 2, 999],) -> (2, 3),
    ([-5, 999, 10],) -> (2, 5),
    ([1, 2, 3],) -> (3, 6),
    ([999, 999],) -> (0, 0)
```

## Edge Cases / Extremos

- O valor ``999`` **NÃO** é contado nem somado (é apenas a condição de parada).
- Nesta versão, **qualquer** ocorrência de ``999`` é ignorada — mesmo no meio ou no fim da lista
  (ex.: ``[1, 999, 2] -> (2, 3)``).
- Lista vazia -> ``(0, 0)``; apenas flags -> ``(0, 0)``.
- Compare com o **ex066** (que para no *primeiro* 999).

## Abordagem / Dica

Percorra a lista uma vez; para cada elemento, se não for ``999``, incremente a contagem e acumule na soma. Ignore todos os ``999``.

## Complexidade

Tempo ``O(n)``; espaço ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List, Tuple


def soma_ignorando_flag(numeros: List[int]) -> Tuple[int, int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function somaIgnorandoFlag(numeros: number[]): [number, number] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex064_soma_com_flag_999/solution_ex064_soma_com_flag_999.py` (Python) e `solution.ts` (TS).
