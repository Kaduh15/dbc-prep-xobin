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

## Restrições / Casos de Borda

- Recurrence: ``fib(0) = 0``, ``fib(1) = 1`` e ``fib(n) = fib(n-1) + fib(n-2)``.
- ``n == 0`` retorna ``[]``; ``n == 1`` retorna ``[0]``.
- Para ``n < 0`` retorna lista vazia (entrada inválida).

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
