# EX054 — Maioridade

**Enunciado (Curso em Vídeo):**
> Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

## Descrição
Dado o ano de nascimento de N pessoas e um ano de referência, calcule a idade (`ano_atual - ano_nascimento`) e conte quantas são maiores de idade (≥ 18) e quantas ainda são menores. O ano atual é um parâmetro para manter a função pura e determinística.

## Parâmetros e Tipos
- `anos_nascimento` — `list[int]`: anos de nascimento de cada pessoa.
- `ano_atual` — `int`: ano de referência para calcular as idades.

## Retorno
`tuple[int, int]`: `(maiores, menores)`.

## Casos de Exemplo
```python
contagem_maioridade([2000, 2005, 2015, 1990, 2012, 2008, 2010], 2023)  # (3, 4)
contagem_maioridade([1990, 1991], 2023)  # (2, 0)
contagem_maioridade([2015, 2016], 2023)  # (0, 2)
contagem_maioridade([2005], 2023)  # (1, 0)
```

## Edge Cases / Extremos
- **Fronteira exata:** Quem completa 18 no ano de referência é maior (2005 @ 2023 → maior).
- **Lista vazia:** `(0, 0)`.
- **Nascimento futuro:** Idade negativa → contado como menor.
- **Todos maiores/todos menores:** Caso extremo `(len, 0)` ou `(0, len)`.

## Abordagem
Uma passada calculando a idade de cada pessoa; conta `maiores` quando `idade >= 18` e deriva `menores = total - maiores`.

## Complexidade
Tempo O(n); Espaço O(1).

## Assinatura canônica
```python
def contagem_maioridade(anos_nascimento: list[int], ano_atual: int) -> tuple[int, int]
```
```typescript
export function contagemMaioridade(anosNascimento: number[], anoAtual: number): [number, number]
```

## Stub TDD (para implementar)
Arquivos: `solution_ex054_maioridade.py`, `solution.ts`. Testes: `test_ex054_maioridade.py`, `solution.test.ts`.

```python
def contagem_maioridade(anos_nascimento: list[int], ano_atual: int) -> tuple[int, int]:
    raise NotImplementedError
```
```typescript
export function contagemMaioridade(anosNascimento: number[], anoAtual: number): [number, number] {
  throw new Error("not implemented");
}
```
