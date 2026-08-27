# EX48 — Soma dos Múltiplos de 3

## Descrição
Faça um programa que calcule a soma entre todos os números múltiplos de 3 que se encontram no intervalo de 1 até 500.

## Parâmetros e Tipos
- `inicio` (int, opcional) — limite inferior, padrão `1`.
- `fim` (int, opcional) — limite superior, padrão `500`.

## Retorno
`int` — soma de todos os múltiplos de 3 no intervalo `[inicio, fim]` (inclusive).

## Casos de Exemplo
```python
soma_multiplos_de_3()      -> 41583
soma_multiplos_de_3(1, 10)  -> 18
soma_multiplos_de_3(5, 12)  -> 27
soma_multiplos_de_3(1, 6)   -> 9"
```

## Restrições / Edge Cases
- Intervalo inclusivo.
- `soma_multiplos_de_3()` = soma de 3,6,9,... até 498 = **41583**.

## Assinatura canônica

```python
def soma_multiplos_de_3(inicio: int = 1, fim: int = 500) -> int:
```

```typescript
somaMultiplosDe3(inicio: number = 1, fim: number = 500): number
```
