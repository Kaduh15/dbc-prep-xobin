# Ex 032 — Ano bissexto

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia um ano qualquer e mostre se ele é bissexto.”

## Descrição
Verifica se um ano é bissexto segundo o calendário gregoriano.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| ano | int | Ano a ser verificado (inteiro). |

## Formato do Retorno
Booleano: `True` se o ano for bissexto; `False` caso contrário.

## Assinatura canônica
```python
def eh_bissexto(ano: int) -> bool:
```
```ts
export function ehBissexto(ano: number): boolean
```

## Casos de Exemplo
```py
f(2024,)  ->  True
```
```py
f(2023,)  ->  False
```
```py
f(2000,)  ->  True
```
```py
f(1900,)  ->  False
```
```py
f(1600,)  ->  True
```
```py
f(4,)  ->  True
```

## Casos de Teste (todos, incluindo extremos)
```py
    (2024,),  # -> True
    (2023,),  # -> False
    (2000,),  # -> True
    (1900,),  # -> False
    (1600,),  # -> True
    (4,),  # -> True
    (1700,),  # -> False
    (2100,),  # -> False
    (0,),  # -> True
    (400,),  # -> True
    (1996,),  # -> True
    (1,),  # -> False
    (100,),  # -> False
    (700,),  # -> False
```

## Edge Cases / Extremos
Regra gregoriana: divisível por 4, exceto finais de século (÷100) que só são bissextos se ÷400. Marcos: 1600/2000 bissextos; 1700/1900/2100 não. Ano 0 (÷400) é bissexto.

## Abordagem / Dica
Precedência: `ano % 400 == 0` ou (`ano % 4 == 0` e `ano % 100 != 0`).

## Complexidade
- Tempo O(1), espaço O(1)
