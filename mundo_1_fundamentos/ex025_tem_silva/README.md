# Ex 025 — Tem SILVA

**Enunciado original (Curso em Vídeo / Guanabara):** “Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.”

## Descrição
Verifica se o nome informado contém o sobrenome “SILVA” em qualquer posição da string, ignorando diferenças entre maiúsculas e minúsculas.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| nome | str | Nome completo da pessoa a ser verificado. |

## Formato do Retorno
Booleano: `True` se o nome contém “silva” (case-insensitive); caso contrário, `False`.

## Assinatura canônica
```python
def tem_silva(nome: str) -> bool:
```
```ts
export function temSilva(nome: string): boolean
```

## Casos de Exemplo
```py
f('João Silva Pereira',)  ->  True
```
```py
f('MARIA DA SILVA',)  ->  True
```
```py
f('Ana Souza',)  ->  False
```
```py
f('Silvania',)  ->  True
```
```py
f('',)  ->  False
```

## Casos de Teste (todos, incluindo extremos)
```py
    ('João Silva Pereira',),  # -> True
    ('MARIA DA SILVA',),  # -> True
    ('Ana Souza',),  # -> False
    ('Silvania',),  # -> True
    ('',),  # -> False
    ('sILvA',),  # -> True
    ('João sILVANIA',),  # -> True
    ('Santo',),  # -> False
    ('Silva Santos',),  # -> True
    ('   da silva   ',),  # -> True
    ('José',),  # -> False
```

## Edge Cases / Extremos
Busca case-insensitive (“SILVA”, “silva”, “SiLvA” todos casam). “Silvania”/prefixo ou substring também casam. Strings vazias ou sem “silva” retornam `False`.

## Abordagem / Dica
Normalizar o nome com `lower()` e verificar presença da substring "silva" (operador `in` em Python / `includes` em JS).

## Complexidade
- Tempo O(n), espaço O(1)
