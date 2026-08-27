# EX052 — Número primo

**Enunciado (Curso em Vídeo, DESAFIO 052):**
> Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

## Descrição
Um número primo é divisível apenas por 1 e por ele mesmo. Dado um inteiro `n`, retorne `True` se ele for primo e `False` caso contrário.

## Parâmetros e Tipos
- `n` — `int`: número inteiro a verificar.

## Retorno
- `bool`: `True` se `n` for primo, senão `False`.

## Casos de Exemplo
```python
eh_primo(2)    # True
eh_primo(7)    # True
eh_primo(97)   # True
eh_primo(1)    # False
eh_primo(4)    # False
eh_primo(100)  # False
```

## Restrições / Edge Cases
- `0` e `1` não são primos.
- `2` é o único primo par.
- Funciona para inteiros positivos.

## Assinatura canônica
```python
def eh_primo(n: int) -> bool
```
```typescript
export function ehPrimo(n: number): boolean
```
