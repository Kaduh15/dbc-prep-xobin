# Exercício 061 — Progressão aritmética (10 termos) com while

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Refaça o DESAFIO 051 lendo o primeiro termo e a razão de uma Progressão Aritmética (PA) e exibindo os dez primeiros termos da progressão, agora usando a estrutura de repetição while.

## Parâmetros e Tipos

- ``primeiro`` (``int``): primeiro termo da PA.
- ``razao`` (``int``): razão (passo) entre os termos.

## Retorno

``list[int]`` — lista com os 10 primeiros termos da PA.

## Casos de Exemplo

```
    dez_termos_pa(2, 3)   -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
    dez_termos_pa(1, 1)   -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dez_termos_pa(10, -2) -> [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
```

## Restrições / Casos de Borda

- A lista deve ter exatamente 10 elementos.
- A razão pode ser negativa (progressão decrescente).
- Termo geral: ``termo_n = primeiro + (n - 1) * razao`` para n de 1 a 10.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List


def dez_termos_pa(primeiro: int, razao: int) -> List[int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function dezTermosPa(primeiro: number, razao: number): number[] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.
