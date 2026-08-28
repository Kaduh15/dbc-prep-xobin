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
celsius_para_fahrenheit(0)      # 32.0
celsius_para_fahrenheit(100)    # 212.0
celsius_para_fahrenheit(-40)    # -40.0  (coincidência Celsius=Fahrenheit)
celsius_para_fahrenheit(37)     # 98.6
celsius_para_fahrenheit(25)     # 77.0
celsius_para_fahrenheit(-273.15)# -459.67  (zero absoluto)
```

## Edge Cases / Extremos
- Conversão linear; aceita valores negativos e fracionários.
- Em `-40°C` Celsius e Fahrenheit coincidem (`-40.0`).
- Zero absoluto `-273.15°C` ⟹ `-459.67°F` (valor exato com a fórmula).
- Casos adicionados: `-273.15 → -459.67`, `1 → 33.8`, `-10 → 14.0`, `50 → 122.0`.

## Abordagem / Dica
Aplicar diretamente `celsius * 9 / 5 + 32`. O operador `/` no Python produz `float` exato; no TypeScript o mesmo resultado é obtido com `* 9 / 5 + 32`. Use comparação com tolerância (ponto flutuante).

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `celsius_para_fahrenheit(celsius: float) -> float`
- **TypeScript**: `celsiusParaFahrenheit(celsius: number): number`

Stub de partida (Python):
```python
def celsius_para_fahrenheit(celsius: float) -> float:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function celsiusParaFahrenheit(celsius: number): number {
  throw new Error("Not implemented");
}
```
