# EX053 — Palíndromo

**Enunciado (Curso em Vídeo, DESAFIO 053):**
> Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

## Descrição
Um palíndromo é uma frase que se lê da mesma forma de trás para frente. A função deve ignorar espaços e considerar maiúsculas/minúsculas como equivalentes para a comparação.

## Parâmetros e Tipos
- `frase` — `str`: texto a ser verificado.

## Retorno
- `bool`: `True` se a frase for palíndromo, senão `False`.

## Casos de Exemplo
```python
eh_palindromo("arara")                              # True
eh_palindromo("Ana")                                # True
eh_palindromo("a sacada da casa")                   # True
eh_palindromo("socorram me subi no onibus em marrocos")  # True
eh_palindromo("banana")                             # False
```

## Restrições / Edge Cases
- **Espaços são desconsiderados** (normalização: remover espaços).
- Comparação é **case-insensitive** (maiúsculas/minúsculas ignoradas).
- Acentos não são removidos; frases com acentuação podem precisar de normalização extra.

## Assinatura canônica
```python
def eh_palindromo(frase: str) -> bool
```
```typescript
export function ehPalindromo(frase: string): boolean
```
