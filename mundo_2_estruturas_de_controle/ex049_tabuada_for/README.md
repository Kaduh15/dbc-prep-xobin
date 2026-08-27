# EX049 — Tabuada com laço for

**Enunciado (Curso em Vídeo, DESAFIO 009 refeito):**
> Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço **for**.

## Descrição
Dado um número inteiro `n`, calcule e retorne os dez resultados da sua tabuada (de `n x 1` até `n x 10`), usando um laço `for`.

## Parâmetros e Tipos
- `n` — `int`: número cuja tabuada será calculada.

## Retorno
- `list[int]`: lista com os produtos `[n*1, n*2, ..., n*10]`.

## Casos de Exemplo
```python
tabuada(5)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
tabuada(7)  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
tabuada(0)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Restrições / Edge Cases
- Funciona para inteiros positivos, negativos e zero.
- Os 10 resultados correspondem aos multiplicadores de 1 a 10.

## Assinatura canônica
```python
def tabuada(n: int) -> list[int]
```
```typescript
export function tabuada(n: number): number[]
```
