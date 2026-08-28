# Exercício 004 — Tipo Primitivo e Informações

## Descrição do Problema
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

Para tornar o exercício testável, a função analisa uma string e retorna um dicionário com o tipo primitivo e os predicados típicos da classe `str`.

## Parâmetros e Tipos Esperados
- `valor: str` — o valor a ser analisado (sempre tratado como string).

## Formato do Retorno
- `dict[str, str | bool]` com as chaves:
  - `tipo`: `"str"`
  - `so_espacos`: `valor.isspace()`
  - `e_numero`: `valor.isnumeric()`
  - `e_alfabetico`: `valor.isalpha()`
  - `e_alfanumerico`: `valor.isalnum()`
  - `em_maiusculas`: `valor.isupper()`
  - `em_minusculas`: `valor.islower()`
  - `capitalizada`: `valor.istitle()`

## Casos de Exemplo
```
Input: "Python"  -> {"tipo": "str", "so_espacos": False, "e_numero": False,
                   "e_alfabetico": True, "e_alfanumerico": True,
                   "em_maiusculas": False, "em_minusculas": False, "capitalizada": True}
Input: "1234"    -> {"tipo": "str", "so_espacos": False, "e_numero": True,
                   "e_alfabetico": False, "e_alfanumerico": True, ...}
Input: "   "     -> {"tipo": "str", "so_espacos": True, ...}
```

## Casos de Teste (todos, incluindo extremos)
```
(("Python",), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": True, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": False, "capitalizada": True})
(("1234",), {"tipo": "str", "so_espacos": False, "e_numero": True, "e_alfabetico": False, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": False, "capitalizada": False})
(("   ",), {"tipo": "str", "so_espacos": True, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": False, "em_maiusculas": False, "em_minusculas": False, "capitalizada": False})
(("",), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": False, "em_maiusculas": False, "em_minusculas": False, "capitalizada": False})
(("ABC",), {"tipo": "str", "e_alfabetico": True, "e_alfanumerico": True, "em_maiusculas": True, "em_minusculas": False, "capitalizada": False})
(("abc",), {"tipo": "str", "e_alfabetico": True, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": True, "capitalizada": False})
(("Hello World",), {"tipo": "str", "em_maiusculas": False, "em_minusculas": False, "capitalizada": True})
(("12A",), {"tipo": "str", "e_alfanumerico": True, "em_maiusculas": True, "em_minusculas": False, "capitalizada": True})
(("123abc",), {"tipo": "str", "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": True, "capitalizada": False})
(("   X",), {"tipo": "str", "em_maiusculas": True, "em_minusculas": False, "capitalizada": True})```

## Edge Cases / Extremos
String vazia (`""`) não é só-espaços nem título. Maiúsculas puras (`"ABC"`) têm `capitalizada = False` (istitle exige apenas a 1ª letra de cada palavra maiúscula). Misturas letras+números (`"12A"`, `"123abc"`) dependem de cada predicado. Espaços no início (`"   X"`) não impedem `isupper()`/`istitle()`. **Nota:** `"Python".islower()` é `False` (o `P` é maiúsculo) — o caso canônico original registrava `em_minusculas: True`, valor factualmente incorreto corrigido para `False`.

## Abordagem / Dica
Delegação direta aos métodos da classe `str` em Python (`isspace`, `isnumeric`, `isalpha`, `isalnum`, `isupper`, `islower`, `istitle`). Em TS, reproduza os predicados com string/RegExp (espaços, dígitos, letras ASCII, maiúsculas/minúsculas e o conceito de 'title case').

## Complexidade
- Tempo O(n), espaço O(n) (tamanho da string de entrada).

## Assinatura Canônica
- **Python**: `def analisar_valor(valor: str) -> dict:`
- **TypeScript**: `export function analisarValor(valor: string): Record<string, string | boolean> {`

> Stub para editar: `ex004_tipo_primitivo/solution_ex004_tipo_primitivo.py` (Python) e `solution.ts` (TS).
