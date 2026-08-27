# EX42 — Tipo de Triângulo

## Descrição
Refaça o desafio dos triângulos (três retas formam um triângulo se cada lado for menor que a soma dos outros dois), acrescentando a classificação do tipo de triângulo formado: equilátero (três lados iguais), isósceles (dois lados iguais) ou escaleno (todos diferentes).

## Parâmetros e Tipos
- `a` (float) — primeira reta.
- `b` (float) — segunda reta.
- `c` (float) — terceira reta.

## Retorno
`str` — `"equilatero"`, `"isosceles"`, `"escaleno"` quando forma triângulo; `"invalido"` caso contrário.

## Casos de Exemplo
```python
tipo_triangulo(2, 2, 2) -> "equilatero"
tipo_triangulo(3, 3, 5) -> "isosceles"
tipo_triangulo(3, 4, 5) -> "escaleno"
tipo_triangulo(1, 1, 3) -> "invalido"
tipo_triangulo(10, 2, 3) -> "invalido"
```

## Restrições / Edge Cases
- Forma triângulo se `a<b+c`, `b<a+c` e `c<a+b`.
- Se não forma triângulo, retorna `"invalido"`.

## Assinatura canônica

```python
def tipo_triangulo(a: float, b: float, c: float) -> str:
```

```typescript
tipoTriangulo(a: number, b: number, c: number): string
```
