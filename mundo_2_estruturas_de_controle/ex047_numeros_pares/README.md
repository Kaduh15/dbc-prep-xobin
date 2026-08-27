# EX47 — Números Pares no Intervalo

## Descrição
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

## Parâmetros e Tipos
- `inicio` (int, opcional) — limite inferior, padrão `1`.
- `fim` (int, opcional) — limite superior, padrão `50`.

## Retorno
`list[int]` — todos os números pares no intervalo `[inicio, fim]` (inclusive), em ordem crescente.

## Casos de Exemplo
```python
numeros_pares()       -> [2, 4, 6, ..., 48, 50]
numeros_pares(1, 10)  -> [2, 4, 6, 8, 10]
numeros_pares(15, 25) -> [16, 18, 20, 22, 24]
numeros_pares(3, 3)   -> []"
```

## Restrições / Edge Cases
- Intervalo inclusivo nas duas pontas.
- Se não houver par, retorna lista vazia.

## Assinatura canônica

```python
def numeros_pares(inicio: int = 1, fim: int = 50) -> list[int]:
```

```typescript
numerosPares(inicio: number = 1, fim: number = 50): number[]
```
