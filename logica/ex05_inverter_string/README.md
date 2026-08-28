# Exercício 05 — Inverter String

## Descrição do Problema
Dada uma string, retorne a versão invertida.

## Parâmetros e Tipos Esperados
- texto: str

## Formato do Retorno
- str: string invertida

## Casos de Exemplo
```python
# (args) -> esperado
    (('hello',), 'olleh'),
    (('',), ''),
    (('abc',), 'cba'),
    (('a',), 'a'),
    (('a man',), 'nam a'),
```

## Casos de Teste (todos, incluindo extremos)
```python
    (('hello',), 'olleh'),
    (('',), ''),
    (('abc',), 'cba'),
    (('a',), 'a'),
    (('a man',), 'nam a'),
    (('olá mundo',), 'odnum álo'),
```

## Edge Cases / Extremos
String vazia; um único caractere; acentos/unicode („olá mundo“); espaços; inversão que muda a ordem das palavras.

## Abordagem / Dica
Itere do fim para o início concatenando (Python [::-1]; TS split/reverse/join). Simples e determinístico.

## Complexidade
- Tempo O(n), espaço O(n)

## Assinatura Canônica
- **Python**: `def inverter_string(texto: str) -> str:`
- **TypeScript**: `export function inverterString(texto: string): string {`

> Stub para editar: `ex05_inverter_string/solution_ex05_inverter_string.py` (Python) e `solution.ts` (TS).

