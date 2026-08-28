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
    analise_pessoas([])                                            -> (0, 0, 0)
```

## Casos de Teste (todos, incluindo extremos)

```python
    ([(22, 'M'), (15, 'F'), (30, 'M'), (19, 'F')],) -> (3, 2, 2),
    ([(18, 'M'), (20, 'F')],) -> (1, 1, 0),
    ([(12, 'F')],) -> (0, 0, 1),
    ([],) -> (0, 0, 0),
    ([(25, 'f')],) -> (1, 0, 0),
    ([(17, 'f')],) -> (0, 0, 1),
    ([(18, 'F')],) -> (0, 0, 1),
    ([(20, 'F')],) -> (1, 0, 0),
    ([(30, 'X')],) -> (1, 0, 0),
    ([(19, 'M'), (21, 'F')],) -> (2, 1, 0)
```

## Edge Cases / Extremos

- ``idade > 18`` (estritamente maior; 18 não conta).
- Mulheres com ``idade < 20`` (19 e 18 contam; 20 não).
- ``sexo`` é **case-insensitive** (``'f'``/``'m'``).
- Sexo diferente de ``M``/``F`` (ex.: ``'X'``) não conta como homem nem mulher, mas a idade segue valendo para ``maiores_de_18``.
- Lista vazia -> ``(0, 0, 0)``.

## Abordagem / Dica

Faça um único passe: para cada ``(idade, sexo)`` normalize o sexo com ``upper()`` e avalie as três condições independentes (maior de 18, sexo masculino, mulher com menos de 20).

## Complexidade

Tempo ``O(n)``; espaço ``O(1)``.

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

> Stub para editar: `ex069_analise_pessoas/solution_ex069_analise_pessoas.py` (Python) e `solution.ts` (TS).
