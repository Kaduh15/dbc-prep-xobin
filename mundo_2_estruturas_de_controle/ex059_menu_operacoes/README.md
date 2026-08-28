# EX059 — Menu de operações

**Enunciado (Curso em Vídeo):**
> Crie um programa que leia dois valores e mostre um menu: (1) somar, (2) multiplicar, (3) maior, (4) novos números, (5) sair do programa.

## Descrição
O menu em loop é interativo; a lógica pura decide o resultado de cada operação sobre os dois valores, de acordo com a opção.

## Parâmetros e Tipos
- `valor1` — `float`: primeiro valor.
- `valor2` — `float`: segundo valor.
- `opcao` — `int`: opção do menu (1, 2 ou 3 operam; 4 e 5 não produzem resultado).

## Retorno
`float | None`: `1`→soma, `2`→produto, `3`→maior; opções `4`/`5` (e inválidas) → `None`.

## Casos de Exemplo
```python
aplicar_menu(10, 5, 1)  # 15.0
aplicar_menu(10, 5, 2)  # 50.0
aplicar_menu(10, 5, 3)  # 10.0
aplicar_menu(4, 8, 3)  # 8.0
aplicar_menu(10, 5, 5)  # None
aplicar_menu(10, 5, 4)  # None
```

## Edge Cases / Extremos
- **Decimais:** Soma/produto com floats (ex.: `10.5 + 2.5 = 13.0`).
- **Negativos:** Maior entre negativos (ex.: `max(-5, -3) = -3`).
- **Empate maior:** `max(7, 7) = 7`.
- **Opção inválida/fora do menu:** `0` ou `6` → `None`.

## Abordagem
Mapeamento direto da opção para a operação; opções sem operação retornam ausência de valor.

## Complexidade
Tempo O(1); Espaço O(1).

## Assinatura canônica
```python
def aplicar_menu(valor1: float, valor2: float, opcao: int) -> float | None
```
```typescript
export function aplicarMenu(valor1: number, valor2: number, opcao: number): number | null
```

## Stub TDD (para implementar)
Arquivos: `solution_ex059_menu_operacoes.py`, `solution.ts`. Testes: `test_ex059_menu_operacoes.py`, `solution.test.ts`.

```python
def aplicar_menu(valor1: float, valor2: float, opcao: int) -> float | None:
    raise NotImplementedError
```
```typescript
export function aplicarMenu(valor1: number, valor2: number, opcao: number): number | null {
  throw new Error("not implemented");
}
```
