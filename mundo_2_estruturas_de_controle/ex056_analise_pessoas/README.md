# EX056 — Análise de pessoas

**Enunciado (Curso em Vídeo):**
> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre: a média de idade do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

## Descrição
Dado o registro `(nome, idade, sexo)` de um grupo de pessoas, calcule e retorne a **média** de idade, o **nome do homem mais velho** e a **quantidade de mulheres com menos de 20 anos**.

## Parâmetros e Tipos
- `pessoas` — `list[tuple[str, int, str]]`: cada registro é `(nome, idade, sexo)`, `sexo` ∈ `{'M','F'}`.

## Retorno
`tuple[float, str, int]`: `(media_idade, nome_homem_mais_velho, qtd_mulheres_menos_20)`. Sem homem, nome é `""`.

## Casos de Exemplo
```python
pessoas = [("Ana", 30, "F"), ("Bruno", 35, "M"), ("Carla", 19, "F"), ("Diego", 40, "M")]
analisar_pessoas(pessoas)  # (31.0, "Diego", 1)

analisar_pessoas([("Alice", 25, "F"), ("Bob", 20, "M")])  # (22.5, "Bob", 0)
analisar_pessoas([("Ana", 30, "F"), ("Bia", 22, "F")])    # (26.0, "", 0)
```

## Edge Cases / Extremos
- **Sem homens:** Nome do homem mais velho é `""`.
- **Média float:** soma das idades / quantidade (ex.: `23.5`).
- **"Menos de 20":** Estritamente `< 20`; idade exatamente `20` **não** conta.
- **Empate na idade:** Maior idade vence; empates não especificados.
- **Um homem/uma mulher:** Casos mínimos funcionam.

## Abordagem
Em uma passada: acumula a soma das idades (depois divide), registra o homem com maior idade e conta mulheres com idade `< 20`.

## Complexidade
Tempo O(n); Espaço O(1) além da entrada.

## Assinatura canônica
```python
def analisar_pessoas(pessoas: list[tuple[str, int, str]]) -> tuple[float, str, int]
```
```typescript
export type Pessoa = { nome: string; idade: number; sexo: string }
export function analisarPessoas(pessoas: Pessoa[]): [number, string, number]
```

## Stub TDD (para implementar)
Arquivos: `solution_ex056_analise_pessoas.py`, `solution.ts`. Testes: `test_ex056_analise_pessoas.py`, `solution.test.ts`.

```python
def analisar_pessoas(pessoas: list[tuple[str, int, str]]) -> tuple[float, str, int]:
    raise NotImplementedError
```
```typescript
export function analisarPessoas(pessoas: Pessoa[]): [number, string, number] {
  throw new Error("not implemented");
}
```
