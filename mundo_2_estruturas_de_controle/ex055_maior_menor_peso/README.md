# EX055 — Maior e menor peso

**Enunciado (Curso em Vídeo):**
> Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

## Descrição
Dada uma lista de pesos (ex.: de cinco pessoas), retorne o maior e o menor valor.

## Parâmetros e Tipos
- `pesos` — `list[float]`: lista com os pesos lidos.

## Retorno
`tuple[float, float]`: **(maior peso, menor peso)**, nesta ordem.

## Casos de Exemplo
```python
maior_menor_peso([70.5, 80.0, 55.3, 90.2, 62.1])  # (90.2, 55.3)
maior_menor_peso([100.0, 20.0, 40.0])  # (100.0, 20.0)
maior_menor_peso([50.0, 50.0])  # (50.0, 50.0)
```

## Edge Cases / Extremos
- **Ordem invertida:** `[20, 100, 40]` ainda retorna `(100.0, 20.0)` (maior primeiro).
- **Um elemento:** `(v, v)`.
- **Empate:** Todos iguais → maior == menor.
- **Decimais:** Pesos fracionários retornados sem alteração.

## Abordagem
Varre a lista mantendo o maior e o menor vistos até então.

## Complexidade
Tempo O(n); Espaço O(1).

## Assinatura canônica
```python
def maior_menor_peso(pesos: list[float]) -> tuple[float, float]
```
```typescript
export function maiorMenorPeso(pesos: number[]): [number, number]
```

## Stub TDD (para implementar)
Arquivos: `solution_ex055_maior_menor_peso.py`, `solution.ts`. Testes: `test_ex055_maior_menor_peso.py`, `solution.test.ts`.

```python
def maior_menor_peso(pesos: list[float]) -> tuple[float, float]:
    raise NotImplementedError
```
```typescript
export function maiorMenorPeso(pesos: number[]): [number, number] {
  throw new Error("not implemented");
}
```
