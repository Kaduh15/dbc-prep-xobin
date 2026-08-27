# Exercício 070 — Análise de produtos

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que leia o nome e o preço de vários produtos. O programa pergunta se o usuário vai continuar cadastrando. No final, mostre: (A) o total gasto; (B) quantos produtos custam menos de R$100,00; (C) o nome do produto mais barato.

## Parâmetros e Tipos

- ``produtos`` (``list[tuple[str, float]]``): lista de cadastros ``(nome, preco)``.

## Retorno

``tuple[float, int, str]`` — ``(total_gasto, produtos_menores_100, nome_mais_barato)``.

## Casos de Exemplo

```
    analise_produtos([("Borracha", 2), ("Caderno", 15), ("Mouse", 120)]) -> (137.0, 2, "Borracha")
    analise_produtos([("X", 100.0)])                                      -> (100.0, 0, "X")
    analise_produtos([("A", 5), ("B", 3)])                               -> (8.0, 2, "B")
    analise_produtos([])                                                   -> (0.0, 0, "")
```

## Restrições / Casos de Borda

- "Menos de R$100" significa preço estritamente menor que ``100``.
- O mais barato é o produto de menor preço; em caso de empate, vale o primeiro encontrado.
- Com lista vazia, retorne ``(0.0, 0, "")``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List, Tuple


def analise_produtos(produtos: List[Tuple[str, float]]) -> Tuple[float, int, str]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function analiseProdutos(produtos: [string, number][]): [number, number, string] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.
