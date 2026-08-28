# EX051 — Progressão aritmética (PA)

**Enunciado (Curso em Vídeo):**
> Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

## Descrição
Dado o primeiro termo e a razão de uma PA, retorne os primeiros `n` termos: `a_i = primeiro_termo + razao * (i - 1)`.

## Parâmetros e Tipos
- `primeiro_termo` — `int`: primeiro termo da PA.
- `razao` — `int`: razão da PA.
- `n` — `int`, opcional: quantidade de termos. Padrão `10`.

## Retorno
`list[int]`: lista com os `n` primeiros termos.

## Casos de Exemplo
```python
progressao_aritmetica(2, 3, 10)  # [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
progressao_aritmetica(10, 10, 10)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
progressao_aritmetica(1, 2, 5)  # [1, 3, 5, 7, 9]
progressao_aritmetica(7, -2, 3)  # [7, 5, 3]
progressao_aritmetica(5, 0, 10)  # [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
```

## Edge Cases / Extremos
- **Razão zero:** Todos os termos iguais ao primeiro (PA constante).
- **Razão negativa:** Progressão decrescente.
- **Primeiro termo zero:** `(0, 5, 3) → [0, 5, 10]`.
- **Primeiro termo negativo:** Série cresce a partir de valor negativo.
- **n = 1:** Lista com um único termo `[primeiro_termo]`.

## Abordagem
Gera cada termo pela fórmula fechada `primeiro + razao * i` para `i` de `0` a `n-1`.

## Complexidade
Tempo O(n); Espaço O(n) para a lista de saída.

## Assinatura canônica
```python
def progressao_aritmetica(primeiro_termo: int, razao: int, n: int = 10) -> list[int]
```
```typescript
export function progressaoAritmetica(primeiroTermo: number, razao: number, n: number = 10): number[]
```

## Stub TDD (para implementar)
Arquivos: `solution_ex051_progressao_aritmetica.py`, `solution.ts`. Testes: `test_ex051_progressao_aritmetica.py`, `solution.test.ts`.

```python
def progressao_aritmetica(primeiro_termo: int, razao: int, n: int = 10) -> list[int]:
    raise NotImplementedError
```
```typescript
export function progressaoAritmetica(primeiroTermo: number, razao: number, n: number = 10): number[] {
  throw new Error("not implemented");
}
```
