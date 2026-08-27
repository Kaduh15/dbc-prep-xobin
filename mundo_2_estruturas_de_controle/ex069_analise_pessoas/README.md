# Exercício 069 — Análise de dados do grupo

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa pergunta se o usuário quer continuar. No final, mostre: (A) quantas pessoas têm mais de 18 anos; (B) quantos homens foram cadastrados; (C) quantas mulheres têm menos de 20 anos.

## Parâmetros e Tipos

- ``pessoas`` (``list[tuple[int, str]]``): lista de cadastros ``(idade, sexo)``, em que ``sexo`` é ``"M"`` (masculino) ou ``"F"`` (feminino).

## Retorno

``tuple[int, int, int]`` — ``(maiores_de_18, homens, mulheres_menores_de_20)``.

## Casos de Exemplo

```
    analise_pessoas([(22, "M"), (15, "F"), (30, "M"), (19, "F")]) -> (3, 2, 2)
    analise_pessoas([(18, "M"), (20, "F")])                       -> (1, 1, 0)
    analise_pessoas([(12, "F")])                                   -> (0, 0, 1)
    analise_pessoas([])                                              -> (0, 0, 0)
```

## Restrições / Casos de Borda

- "Maiores de 18 anos" significa idade estritamente maior que 18 (``idade > 18``).
- "Mulheres com menos de 20 anos": sexo ``"F"`` e ``idade < 20``.
- ``sexo`` é case-insensitive; valores diferentes de ``M``/``F`` são ignorados.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List, Tuple


def analise_pessoas(pessoas: List[Tuple[int, str]]) -> Tuple[int, int, int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function analisePessoas(pessoas: [number, string][]): [number, number, number] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.
