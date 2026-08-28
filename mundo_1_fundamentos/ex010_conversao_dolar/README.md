# Exercício 010 — Conversão de Reais para Dólares

## Descrição do Problema
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

## Parâmetros e Tipos Esperados
- `reais: float` — quantia em reais disponível na carteira.
- `cotacao: float = 3.27` — valor de um dólar em reais (padrão histórico usado no curso; pode ser informado na chamada).

## Formato do Retorno
- `float`: a quantidade de dólares comprável, `reais / cotacao`.

## Casos de Exemplo
```
Input: (327, 3.27)   Output: 100.0
Input: (100, 5.0)    Output: 20.0
Input: (0, 3.27)     Output: 0.0
Input: (3.27)        -> cotação padrão, Output: 1.0
```

## Casos de Teste (todos, incluindo extremos)
```
((327, 3.27), 100.0)   ((100, 5.0), 20.0)   ((0, 3.27), 0.0)
((3.27, 3.27), 1.0)   ((3.27,), 1.0)       ((50, 5.0), 10.0)
((200, 4.0), 50.0)    ((1, 2.0), 0.5)
- Caso `(3.27,)` exercita a cotação padrão (omitida na chamada).```

## Edge Cases / Extremos
Cotação padrão é `3.27` (valor de referência do exercício original) — chamar sem o segundo argumento deve usá-la. Reais zero retornam `0.0`. Divisões podem gerar dízimas — compare sempre com tolerância (`pytest.approx` / `toBeCloseTo`). Cotação deve ser > 0 (evita divisão por zero).

## Abordagem / Dica
Retorne `reais / cotacao`. O argumento `cotacao` tem valor padrão `3.27`; quem chamar omitindo-o recebe a conversão pela cotação padrão. Não arredonde — o consumidor compara com aproximação.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def converter_dolar(reais: float, cotacao: float = 3.27) -> float:`
- **TypeScript**: `export function converterDolar(reais: number, cotacao: number = 3.27): number {`

> Stub para editar: `ex010_conversao_dolar/solution_ex010_conversao_dolar.py` (Python) e `solution.ts` (TS).
