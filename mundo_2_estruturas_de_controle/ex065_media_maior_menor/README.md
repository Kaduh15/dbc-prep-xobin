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

## Restrições / Casos de Borda

- A média é a soma dividida pela quantidade de elementos (ponto flutuante).
- Com lista vazia, retorne ``(0.0, 0, 0)``.
- Maior e menor são os valores extremos da lista.

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
