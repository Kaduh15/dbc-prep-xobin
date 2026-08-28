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

## Assinatura canônica
```python
def par_ou_impar(numero: int) -> str:
```
```ts
export function parOuImpar(numero: number): "PAR" | "ÍMPAR"
```

## Casos de Exemplo
```py
f(2,)  ->  'PAR'
```
```py
f(3,)  ->  'ÍMPAR'
```
```py
f(0,)  ->  'PAR'
```
```py
f(-4,)  ->  'PAR'
```

## Casos de Teste (todos, incluindo extremos)
```py
    (2,),  # -> PAR
    (3,),  # -> ÍMPAR
    (0,),  # -> PAR
    (-4,),  # -> PAR
    (-7,),  # -> ÍMPAR
    (1,),  # -> ÍMPAR
    (-2,),  # -> PAR
    (-1,),  # -> ÍMPAR
    (4,),  # -> PAR
    (100,),  # -> PAR
    (101,),  # -> ÍMPAR
```

## Edge Cases / Extremos
Zero é par. Números negativos seguem a mesma regra (resto da divisão por 2). Valores grandes pares/ímpares (100/101) também.

## Abordagem / Dica
Resto de divisão por 2: `numero % 2 == 0` -> `"PAR"`; senão `"ÍMPAR"`.

## Complexidade
- Tempo O(1), espaço O(1)
