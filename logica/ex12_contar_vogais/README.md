# Exercício 12 — Contagem de Vogais

## Descrição do Problema
Retorne a quantidade de vogais (a, e, i, o, u) em uma string, ignorando maiúsculas.

## Parâmetros e Tipos Esperados
- texto: str.

## Formato do Retorno
- int

## Casos de Exemplo
```text
[
    (['hello'], 2),
    (['Banana'], 3),
    (['xyz'], 0),
    (['AEIOU'], 5),
    ([''], 0),
    (['ritmo'], 2)
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def contar_vogais(texto: str) -> int:`
- Assinatura em TypeScript: `export function contarVogais(texto: string): number {`
