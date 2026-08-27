# EX054 — Maioridade

**Enunciado (Curso em Vídeo, DESAFIO 054):**
> Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

## Descrição
Dado o ano de nascimento de N pessoas e um ano de referência, calcule a idade (`ano_atual - ano_nascimento`) de cada uma e conte quantas já são maiores de idade (≥ 18) e quantas ainda são menores.

> **Nota de determinismo:** o ano atual vira um parâmetro (`ano_atual`) para que a função seja pura e testável, independente do relógio do sistema.

## Parâmetros e Tipos
- `anos_nascimento` — `list[int]`: anos de nascimento de cada pessoa.
- `ano_atual` — `int`: ano de referência para calcular as idades.

## Retorno
- `tuple[int, int]`: `(maiores, menores)` — quantidade de maiores e de menores de idade.

## Casos de Exemplo
```python
# 3 maiores (2000, 2005, 1990), 4 menores (2015, 2012, 2008, 2010)
contagem_maioridade([2000, 2005, 2015, 1990, 2012, 2008, 2010], 2023)
# (3, 4)

contagem_maioridade([1990, 1991], 2023)  # (2, 0)
contagem_maioridade([2015, 2016], 2023)  # (0, 2)
contagem_maioridade([2005], 2023)        # (1, 0)  -> completa 18 em 2023
```

## Restrições / Edge Cases
- Maioridade: idade **≥ 18** (quem completa 18 no ano de referência é maior).
- Soma de `maiores + menores` é sempre igual ao tamanho da lista.
- Lista vazia → `(0, 0)`.

## Assinatura canônica
```python
def contagem_maioridade(anos_nascimento: list[int], ano_atual: int) -> tuple[int, int]
```
```typescript
export function contagemMaioridade(anosNascimento: number[], anoAtual: number): [number, number]
```
