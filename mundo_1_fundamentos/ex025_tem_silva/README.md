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

## Casos de Exemplo
```py
tem_silva("João Silva Pereira")  ->  True
```
```py
tem_silva("MARIA DA SILVA")  ->  True
```
```py
tem_silva("Ana Souza")  ->  False
```
```py
tem_silva("Silvania")  ->  True
```
```py
tem_silva("")  ->  False
```
## Restrições / Edge Cases
- A busca ignora maiúsculas/minúsculas (ex.: “SILVA”, “silva”, “SiLvA”).
- “Silvania” contém “silva” como substring (verdadeiro).
- String vazia retorna `False`.

## Assinatura canônica
```python
def tem_silva(nome: str) -> bool:
```
```ts
export function temSilva(nome: string): boolean
```
