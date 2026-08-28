# Exercício 002 — Boas-Vindas

## Descrição do Problema
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

## Parâmetros e Tipos Esperados
- `nome: str` — o nome da pessoa a ser saudada.

## Formato do Retorno
- `str`: a mensagem `Olá, {nome}! Seja muito bem-vindo(a)!`.

## Casos de Exemplo
```
Input: "João"
Output: "Olá, João! Seja muito bem-vindo(a)!"

Input: "Maria"
Output: "Olá, Maria! Seja muito bem-vindo(a)!"
```

## Casos de Teste (todos, incluindo extremos)
```
(("João",), "Olá, João! Seja muito bem-vindo(a)!")
(("Maria",), "Olá, Maria! Seja muito bem-vindo(a)!")
(("",), "Olá, ! Seja muito bem-vindo(a)!")
(("Ana Clara",), "Olá, Ana Clara! Seja muito bem-vindo(a)!")
((" ",), "Olá,  ! Seja muito bem-vindo(a)!")
(("Zé",), "Olá, Zé! Seja muito bem-vindo(a)!")```

## Edge Cases / Extremos
Nome vazio (`""`) ainda produz mensagem válida. Nome só de espaços produz espaços duplicados na saída (a interpolação preserva os espaços). Nomes compostos com espaço interno são preservados tal como informados.

## Abordagem / Dica
Use interpolação/`f-string` com o mesmo template exato `Olá, {nome}! Seja muito bem-vindo(a)!`. Não normalize (trim) o nome — a saída deve espelhar o texto de entrada.

## Complexidade
- Tempo O(n) (tamanho do nome), espaço O(n).

## Assinatura Canônica
- **Python**: `def boas_vindas(nome: str) -> str:`
- **TypeScript**: `export function boasVindas(nome: string): string {`

> Stub para editar: `ex002_boas_vindas/solution_ex002_boas_vindas.py` (Python) e `solution.ts` (TS).
