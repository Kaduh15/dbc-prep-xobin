# Exercício 066 — Soma até o flag 999

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag.

## Parâmetros e Tipos

- ``numeros`` (``list[int]``): lista de números digitados; 999 é o valor de parada.

## Retorno

``tuple[int, int]`` — ``(quantidade, soma)``: quantidade de números digitados (excluindo o 999) e soma deles (ignorando o flag).

## Casos de Exemplo

```
    numeros_ate_999([5, 999])        -> (1, 5)
    numeros_ate_999([7, 8, 999, 10]) -> (2, 15)
    numeros_ate_999([999])           -> (0, 0)
    numeros_ate_999([])              -> (0, 0)
```

## Casos de Teste (todos, incluindo extremos)

```python
    ([5, 999],) -> (1, 5),
    ([7, 8, 999, 10],) -> (2, 15),
    ([999],) -> (0, 0),
    ([],) -> (0, 0),
    ([1, 999],) -> (1, 1),
    ([1, 2, 999, 4, 999],) -> (2, 3),
    ([1, 2, 3],) -> (3, 6),
    ([999, 10],) -> (0, 0)
```

## Edge Cases / Extremos

- O primeiro ``999`` **encerra** a leitura; tudo depois dele é ignorado (``[1,2,999,4,999] -> (2,3)``).
- Se não houver ``999``, processa a lista inteira (``[1,2,3] -> (3,6)``).
- Flag no início -> ``(0, 0)``.
- Compare com o **ex064** (que ignora todos os 999 e não para).

## Abordagem / Dica

Percorra em ordem e **pare** no primeiro ``999``, acumulando contagem e soma dos elementos anteriores. Use ``break`` ao encontrar o flag.

## Complexidade

Tempo ``O(n)``; espaço ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List, Tuple


def numeros_ate_999(numeros: List[int]) -> Tuple[int, int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function numerosAte999(numeros: number[]): [number, number] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex066_soma_ate_flag_999/solution_ex066_soma_ate_flag_999.py` (Python) e `solution.ts` (TS).
