# Ex 026 — Análise da letra A

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.”

## Descrição
Analisa uma frase e retorna quantas vezes a letra “A” (maiúscula ou minúscula) aparece, além do índice (0-based) da primeira e da última ocorrência.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| frase | str | Texto a ser analisado. |

## Formato do Retorno
Tupla `(total, primeira, ultima)`: total de ocorrências; índice da primeira ocorrência; índice da última ocorrência. Se não houver ocorrência, `primeira = -1` e `ultima = -1`.

## Casos de Exemplo
```py
analisar_letra_a("Arara Azul")  ->  (4, 0, 6)
```
```py
analisar_letra_a("Mariana")  ->  (3, 1, 6)
```
```py
analisar_letra_a("xyz")  ->  (0, -1, -1)
```
```py
analisar_letra_a("")  ->  (0, -1, -1)
```
## Restrições / Edge Cases
- Contagem case-insensitive (‘a’ e ‘A’ contam).
- Índices baseados em 0.
- Frase sem a letra “a” retorna `(0, -1, -1)`.

## Assinatura canônica
```python
def analisar_letra_a(frase: str) -> tuple[int, int, int]:
```
```ts
export function analisarLetraA(frase: string): [number, number, number]
```
