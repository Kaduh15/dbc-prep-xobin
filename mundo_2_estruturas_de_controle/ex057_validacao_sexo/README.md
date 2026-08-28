# EX057 — Validação de sexo

**Enunciado (Curso em Vídeo):**
> Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

## Descrição
O laço/validação interativo do programa original fica fora da função pura. A lógica testável decide se um valor é aceito: apenas `'M'` ou `'F'`.

## Parâmetros e Tipos
- `sexo` — `str`: valor informado pelo usuário.

## Retorno
`bool`: `True` se `sexo` for exatamente `'M'` ou `'F'`; `False` caso contrário.

## Casos de Exemplo
```python
validar_sexo('M')  # True
validar_sexo('F')  # True
validar_sexo('m')  # False
validar_sexo('X')  # False
validar_sexo('')  # False
```

## Edge Cases / Extremos
- **Case-sensitive:** `'m'`/`'f'` são rejeitados.
- **Espaço em branco:** `' M'` / `'F '` → False.
- **Múltiplos caracteres:** `'MF'`, `'MO'` → False.
- **Vazia:** `''` → False.

## Abordagem
Compara exatamente o valor com `'M'` e `'F'` (pertença a um conjunto de dois valores).

## Complexidade
Tempo O(1); Espaço O(1).

## Assinatura canônica
```python
def validar_sexo(sexo: str) -> bool
```
```typescript
export function validarSexo(sexo: string): boolean
```

## Stub TDD (para implementar)
Arquivos: `solution_ex057_validacao_sexo.py`, `solution.ts`. Testes: `test_ex057_validacao_sexo.py`, `solution.test.ts`.

```python
def validar_sexo(sexo: str) -> bool:
    raise NotImplementedError
```
```typescript
export function validarSexo(sexo: string): boolean {
  throw new Error("not implemented");
}
```
