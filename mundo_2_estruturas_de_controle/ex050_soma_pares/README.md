# EX050 — Soma dos valores pares

**Enunciado (Curso em Vídeo):**
> Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

## Descrição
Dada uma lista de números inteiros, some apenas os valores pares e retorne o total. Os valores ímpares são ignorados.

## Parâmetros e Tipos
- `numeros` — `list[int]`: lista de números inteiros a analisar.

## Retorno
`int`: soma dos valores pares presentes na lista. Se não houver pares, retorna `0`.

## Casos de Exemplo
```python
soma_pares([1, 2, 3, 4, 5, 6])  # 12
soma_pares([2, 4, 6])  # 12
soma_pares([1, 3, 5])  # 0
soma_pares([-2, 3, 4, -6])  # -4
soma_pares([])  # 0
```

## Edge Cases / Extremos
- **Lista vazia:** Soma 0.
- **Nenhum par:** Soma 0 (ex.: `[1, 3, 5, 7]`).
- **Pares negativos:** Entram na soma com sinal (ex.: `[-2, -4, -6] → -12`).
- **Zero:** `0` é par e contribui com 0 à soma.
- **Um único elemento:** `[8] → 8`; `[7] → 0`.

## Abordagem
Filtra os elementos pares (`x % 2 == 0`) e acumula a soma em uma única passada.

## Complexidade
Tempo O(n); Espaço O(1) (iterador; não materializa nova lista).

## Assinatura canônica
```python
def soma_pares(numeros: list[int]) -> int
```
```typescript
export function somaPares(numeros: number[]): number
```

## Stub TDD (para implementar)
Arquivos: `solution_ex050_soma_pares.py`, `solution.ts`. Testes: `test_ex050_soma_pares.py`, `solution.test.ts`.

```python
def soma_pares(numeros: list[int]) -> int:
    raise NotImplementedError
```
```typescript
export function somaPares(numeros: number[]): number {
  throw new Error("not implemented");
}
```
