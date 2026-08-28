# Exercício 001 — Olá, Mundo!

## Descrição do Problema
Crie um programa que escreva "Olá, mundo!" na tela.

## Parâmetros e Tipos Esperados
- Nenhum parâmetro.

## Formato do Retorno
- `str`: a mensagem literal `Olá, mundo!`.

## Casos de Exemplo
```
Input: (nenhum)
Output: "Olá, mundo!"
```

## Casos de Teste (todos, incluindo extremos)
```
((), "Olá, mundo!")
- Sempre retorna a mesma string (função determinística) e do tipo `str`.```

## Edge Cases / Extremos
Sem parâmetros: só existe uma saída válida. Verificar que o valor retornado é sempre exatamente `"Olá, mundo!"` (e do tipo `str`) — chamadas repetidas devem ser iguais (determinismo).

## Abordagem / Dica
Retorne o literal exato `"Olá, mundo!"`; nada de I/O para fora da função.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def ola_mundo() -> str:`
- **TypeScript**: `export function olaMundo(): string {`

> Stub para editar: `ex001_ola_mundo/solution_ex001_ola_mundo.py` (Python) e `solution.ts` (TS).
