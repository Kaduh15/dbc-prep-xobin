# Exercício 063 — Sequência de Fibonacci

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Escreva um programa que leia um número inteiro N e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

## Parâmetros e Tipos

- ``n`` (``int``): quantidade de termos da sequência a exibir (inteiro >= 0).

## Retorno

``list[int]`` — os N primeiros termos de Fibonacci, começando com 0 e 1: cada termo é a soma dos dois anteriores.

## Casos de Exemplo

```
    fibonacci(0)  -> []
    fibonacci(1)  -> [0]
    fibonacci(2)  -> [0, 1]
    fibonacci(5)  -> [0, 1, 1, 2, 3]
    fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Casos de Teste (todos, incluindo extremos)

```python
    (0,) -> [],
    (1,) -> [0],
    (2,) -> [0, 1],
    (5,) -> [0, 1, 1, 2, 3],
    (10,) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
    (6,) -> [0, 1, 1, 2, 3, 5],
    (7,) -> [0, 1, 1, 2, 3, 5, 8],
    (-3,) -> []
```

## Edge Cases / Extremos

- ``n == 0`` retorna ``[]``; ``n == 1`` retorna ``[0]`` (termina antes de completar ``[0, 1]``).
- ``n < 0``: entrada inválida -> lista vazia.
- Recurrency: ``fib(0)=0``, ``fib(1)=1``, ``fib(n)=fib(n-1)+fib(n-2)``.
- Um termo de meio (ex.: ``n=7`` -> ``[0,1,1,2,3,5,8]``) confere a enumeração a partir de 0.

## Abordagem / Dica

Itere mantendo os dois últimos termos em variáveis/pilha: a cada passo o novo termo é a soma dos dois anteriores. Para listas, comece de ``[0, 1]`` e estenda até alcançar ``n`` (fatiando caso a semente já ultrapasse ``n``).

## Complexidade

Tempo ``O(n)``; espaço ``O(n)`` (lista de saída).

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List


def fibonacci(n: int) -> List[int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function fibonacci(n: number): number[] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex063_fibonacci/solution_ex063_fibonacci.py` (Python) e `solution.ts` (TS).
