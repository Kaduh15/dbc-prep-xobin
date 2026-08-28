# EX023 — Dígitos de um Número

## Descrição
Receba um número inteiro entre **0 e 9999** e decomponha-o, retornando separadamente os dígitos de **unidade**, **dezena**, **centena** e **milhar**.

## Parâmetros e Tipos
- `numero` (`int`): número entre 0 e 9999.

## Formato do Retorno
Tupla `(unidade, dezena, centena, milhar)` — `tuple[int, int, int, int]`.

## Casos de Exemplo
```python
decompor_numero(1834)  # (4, 3, 8, 1)
decompor_numero(5)     # (5, 0, 0, 0)
decompor_numero(2764)  # (4, 6, 7, 2)
decompor_numero(0)     # (0, 0, 0, 0)
decompor_numero(100)   # (0, 0, 1, 0)
decompor_numero(9999)  # (9, 9, 9, 9)  // valor máximo
```

## Edge Cases / Extremos
- Números com menos de 4 dígitos têm posições superiores preenchidas com `0` (`5 → (5, 0, 0, 0)`).
- `0 → (0, 0, 0, 0)`.
- Limite superior `9999 → (9, 9, 9, 9)`.
- Valores como `10 → (0, 1, 0, 0)` e `1000 → (0, 0, 0, 1)` exercitam cada casa isoladamente.
- Casos adicionados: `9999 → (9,9,9,9)`, `10 → (0,1,0,0)`, `1000 → (0,0,0,1)`, `1234 → (4,3,2,1)`.

## Abordagem / Dica
Extraia cada casa por divisão e módulo por 10: unidade `n % 10`, dezena `(n // 10) % 10`, centena `(n // 100) % 10`, milhar `(n // 1000) % 10`. No TypeScript `//` não existe — use `Math.floor(n / 10)`.

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `decompor_numero(numero: int) -> tuple[int, int, int, int]`
- **TypeScript**: `decomporNumero(numero: number): [number, number, number, number]`

Stub de partida (Python):
```python
def decompor_numero(numero: int) -> tuple[int, int, int, int]:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function decomporNumero(numero: number): [number, number, number, number] {
  throw new Error("Not implemented");
}
```
