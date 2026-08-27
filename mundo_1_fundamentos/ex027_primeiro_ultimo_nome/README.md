# Ex 027 — Primeiro e último nome

**Enunciado original (Curso em Vídeo / Guanabara):** “Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.”

## Descrição
Dado um nome completo, extrai separadamente o primeiro nome (primeira palavra) e o último nome (última palavra), ignorando espaços extras.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| nome_completo | str | Nome completo da pessoa, possivelmente com espaços extras. |

## Formato do Retorno
Tupla `(primeiro, ultimo)` com o primeiro e o último nome.
- Se houver apenas um nome, primeiro == ultimo.

## Casos de Exemplo
```py
primeiro_ultimo_nome("João Silva")  ->  ("João", "Silva")
```
```py
primeiro_ultimo_nome("Maria Clara Souza")  ->  ("Maria", "Souza")
```
```py
primeiro_ultimo_nome("Ana")  ->  ("Ana", "Ana")
```
```py
primeiro_ultimo_nome("  Pedro  Henrique  ")  ->  ("Pedro", "Henrique")
```
## Restrições / Edge Cases
- Espaços extras no início/fim/meio são removidos.
- Nome com palavra única: primeiro == último.

## Assinatura canônica
```python
def primeiro_ultimo_nome(nome_completo: str) -> tuple[str, str]:
```
```ts
export function primeiroUltimoNome(nomeCompleto: string): [string, string]
```
