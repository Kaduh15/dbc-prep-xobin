# Exercício 01 — FizzBuzz

## Descrição do Problema
Dado um inteiro n, retorne "FizzBuzz" se for múltiplo de 15, "Fizz" se múltiplo de 3, "Buzz" se múltiplo de 5; caso contrário, o número como string.

## Parâmetros e Tipos Esperados
- n: int

## Formato do Retorno
- str: "FizzBuzz" | "Fizz" | "Buzz" | o número como string

## Casos de Exemplo
```python
# (args) -> esperado
    ((15,), 'FizzBuzz'),
    ((3,), 'Fizz'),
    ((5,), 'Buzz'),
    ((1,), '1'),
    ((30,), 'FizzBuzz'),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((15,), 'FizzBuzz'),
    ((3,), 'Fizz'),
    ((5,), 'Buzz'),
    ((1,), '1'),
    ((30,), 'FizzBuzz'),
    ((0,), 'FizzBuzz'),
    ((-3,), 'Fizz'),
    ((45,), 'FizzBuzz'),
    ((7,), '7'),
```

## Edge Cases / Extremos
Múltiplo exato (0, 15, 30, 45); múltiplo só de 3 ou só de 5; números negativos (ex.: -3 é Fizz); números não múltiplos.

## Abordagem / Dica
Cheque a divisibilidade na ordem 15 → 3 → 5 → número. O módulo % captura os múltiplos; a ordem importa para não mascarar o FizzBuzz.

## Complexidade
- Tempo O(1), espaço O(1)

## Assinatura Canônica
- **Python**: `def fizzbuzz(n: int) -> str:`
- **TypeScript**: `export function fizzbuzz(n: number): string {`

> Stub para editar: `ex01_fizzbuzz/solution_ex01_fizzbuzz.py` (Python) e `solution.ts` (TS).

