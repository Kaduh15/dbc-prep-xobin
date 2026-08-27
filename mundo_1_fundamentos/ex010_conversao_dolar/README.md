# Exercício 010 — Conversão de Reais para Dólares

## Descrição do Problema
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

## Parâmetros e Tipos Esperados
- `reais: float` — quantia em reais disponível na carteira.
- `cotacao: float = 3.27` — valor de um dólar em reais (padrão histórico usado no curso; pode ser informado na chamada).

## Formato do Retorno
- `float`: a quantidade de dólares comprável, `reais / cotacao`.

## Assinatura Canônica
- **Python**: `converter_dolar(reais: float, cotacao: float = 3.27) -> float`
- **TypeScript**: `converterDolar(reais: number, cotacao: number = 3.27): number`

## Casos de Exemplo
```
Input: (327, 3.27)
Output: 100.0

Input: (100, 5.0)
Output: 20.0

Input: (0, 3.27)
Output: 0.0

Input: (3.27)   -> cotação padrão
Output: 1.0
```

## Restrições / Edge Cases
- Cotação padrão de 3.27 (valor de referência do exercício original).
- Comparações de divisão com float devem usar tolerância (`pytest.approx` / `toBeCloseTo`).
- Cotação deve ser > 0 (evitar divisão por zero).