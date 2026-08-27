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

## Restrições / Casos de Borda

- O flag 999 não entra na contagem nem na soma.
- O primeiro 999 encerra a leitura; valores posteriores a ele não devem ser considerados.
- A função é determinística e ignora qualquer 999 da lista.

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
