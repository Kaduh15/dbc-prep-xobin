# EX43 — Índice de Massa Corporal (IMC)

## Descrição
Leia o peso e a altura de uma pessoa, calcule o IMC (`peso / altura²`) e mostre seu status: **IMC < 18.5** → `Abaixo do Peso`; **18.5 ≤ IMC < 25** → `Peso Ideal`; **25 ≤ IMC < 30** → `Sobrepeso`; **30 ≤ IMC < 40** → `Obesidade`; **IMC ≥ 40** → `Obesidade Morbida`.

## Parâmetros e Tipos
- `peso` (float) — peso em kg.
- `altura` (float) — altura em metros.

## Retorno
`str` — `Abaixo do Peso`, `Peso Ideal`, `Sobrepeso`, `Obesidade` ou `Obesidade Morbida`.

## Casos de Exemplo
```python
imc(50, 1.75)  -> "Abaixo do Peso"
imc(70, 1.75)  -> "Peso Ideal"
imc(90, 1.75)  -> "Sobrepeso"
imc(110, 1.75) -> "Obesidade"
imc(130, 1.75) -> "Obesidade Morbida"
imc(60, 1.75)  -> "Peso Ideal"
```

## Casos de Teste (todos, incluindo extremos)
```python
# exemplos (altura 1.75)
((50, 1.75), 'Abaixo do Peso'), ((70, 1.75), 'Peso Ideal'),
((90, 1.75), 'Sobrepeso'), ((110, 1.75), 'Obesidade'),
((130, 1.75), 'Obesidade Morbida'), ((60, 1.75), 'Peso Ideal'),
# extremos: limites exatos 18.5 / 25 / 30 / 40 (altura=2 => imc = peso / 4)
((73, 2), 'Abaixo do Peso'), ((74, 2), 'Peso Ideal'),      # 18.5 exato (inclusivo)
((90, 2), 'Peso Ideal'), ((99, 2), 'Peso Ideal'),
((100, 2), 'Sobrepeso'), ((101, 2), 'Sobrepeso'),          # 25 exato (inclusivo)
((110, 2), 'Sobrepeso'), ((119, 2), 'Sobrepeso'),
((120, 2), 'Obesidade'), ((130, 2), 'Obesidade'),          # 30 exato (inclusivo)
((159, 2), 'Obesidade'),
((160, 2), 'Obesidade Morbida'), ((200, 2), 'Obesidade Morbida'),  # 40 exato (inclusivo)
```

## Edge Cases / Extremos
- Limites exatos **18.5**, **25**, **30** e **40** caem na faixa **superior** (limites inclusivos à esquerda: `18.5`, `25`, `30`, `40` pertencem a Peso Ideal / Sobrepeso / Obesidade / Obesidade Morbida).
- Abaixo de cada limite, o status cai na faixa anterior (ex.: `73` → 18.25 → Abaixo; `99` → 24.75 → Peso Ideal).
- `peso/4` com `altura=2` gera valores exatos para testar a borda sem erros de ponto flutuante.

## Abordagem / Dica
`valor = peso / (altura ** 2)`; comparar com `<` (`18.5`, `25`, `30`, `40`) encadeando as faixas. A última (≥ 40) é o `else`.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def imc(peso: float, altura: float) -> str:`
- **TypeScript**: `export function calcularImc(peso: number, altura: number): string`

> Stub para editar: `ex043_imc/solution_ex043_imc.py` (Python) e `solution.ts` (TS).
