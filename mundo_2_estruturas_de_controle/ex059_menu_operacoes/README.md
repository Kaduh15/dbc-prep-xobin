# EX059 — Menu de operações

**Enunciado (Curso em Vídeo, DESAFIO 059):**
> Crie um programa que leia dois valores e mostre um menu na tela: (1) somar, (2) multiplicar, (3) maior, (4) novos números, (5) sair do programa.

## Descrição
O programa original é interativo (menu em loop). A lógica **testável e pura** é a que decide o resultado de cada operação sobre os dois valores lidos, de acordo com a opção escolhida.

## Parâmetros e Tipos
- `valor1` — `float`: primeiro valor.
- `valor2` — `float`: segundo valor.
- `opcao` — `int`: opção do menu.

## Retorno
- `float | None`:
  - `1` → `valor1 + valor2` (somar)
  - `2` → `valor1 * valor2` (multiplicar)
  - `3` → `max(valor1, valor2)` (maior)
  - outras (`4` novos números / `5` sair) → `None`

## Casos de Exemplo
```python
aplicar_menu(10, 5, 1)  # 15.0   somar
aplicar_menu(10, 5, 2)  # 50.0   multiplicar
aplicar_menu(10, 5, 3)  # 10.0   maior
aplicar_menu(4, 8, 3)   # 8.0    maior
aplicar_menu(10, 5, 5)  # None   sair
```

## Restrições / Edge Cases
- Opções interativas (`4` novos números, `5` sair) não produzem resultado numérico → `None`.
- Em TypeScript, `null` representa a ausência de resultado.

## Assinatura canônica
```python
def aplicar_menu(valor1: float, valor2: float, opcao: int) -> float | None
```
```typescript
export function aplicarMenu(valor1: number, valor2: number, opcao: number): number | null
```
