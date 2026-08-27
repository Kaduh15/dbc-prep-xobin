# Ex 032 — Ano bissexto

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia um ano qualquer e mostre se ele é bissexto.”

## Descrição
Verifica se um ano é bissexto segundo o calendário gregoriano.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| ano | int | Ano a ser verificado (inteiro). |

## Formato do Retorno
Booleano: `True` se o ano for bissexto; caso contrário `False`.

## Casos de Exemplo
```py
eh_bissexto(2024)  ->  True
```
```py
eh_bissexto(2023)  ->  False
```
```py
eh_bissexto(2000)  ->  True
```
```py
eh_bissexto(1900)  ->  False
```
```py
eh_bissexto(1600)  ->  True
```
```py
eh_bissexto(4)  ->  True
```
## Restrições / Edge Cases
- Regra: divisível por 4, exceto finais de século (÷100) que só são bissextos se ÷400.
- 1900 não é bissexto; 2000 é bissexto.

## Assinatura canônica
```python
def eh_bissexto(ano: int) -> bool:
```
```ts
export function ehBissexto(ano: number): boolean
```
