# EX049 — Tabuada com laço for

**Enunciado (Curso em Vídeo):**
> Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço **for**.

## Descrição
Dado um número inteiro `n`, calcule e retorne os dez resultados da sua tabuada (de `n x 1` até `n x 10`).

## Parâmetros e Tipos
- `n` — `int`: número cuja tabuada será calculada.

## Retorno
`list[int]`: lista com os produtos `[n*1, n*2, ..., n*10]`.

## Casos de Exemplo
```python
tabuada(5)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
tabuada(7)  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
tabuada(-3)  # [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30]
tabuada(0)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Edge Cases / Extremos
- **Número negativo:** Multiplicadores de 1 a 10 aplicados também a negativos → lista com valores negativos.
- **n = 0:** Todos os produtos são 0.
- **n = 1:** Identidade: `[1, 2, ..., 10]`.
- **n = 12:** Acima da faixa clássica 1–10, qualquer inteiro funciona.

## Abordagem
Um laço de 1 até 10 multiplicando `n` pelo multiplicador corrente, acumulando cada resultado na lista.

## Complexidade
Tempo O(10) = O(1) (sempre dez iterações); Espaço O(10) para a lista de saída.

## Assinatura canônica
```python
def tabuada(n: int) -> list[int]
```
```typescript
export function tabuada(n: number): number[]
```

## Stub TDD (para implementar)
Arquivos: `solution_ex049_tabuada_for.py`, `solution.ts`. Testes: `test_ex049_tabuada_for.py`, `solution.test.ts`.

```python
def tabuada(n: int) -> list[int]:
    raise NotImplementedError
```
```typescript
export function tabuada(n: number): number[] {
  throw new Error("not implemented");
}
```
