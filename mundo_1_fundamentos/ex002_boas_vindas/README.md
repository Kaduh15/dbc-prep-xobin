# Exercício 002 — Boas-Vindas

## Descrição do Problema
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

## Parâmetros e Tipos Esperados
- `nome: str` — o nome da pessoa a ser saudada.

## Formato do Retorno
- `str`: a mensagem `Olá, {nome}! Seja muito bem-vindo(a)!`.

## Assinatura Canônica
- **Python**: `boas_vindas(nome: str) -> str`
- **TypeScript**: `boasVindas(nome: string): string`

## Casos de Exemplo
```
Input: "João"
Output: "Olá, João! Seja muito bem-vindo(a)!"

Input: "Maria"
Output: "Olá, Maria! Seja muito bem-vindo(a)!"
```

## Restrições / Edge Cases
- Função determinística: mesmo nome implica sempre a mesma mensagem.
- Nome vazio (`""`) ainda produz mensagem válida.