# Ex 028 — Adivinhação (0 a 5)

**Enunciado original (Curso em Vídeo / Guanabara):** “Escreva um programa que pense em um número inteiro entre 0 e 5 e peça para o usuário adivinhá-lo. O programa escreve se o usuário venceu ou perdeu.”

## Descrição
Versão determinística: dado o palpite do usuário e o número “pensado” (segredo), retorna se acertou. A geração do segredo fica fora da função.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| palpite | int | Palpite dado pelo usuário. |
| segredo | int | Número “pensado” pelo computador. |

## Formato do Retorno
Booleano: `True` se `palpite == segredo` (venceu); caso contrário `False`.

## Assinatura canônica
```python
def venceu_adivinhacao(palpite: int, segredo: int) -> bool:
```
```ts
export function venceuAdivinhacao(palpite: number, segredo: number): boolean
```

## Casos de Exemplo
```py
f(3, 3)  ->  True
```
```py
f(3, 5)  ->  False
```
```py
f(0, 0)  ->  True
```

## Casos de Teste (todos, incluindo extremos)
```py
    (3, 3),  # -> True
    (3, 5),  # -> False
    (0, 0),  # -> True
    (5, 0),  # -> False
    (5, 5),  # -> True
    (2, 3),  # -> False
    (0, 5),  # -> False
    (4, 4),  # -> True
    (1, 0),  # -> False
    (-1, -1),  # -> True
```

## Edge Cases / Extremos
Função pura: a aleatoriedade fica fora (segredo é argumento). Coincidência exata nos extremos do intervalo ([0,5]) e palpite == segredo em qualquer faixa retorna `True`.

## Abordagem / Dica
Comparação direta `palpite == segredo`.

## Complexidade
- Tempo O(1), espaço O(1)
