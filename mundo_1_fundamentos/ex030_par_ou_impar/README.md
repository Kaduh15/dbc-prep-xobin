# Ex 030 — Par ou Ímpar

**Enunciado original (Curso em Vídeo / Guanabara):** “Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.”

## Descrição
Determina se um número inteiro é par ou ímpar.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| numero | int | Número inteiro a ser classificado. |

## Formato do Retorno
String `"PAR"` se o número for par (divisível por 2); caso contrário `"ÍMPAR"`.

## Casos de Exemplo
```py
par_ou_impar(2)  ->  "PAR"
```
```py
par_ou_impar(3)  ->  "ÍMPAR"
```
```py
par_ou_impar(0)  ->  "PAR"
```
```py
par_ou_impar(-4)  ->  "PAR"
```
## Restrições / Edge Cases
- Zero é par.
- Números negativos seguem a mesma regra (resto de divisão por 2).

## Assinatura canônica
```python
def par_ou_impar(numero: int) -> str:
```
```ts
export function parOuImpar(numero: number): "PAR" | "ÍMPAR"
```
