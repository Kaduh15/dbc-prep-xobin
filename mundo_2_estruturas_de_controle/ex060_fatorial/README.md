# EX060 — Fatorial

**Enunciado (Curso em Vídeo, DESAFIO 060):**
> Faça um programa que leia um número qualquer e mostre o seu fatorial.

## Descrição
Calcule o fatorial de um número inteiro não-negativo `n`: o produto de todos os inteiros de 1 até `n`. Por convenção, `0! = 1`.

## Parâmetros e Tipos
- `n` — `int`: número inteiro **não-negativo**.

## Retorno
- `int`: valor de `n!`.

## Casos de Exemplo
```python
fatorial(5)   # 120
fatorial(0)   # 1
fatorial(1)   # 1
fatorial(3)   # 6
fatorial(10)  # 3628800
```

## Restrições / Edge Cases
- `0! = 1` (caso base convencional).
- Funciona apenas para `n >= 0` (o enunciado original não trata negativos).

## Assinatura canônica
```python
def fatorial(n: int) -> int
```
```typescript
export function fatorial(n: number): number
```
