# Exercício 007 — Média de Duas Notas

## Descrição do Problema
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

## Parâmetros e Tipos Esperados
- `n1: float` — primeira nota (0 a 10).
- `n2: float` — segunda nota (0 a 10).

## Formato do Retorno
- `float`: a média aritmética `(n1 + n2) / 2`.

## Assinatura Canônica
- **Python**: `media_notas(n1: float, n2: float) -> float`
- **TypeScript**: `mediaNotas(n1: number, n2: number): number`

## Casos de Exemplo
```
Input: (7, 7)
Output: 7.0

Input: (5.5, 8.5)
Output: 7.0

Input: (10, 2)
Output: 6.0

Input: (0, 0)
Output: 0.0
```

## Restrições / Edge Cases
- Notas podem ser decimais.
- Média de duas notas iguais resulta na própria nota.