# EX050 — Soma dos valores pares

**Enunciado (Curso em Vídeo, DESAFIO 050):**
> Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

## Descrição
Dada uma lista de números inteiros, some apenas os valores pares e retorne o total. Os valores ímpares são ignorados.

## Parâmetros e Tipos
- `numeros` — `list[int]`: lista de números inteiros a analisar.

## Retorno
- `int`: soma dos valores pares presentes na lista. Se não houver pares, retorna `0`.

## Casos de Exemplo
```python
soma_pares([1, 2, 3, 4, 5, 6])   # 12
soma_pares([2, 4, 6])            # 12
soma_pares([1, 3, 5])            # 0
soma_pares([])                   # 0
```

## Restrições / Edge Cases
- Ímpares são desconsiderados.
- Lista vazia → soma `0`.
- Números negativos pares também entram na soma.

## Assinatura canônica
```python
def soma_pares(numeros: list[int]) -> int
```
```typescript
export function somaPares(numeros: number[]): number
```
