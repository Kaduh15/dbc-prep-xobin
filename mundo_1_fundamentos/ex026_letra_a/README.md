# Ex 026 — Análise da letra A

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia uma frase e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.”

## Descrição
Analisa a frase e retorna quantas vezes a letra “A” (maiúscula ou minúscula) aparece, além do índice (0-based) da primeira e da última ocorrência.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| frase | str | Texto a ser analisado. |

## Formato do Retorno
Tupla `(total, primeira, ultima)`: total de ocorrências; índice da primeira; índice da última. Sem ocorrência, `primeira = -1` e `ultima = -1`.

## Assinatura canônica
```python
def analisar_letra_a(frase: str) -> tuple[int, int, int]:
```
```ts
export function analisarLetraA(frase: string): [number, number, number]
```

## Casos de Exemplo
```py
f('Arara Azul',)  ->  (4, 0, 6)
```
```py
f('Mariana',)  ->  (3, 1, 6)
```
```py
f('xyz',)  ->  (0, -1, -1)
```
```py
f('',)  ->  (0, -1, -1)
```

## Casos de Teste (todos, incluindo extremos)
```py
    ('Arara Azul',),  # -> (4, 0, 6)
    ('Mariana',),  # -> (3, 1, 6)
    ('xyz',),  # -> (0, -1, -1)
    ('',),  # -> (0, -1, -1)
    ('AaA',),  # -> (3, 0, 2)
    ('aaaa',),  # -> (4, 0, 3)
    ('A',),  # -> (1, 0, 0)
    ('a',),  # -> (1, 0, 0)
    ('banana',),  # -> (3, 1, 5)
    ('XYZYX',),  # -> (0, -1, -1)
    ('casa amarela',),  # -> (5, 1, 11)
```

## Edge Cases / Extremos
Contagem case-insensitive (‘a’ e ‘A’ contam). Índices 0-based. Casos com caixa mista e espaços (ex.: “casa amarela” -> 5 ocorrências, 1ª posição 1, última 11). Frases sem ‘a’ retornam `(0, -1, -1)`.

## Abordagem / Dica
Normalizar com `lower()`; usar `find`/`rfind` (Python) ou `indexOf`/`lastIndexOf` (JS) para primeira/última ocorrência. Se `total == 0`, retornar `-1` nas posições.

## Complexidade
- Tempo O(n), espaço O(1)
