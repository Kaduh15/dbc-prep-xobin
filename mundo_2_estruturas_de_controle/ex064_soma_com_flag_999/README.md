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

## Restrições / Casos de Borda

- O valor 999 NÃO é contado nem somado (é apenas a condição de parada).
- Qualquer ocorrência de 999 deve ser ignorada na contagem e na soma.

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
