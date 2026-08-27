# Exercício 01 — FizzBuzz

## Descrição do Problema
Para um inteiro positivo n, retorne:
- "FizzBuzz" se múltiplo de 3 e 5;
- "Fizz" se múltiplo de 3 (e não de 5);
- "Buzz" se múltiplo de 5 (e não de 3);
- o número como string, caso contrário.

## Parâmetros e Tipos Esperados
- n: int (>= 1).

## Formato do Retorno
- str

## Casos de Exemplo
```text
[
    ([1], '1'),
    ([3], 'Fizz'),
    ([5], 'Buzz'),
    ([15], 'FizzBuzz'),
    ([9], 'Fizz'),
    ([10], 'Buzz'),
    ([30], 'FizzBuzz'),
    ([7], '7')
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def fizzbuzz(n: int) -> str:`
- Assinatura em TypeScript: `export function fizzbuzz(n: number): string {`
