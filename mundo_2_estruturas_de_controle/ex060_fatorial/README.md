# EX060 — Fatorial

**Enunciado (Curso em Vídeo):**
> Faça um programa que leia um número qualquer e mostre o seu fatorial.

## Descrição
Calcule o fatorial de um inteiro não-negativo `n`: o produto de todos os inteiros de 1 até `n`. Por convenção, `0! = 1`.

## Parâmetros e Tipos
- `n` — `int`: número inteiro não-negativo.

## Retorno
`int`: valor de `n!`.

## Casos de Exemplo
```python
fatorial(5)  # 120
fatorial(0)  # 1
fatorial(1)  # 1
fatorial(6)  # 720
fatorial(10)  # 3628800
```

## Edge Cases / Extremos
- **0!:** `1` (caso base).
- **1!:** `1`.
- **Pequenos:** `2! = 2`, `3! = 6`, `4! = 24`.
- **Crescer rápido:** `10! = 3628800`, `12! = 479001600` (estoura tipos pequenos; use int/number).
- **Negativos:** Fora do escopo (função definida apenas para `n >= 0`).

## Abordagem
Multiplica iterativamente `resultado` por `2..n`; para `n < 2` retorna `1`.

## Complexidade
Tempo O(n); Espaço O(1).

## Assinatura canônica
```python
def fatorial(n: int) -> int
```
```typescript
export function fatorial(n: number): number
```

## Stub TDD (para implementar)
Arquivos: `solution_ex060_fatorial.py`, `solution.ts`. Testes: `test_ex060_fatorial.py`, `solution.test.ts`.

```python
def fatorial(n: int) -> int:
    raise NotImplementedError
```
```typescript
export function fatorial(n: number): number {
  throw new Error("not implemented");
}
```
