# EX018 — Seno, Cosseno e Tangente

## Descrição
Receba um ângulo em **graus** e retorne os valores de **seno**, **cosseno** e **tangente** desse ângulo.

## Parâmetros e Tipos
- `angulo` (`float`): ângulo em graus.

## Formato do Retorno
Tupla `(seno, cosseno, tangente)` de `float` (`tuple[float, float, float]`), nessa ordem.

## Casos de Exemplo
```python
trigonometria(0)   # (0.0, 1.0, 0.0)
trigonometria(30)  # (0.5, 0.866025..., 0.577350...)
trigonometria(45)  # (0.707106..., 0.707106..., 1.0)
```

## Restrições / Edge Cases
- O ângulo é fornecido em graus e convertido para radianos internamente.
- Em `90°` a tangente tende a infinito; evite valores de borda no caso base.
- Valores trigonométricos usam aproximação de ponto flutuante (compare com tolerância).

## Assinaturas canônicas
- **Python**: `trigonometria(angulo: float) -> tuple[float, float, float]`
- **TypeScript**: `trigonometria(angulo: number): [number, number, number]`