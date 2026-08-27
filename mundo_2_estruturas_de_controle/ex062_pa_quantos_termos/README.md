# Exercício 062 — Progressão aritmética melhorada (mais termos)

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Melhore o desafio 061: após exibir os 10 primeiros termos da PA, pergunte ao usuário se ele quer mostrar mais alguns termos. Cada valor digitado indica quantos termos adicionais devem ser exibidos. O programa encerra quando o usuário responder 0.

## Parâmetros e Tipos

- ``primeiro`` (``int``): primeiro termo da PA.
- ``razao`` (``int``): razão da PA.
- ``pedidos_extras`` (``list[int]``): quantidade de termos extras pedida em cada rodada; a leitura termina quando um valor é 0.

## Retorno

``list[int]`` — a sequência completa: os 10 primeiros termos seguidos dos termos extras solicitados antes do flag de parada (0).

## Casos de Exemplo

```
    pa_continua(2, 3, [5])    -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]
    pa_continua(2, 3, [])     -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
    pa_continua(2, 3, [3, 0]) -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]
    pa_continua(2, 3, [0, 5]) -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
    pa_continua(1, 5, [2])    -> [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]
```

## Restrições / Casos de Borda

- Sempre começam sendo exibidos os 10 primeiros termos.
- O valor 0 na lista de pedidos é a condição de parada: encerra a leitura e adiciona 0 termos (pedidos posteriores são ignorados).
- Pedidos com valor negativo são tratados como 0 termo extra.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List


def pa_continua(primeiro: int, razao: int, pedidos_extras: List[int]) -> List[int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function paContinua(primeiro: number, razao: number, pedidosExtras: number[]): number[] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.
