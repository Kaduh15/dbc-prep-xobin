# EX057 — Validação de sexo

**Enunciado (Curso em Vídeo, DESAFIO 057):**
> Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

## Descrição
O laço de repetição/validação do programa original é interativo. A lógica **testável** é a que decide se um valor é aceito: apenas `'M'` ou `'F'`.

## Parâmetros e Tipos
- `sexo` — `str`: valor informado pelo usuário.

## Retorno
- `bool`: `True` se `sexo` for exatamente `'M'` ou `'F'`; `False` caso contrário.

## Casos de Exemplo
```python
validar_sexo("M")   # True
validar_sexo("F")   # True
validar_sexo("m")   # False
validar_sexo("X")   # False
validar_sexo("")    # False
```

## Restrições / Edge Cases
- Comparação **exata e case-sensitive**: `'m'`/`'f'` (minúsculas) são rejeitados.
- String vazia ou com mais de um caractere → `False`.
- O laço do enunciado original (repetir até validar) fica **fora** da função pura.

## Assinatura canônica
```python
def validar_sexo(sexo: str) -> bool
```
```typescript
export function validarSexo(sexo: string): boolean
```
