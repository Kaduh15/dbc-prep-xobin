# EX014 — Conversor de Temperatura

## Descrição
Receba uma temperatura em graus **Celsius** e converta para graus **Fahrenheit**.

## Parâmetros e Tipos
- `celsius` (`float`): temperatura em graus Celsius (°C).

## Formato do Retorno
`float` — temperatura equivalente em graus Fahrenheit (°F).

Fórmula: `fahrenheit = celsius * 9 / 5 + 32`.

## Casos de Exemplo
```python
celsius_para_fahrenheit(0)    # 32.0
celsius_para_fahrenheit(100)  # 212.0
celsius_para_fahrenheit(-40)  # -40.0
celsius_para_fahrenheit(37)   # 98.6
```

## Restrições / Edge Cases
- Conversão linear; aceita valores negativos e fracionários.
- Em `-40°C` Celsius e Fahrenheit coincidem (`-40.0`).

## Assinaturas canônicas
- **Python**: `celsius_para_fahrenheit(celsius: float) -> float`
- **TypeScript**: `celsiusParaFahrenheit(celsius: number): number`