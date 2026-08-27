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

## Restrições / Casos de Borda

- A tabuada cobre os multiplicadores de 0 a 10 (11 elementos).
- Número negativo retorna ``None`` (sinal de encerramento do loop).

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
