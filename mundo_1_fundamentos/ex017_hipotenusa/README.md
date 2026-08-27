# EX017 — Hipotenusa

## Descrição
Dados o comprimento do **cateto oposto** e do **cateto adjacente** de um triângulo retângulo, calcule o comprimento da **hipotenusa**.

## Parâmetros e Tipos
- `cateto_oposto` (`float`): cateto oposto ao ângulo reto (um dos catetos).
- `cateto_adjacente` (`float`): cateto adjacente.

## Formato do Retorno
`float` — hipotenusa: `sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)`.

## Casos de Exemplo
```python
hipotenusa(3, 4)   # 5.0
hipotenusa(6, 8)   # 10.0
hipotenusa(5, 12)  # 13.0
```

## Restrições / Edge Cases
- Ambos os catetos são positivos em um triângulo real.
- O resultado é sempre maior que cada cateto.

## Assinaturas canônicas
- **Python**: `hipotenusa(cateto_oposto: float, cateto_adjacente: float) -> float`
- **TypeScript**: `hipotenusa(catetoOposto: number, catetoAdjacente: number): number`