# EX051 — Progressão aritmética (PA)

**Enunciado (Curso em Vídeo, DESAFIO 051):**
> Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

## Descrição
Dado o primeiro termo e a razão de uma PA, retorne os primeiros `n` termos da progressão. Cada termo é o anterior somado à razão: `a_i = primeiro_termo + razao * (i - 1)`.

## Parâmetros e Tipos
- `primeiro_termo` — `int`: primeiro termo da PA.
- `razao` — `int`: razão da PA.
- `n` — `int`, opcional: quantidade de termos. Padrão `10` (como no enunciado original).

## Retorno
- `list[int]`: lista com os `n` primeiros termos.

## Casos de Exemplo
```python
progressao_aritmetica(2, 3)          # [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
progressao_aritmetica(10, 10)        # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
progressao_aritmetica(1, 2, 5)       # [1, 3, 5, 7, 9]
progressao_aritmetica(5, 0, 10)      # [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
```

## Restrições / Edge Cases
- Razão zero → todos os termos iguais ao primeiro.
- Razão negativa → progressão decrescente.
- nº de termos `n <= 0` não ocorre no problema original (assuma `n >= 1`).

## Assinatura canônica
```python
def progressao_aritmetica(primeiro_termo: int, razao: int, n: int = 10) -> list[int]
```
```typescript
export function progressaoAritmetica(primeiroTermo: number, razao: number, n: number = 10): number[]
```
