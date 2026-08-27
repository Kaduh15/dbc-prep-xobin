# Exercício 06 — Contagem de Caracteres

## Descrição do Problema
Retorne a frequência de cada caractere na string (chaves = caracteres distintos, case-sensitive).

## Parâmetros e Tipos Esperados
- texto: str.

## Formato do Retorno
- dict (char -> quantidade)

## Casos de Exemplo
```text
[
    (['banana'], {'b': 1, 'a': 3, 'n': 2}),
    ([''], {}),
    (['aA'], {'a': 1, 'A': 1}),
    (['aba'], {'a': 2, 'b': 1})
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def contar_caracteres(texto: str) -> dict:`
- Assinatura em TypeScript: `export function contarCaracteres(texto: string): Record<string, number> {`
