# EX46 — Contagem Regressiva

## Descrição
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0. A pausa de 1 segundo fica fora da função testável.

## Parâmetros e Tipos
- `inicio` (int, opcional) — número de partida, padrão `10`.

## Retorno
`list[int]` — sequência decrescente de `inicio` até `0`, inclusive.

## Casos de Exemplo
```python
contagem_regressiva()   -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
contagem_regressiva(3)  -> [3, 2, 1, 0]
contagem_regressiva(0)  -> [0]"
```

## Restrições / Edge Cases
- Sempre inclui o `0`.
- Parâmetro padrão `inicio=10`.

## Assinatura canônica

```python
def contagem_regressiva(inicio: int = 10) -> list[int]:
```

```typescript
contagemRegressiva(inicio: number = 10): number[]
```
