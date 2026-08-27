# Exercício 11 — Número Primo

## Descrição do Problema
Verifique se um inteiro positivo é primo. Números <= 1 não são primos.

## Parâmetros e Tipos Esperados
- n: int.

## Formato do Retorno
- bool

## Casos de Exemplo
```text
[
    ([1], False),
    ([2], True),
    ([3], True),
    ([4], False),
    ([17], True),
    ([97], True),
    ([100], False)
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def numero_primo(n: int) -> bool:`
- Assinatura em TypeScript: `export function numeroPrimo(n: number): boolean {`
