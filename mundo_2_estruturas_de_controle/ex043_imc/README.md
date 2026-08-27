# EX43 — Índice de Massa Corporal (IMC)

## Descrição
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: IMC < 18.5 → Abaixo do Peso; 18.5 ≤ IMC < 25 → Peso Ideal; 25 ≤ IMC < 30 → Sobrepeso; 30 ≤ IMC < 40 → Obesidade; IMC ≥ 40 → Obesidade Mórbida.

## Parâmetros e Tipos
- `peso` (float) — peso em kg.
- `altura` (float) — altura em metros.

## Retorno
`str` — status conforme a tabela: `Abaixo do Peso`, `Peso Ideal`, `Sobrepeso`, `Obesidade` ou `Obesidade Morbida`.

## Casos de Exemplo
```python
imc(50, 1.75)  -> "Abaixo do Peso"
imc(70, 1.75)  -> "Peso Ideal"
imc(90, 1.75)  -> "Sobrepeso"
imc(110, 1.75) -> "Obesidade"
imc(130, 1.75) -> "Obesidade Morbida"
imc(60, 1.75)  -> "Peso Ideal"
```

## Restrições / Edge Cases
- Fórmula: `imc = peso / (altura ** 2)`.
- Faixas exatas conforme a tabela canônica.

## Assinatura canônica

```python
def imc(peso: float, altura: float) -> str:
```

```typescript
calcularImc(peso: number, altura: number): string
```
