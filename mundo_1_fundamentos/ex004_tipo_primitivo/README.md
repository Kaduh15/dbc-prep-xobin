# Exercício 004 — Tipo Primitivo e Informações

## Descrição do Problema
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

Para tornar o exercício testável, a função analisa uma string e retorna um dicionário com o tipo primitivo e os predicados típicos da classe `str`.

## Parâmetros e Tipos Esperados
- `valor: str` — o valor a ser analisado (sempre tratado como string).

## Formato do Retorno
- `dict[str, str | bool]` com as chaves:
  - `tipo`: `"str"` (tipo primitivo)
  - `so_espacos`: `valor.isspace()`
  - `e_numero`: `valor.isnumeric()`
  - `e_alfabetico`: `valor.isalpha()`
  - `e_alfanumerico`: `valor.isalnum()`
  - `em_maiusculas`: `valor.isupper()`
  - `em_minusculas`: `valor.islower()`
  - `capitalizada`: `valor.istitle()`

## Assinatura Canônica
- **Python**: `analisar_valor(valor: str) -> dict`
- **TypeScript**: `analisarValor(valor: string): Record<string, string | boolean>`

## Casos de Exemplo
```
Input: "Python"
Output: {"tipo": "str", "so_espacos": False, "e_numero": False,
         "e_alfabetico": True, "e_alfanumerico": True,
         "em_maiusculas": False, "em_minusculas": True, "capitalizada": True}

Input: "1234"
Output: {"tipo": "str", "so_espacos": False, "e_numero": True,
         "e_alfabetico": False, "e_alfanumerico": True,
         "em_maiusculas": False, "em_minusculas": False, "capitalizada": False}

Input: "   "
Output: {"tipo": "str", "so_espacos": True, "e_numero": False,
         "e_alfabetico": False, "e_alfanumerico": False,
         "em_maiusculas": False, "em_minusculas": False, "capitalizada": False}
```

## Restrições / Edge Cases
- Entrada sempre tratada como string (mantém fidelidade ao `input()` original).
- String vazia e strings só de espaços são válidas.