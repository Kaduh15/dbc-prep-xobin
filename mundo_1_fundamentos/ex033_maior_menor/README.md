# Ex 033 — Maior e menor de três

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia três números e mostre qual é o maior e qual é o menor.”

## Descrição
Dados três números inteiros, retorna o maior e o menor deles.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| a | int | Primeiro número. |
| b | int | Segundo número. |
| c | int | Terceiro número. |

## Formato do Retorno
Tupla `(maior, menor)` com o maior e o menor valor informado.

## Casos de Exemplo
```py
maior_e_menor(3, 7, 5)  ->  (7, 3)
```
```py
maior_e_menor(1, 2, 3)  ->  (3, 1)
```
```py
maior_e_menor(-1, -5, -2)  ->  (-1, -5)
```
```py
maior_e_menor(9, 9, 9)  ->  (9, 9)
```
## Restrições / Edge Cases
- Valores iguais: maior == menor quando todos forem iguais.
- Aceita números negativos.

## Assinatura canônica
```python
def maior_e_menor(a: int, b: int, c: int) -> tuple[int, int]:
```
```ts
export function maiorEMenor(a: number, b: number, c: number): [number, number]
```
