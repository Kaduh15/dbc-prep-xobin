# Exercício 03 — Anagrama

## Descrição do Problema
Verifique se duas strings são anagramas (mesmos caracteres na mesma quantidade, em qualquer ordem), ignorando maiúsculas/minúsculas e espaços.

## Parâmetros e Tipos Esperados
- a: str, b: str.

## Formato do Retorno
- bool

## Casos de Exemplo
```text
[
    (['listen', 'silent'], True),
    (['ana', 'naa'], True),
    (['hello', 'world'], False),
    (['', ''], True),
    (['aabb', 'abab'], True),
    (['abc', 'abcd'], False)
]
```

## Restrição
- Trate entradas vazias quando fizer sentido.
- Assinatura em Python: `def anagrama(a: str, b: str) -> bool:`
- Assinatura em TypeScript: `export function anagrama(a: string, b: string): boolean {`
