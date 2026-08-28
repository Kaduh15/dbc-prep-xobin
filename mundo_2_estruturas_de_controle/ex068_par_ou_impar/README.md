# Exercício 068 — Jogo Par ou Ímpar

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Faça um programa que jogue par ou ímpar com o computador. O jogador escolhe entre Par ou Ímpar e o computador joga ao mesmo tempo; se a soma das jogadas corresponder à aposta do jogador, ele vence a rodada. (No jogo completo o computador joga de forma aleatória — aqui a rodada é determinística e testável.)

## Parâmetros e Tipos

- ``jogador`` (``int``): número escolhido pelo jogador.
- ``computador`` (``int``): número escolhido pelo computador.
- ``escolha`` (``str``): aposta do jogador entre ``"par"`` e ``"impar"`` (case-insensitive).

## Retorno

``bool`` — ``True`` se o jogador venceu a rodada, ``False`` caso contrário.

## Casos de Exemplo

```
    par_ou_impar(4, 2, "par")   -> True
    par_ou_impar(5, 4, "impar") -> True
    par_ou_impar(4, 2, "impar") -> False
    par_ou_impar(3, 4, "par")   -> False
    par_ou_impar(7, 3, "par")   -> True
```

## Casos de Teste (todos, incluindo extremos)

```python
    (4, 2, 'par') -> True,
    (5, 4, 'impar') -> True,
    (4, 2, 'impar') -> False,
    (3, 4, 'par') -> False,
    (7, 3, 'par') -> True,
    (7, 3, 'PAR') -> True,
    (5, 5, 'impar') -> False,
    (0, 0, 'par') -> True,
    (1, 2, 'impar') -> True,
    (2, 4, 'impar') -> False,
    (3, 4, 'IMPAR') -> True
```

## Edge Cases / Extremos

- A soma é **par** quando ``soma % 2 == 0``.
- Jogador vence quando a paridade da soma bate com a aposta (par->par ou ímpar->ímpar).
- ``escolha`` é **case-insensitive** (``"PAR"``, ``"Impar"`` funcionam).
- Somas empatadas/zero também são determinísticas (``(0,0,'par') -> True``).

## Abordagem / Dica

Calcule ``soma = jogador + computador``; determine a paridade. Compare a paridade da soma com a escolha normalizada (<- letras minúsculas). Qualquer escolha não-``"par"`` é tratada como ímpar.

## Complexidade

Tempo ``O(1)``; espaço ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
def par_ou_impar(jogador: int, computador: int, escolha: str) -> bool:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function parOuImpar(jogador: number, computador: number, escolha: string): boolean {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex068_par_ou_impar/solution_ex068_par_ou_impar.py` (Python) e `solution.ts` (TS).
