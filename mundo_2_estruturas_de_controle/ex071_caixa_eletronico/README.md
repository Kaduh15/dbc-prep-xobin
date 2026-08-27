# Exercício 071 — Caixa eletrônico

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

## Parâmetros e Tipos

- ``valor`` (``int``): valor a ser sacado (inteiro, deve ser >= 0).

## Retorno

``dict[int, int]`` — mapa de cédula -> quantidade, nas denominações ``[100, 50, 20, 10, 5, 2, 1]``, sempre com todas as chaves presentes (quantidade pode ser 0).

## Casos de Exemplo

```
    caixa_eletronico(188) -> {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1}
    caixa_eletronico(650) -> {100: 6, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    caixa_eletronico(30)  -> {100: 0, 50: 0, 20: 1, 10: 1, 5: 0, 2: 0, 1: 0}
    caixa_eletronico(0)   -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
```

## Restrições / Casos de Borda

- Algoritmo guloso: prioriza as cédulas de maior valor.
- Como existe a cédula de 1, qualquer valor inteiro não negativo é totalmente decomposto.
- O dicionário retornado sempre contém as 7 denominações, mesmo com quantidade 0.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import Dict


def caixa_eletronico(valor: int) -> Dict[int, int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function caixaEletronico(valor: number): Record<number, number> {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.
