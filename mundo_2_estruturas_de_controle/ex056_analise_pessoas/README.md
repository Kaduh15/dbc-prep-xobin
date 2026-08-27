# EX056 — Análise de pessoas

**Enunciado (Curso em Vídeo, DESAFIO 056):**
> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

## Descrição
Dado o registro (nome, idade, sexo) de um grupo de pessoas, calcule e retorne: a **média** de idade do grupo, o **nome do homem mais velho** e a **quantidade de mulheres com menos de 20 anos**.

## Parâmetros e Tipos
- `pessoas` — `list[tupla]`: cada registro é `(nome: str, idade: int, sexo: str)`, com `sexo` igual a `'M'` ou `'F'`.

## Retorno
- `tuple`: `(media_idade, nome_homem_mais_velho, qtd_mulheres_menos_20)`.
  - `media_idade` — `float`: média aritmética das idades.
  - `nome_homem_mais_velho` — `str`: nome do homem de maior idade. **String vazia** se não houver homem no grupo.
  - `qtd_mulheres_menos_20` — `int`: contagem de mulheres com idade < 20.

## Casos de Exemplo
```python
pessoas = [("Ana", 30, "F"), ("Bruno", 35, "M"), ("Carla", 19, "F"), ("Diego", 40, "M")]
analisar_pessoas(pessoas)
# (31.0, "Diego", 1)   # média 124/4=31.0 ; homem mais velho Diego ; 1 mulher < 20

analisar_pessoas([("Alice", 25, "F"), ("Bob", 20, "M")])  # (22.5, "Bob", 0)
analisar_pessoas([("Ana", 30, "F"), ("Bia", 22, "F")])    # (26.0, "", 0)
```

## Restrições / Edge Cases
- Sem homens no grupo → nome do homem mais velho é `""`.
- Média retornada como `float` (soma das idades / quantidade).
- "Menos de 20 anos" é estritamente `< 20` (idade 20 não conta).
- No TypeScript, cada pessoa é um objeto `{ nome, idade, sexo }` (tipo `Pessoa`).

## Assinatura canônica
```python
def analisar_pessoas(pessoas: list[tuple[str, int, str]]) -> tuple[float, str, int]
```
```typescript
export type Pessoa = { nome: string; idade: number; sexo: string }
export function analisarPessoas(pessoas: Pessoa[]): [number, string, number]
```
