# Ex 027 — Primeiro e último nome

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadamente.”

## Descrição
Dado um nome completo, extrai o primeiro nome (primeira palavra) e o último nome (última palavra), ignorando espaços extras.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| nome_completo | str | Nome completo, possivelmente com espaços extras. |

## Formato do Retorno
Tupla `(primeiro, ultimo)`. Se houver um único nome, primeiro == ultimo. Nome vazio/em branco retorna `("", "")`.

## Assinatura canônica
```python
def primeiro_ultimo_nome(nome_completo: str) -> tuple[str, str]:
```
```ts
export function primeiroUltimoNome(nomeCompleto: string): [string, string]
```

## Casos de Exemplo
```py
f('João Silva',)  ->  ('João', 'Silva')
```
```py
f('Maria Clara Souza',)  ->  ('Maria', 'Souza')
```
```py
f('Ana',)  ->  ('Ana', 'Ana')
```
```py
f('  Pedro  Henrique  ',)  ->  ('Pedro', 'Henrique')
```

## Casos de Teste (todos, incluindo extremos)
```py
    ('João Silva',),  # -> ('João', 'Silva')
    ('Maria Clara Souza',),  # -> ('Maria', 'Souza')
    ('Ana',),  # -> ('Ana', 'Ana')
    ('  Pedro  Henrique  ',),  # -> ('Pedro', 'Henrique')
    ('',),  # -> ('', '')
    ('   ',),  # -> ('', '')
    ('A B C D',),  # -> ('A', 'D')
    ('   Ana   ',),  # -> ('Ana', 'Ana')
```

## Edge Cases / Extremos
Espaços extras no início/fim/meio são removidos. Nome com palavra única: primeiro == último. Nome vazio ou só espaços: `("", "")`.

## Abordagem / Dica
Quebrar o nome em palavras com `split()` (Python) / `split(/\s+/)` (JS), retornando a primeira e a última palavra; sem palavras, retorna vazios.

## Complexidade
- Tempo O(n), espaço O(n)
