# EX38 — Comparando Números

## Descrição
Escreva um programa que leia dois números inteiros e os compare, mostrando qual é maior ou se são iguais.

## Parâmetros e Tipos
- `a` (int) — primeiro número.
- `b` (int) — segundo número.

## Retorno
`str` — `"primeiro maior"` se `a > b`, `"segundo maior"` se `b > a`, `"iguais"` se forem iguais.

## Casos de Exemplo
```python
comparar_numeros(5, 2) -> "primeiro maior"
comparar_numeros(2, 5) -> "segundo maior"
comparar_numeros(3, 3) -> "iguais"
comparar_numeros(-1, 4) -> "segundo maior"
```

## Restrições / Edge Cases
- Caso `a == b`, retornar exatamente `"iguais"`.
- Aceita números inteiros negativos.

## Assinatura canônica

```python
def comparar_numeros(a: int, b: int) -> str:
```

```typescript
compararNumeros(a: number, b: number): string
```
