# Exercício 02 — Palíndromo

## Descrição do Problema
Verifique se uma string é palíndromo (igual de trás pra frente), ignorando maiúsculas/minúsculas e ignorando caracteres não alfanuméricos.

## Parâmetros e Tipos Esperados
- texto: str.

## Formato do Retorno
- bool

## Casos de Exemplo
```text
[
    (['ana'], True),
    (['hello'], False),
    (['A man a plan a canal Panama'], True),
    ([''], True),
    (['anA'], True),
    (['never odd or even'], True),
    (['java'], False)
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def palindromo(texto: str) -> bool:`
- Assinatura em TypeScript: `export function palindromo(texto: string): boolean {`
