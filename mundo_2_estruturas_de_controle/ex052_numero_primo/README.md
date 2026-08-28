# EX052 — Número primo

**Enunciado (Curso em Vídeo):**
> Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

## Descrição
Um número primo é divisível apenas por 1 e por ele mesmo. Dado um inteiro `n`, retorne `True` se ele for primo e `False` caso contrário.

## Parâmetros e Tipos
- `n` — `int`: número inteiro a verificar.

## Retorno
`bool`: `True` se `n` for primo, senão `False`.

## Casos de Exemplo
```python
eh_primo(7)  # True
eh_primo(2)  # True
eh_primo(97)  # True
eh_primo(1)  # False
eh_primo(4)  # False
eh_primo(100)  # False
eh_primo(0)  # False
```

## Edge Cases / Extremos
- **0 e 1:** Não são primos.
- **Negativos e < 2:** Não são primos.
- **2:** Pelo único primo par.
- **Compostos:** `91 = 7·13`, `9 = 3·3` → False.
- **Primos grandes:** `101` e `997` → True.

## Abordagem
Para `n < 2` retorna `False`. Exclui pares, depois testa divisores ímpares de `3` até `√n`.

## Complexidade
Tempo O(√n); Espaço O(1).

## Assinatura canônica
```python
def eh_primo(n: int) -> bool
```
```typescript
export function ehPrimo(n: number): boolean
```

## Stub TDD (para implementar)
Arquivos: `solution_ex052_numero_primo.py`, `solution.ts`. Testes: `test_ex052_numero_primo.py`, `solution.test.ts`.

```python
def eh_primo(n: int) -> bool:
    raise NotImplementedError
```
```typescript
export function ehPrimo(n: number): boolean {
  throw new Error("not implemented");
}
```
