# EX022 — Análise do Nome Completo

## Descrição
Receba o **nome completo** de uma pessoa e retorne informações sobre ele: o nome em **maiúsculas**, o nome em **minúsculas**, o **total de letras** (desconsiderando espaços) e a **quantidade de letras do primeiro nome**.

## Parâmetros e Tipos
- `nome` (`str`): nome completo da pessoa.

## Formato do Retorno
Tupla `(maiusculas, minusculas, total_letras, letras_primeiro_nome)` — `tuple[str, str, int, int]`.

`total_letras` ignora qualquer espaço em branco; `letras_primeiro_nome` é `len(nome.split()[0])`.

## Casos de Exemplo
```python
analisar_nome("Maria Silva")      # ("MARIA SILVA", "maria silva", 10, 5)
analisar_nome("JOAO PEREIRA")     # ("JOAO PEREIRA", "joao pereira", 11, 4)
analisar_nome("A")                # ("A", "a", 1, 1)
analisar_nome("Ana Clara de Souza")  # ("ANA CLARA DE SOUZA", "ana clara de souza", 15, 3)
```

## Edge Cases / Extremos
- `total_letras` desconsidera **qualquer** espaço em branco (inclusive múltiplos espaços entre nomes).
- `letras_primeiro_nome` usa o **primeiro** token separado por espaço.
- Nome de um só token (`"Joao"`) → primeiro nome = nome inteiro.
- Espaços duplos internos (`"Ana  Paula"`) são preservados nas versões maiúscula/minúscula, mas ignorados na contagem de letras.
- Assume nome não vazio (existe ao menos um nome).
- Casos adicionados: `"Joao" → ("JOAO", "joao", 4, 4)`, `"LUIZ CARLOS" → (..., 10, 4)`, `"Ana  Paula" → (..., 8, 3)`.

## Abordagem / Dica
Python: `nome.upper()`, `nome.lower()`, `len("".join(nome.split()))` (remove todo espaço em branco) e `len(nome.split()[0])`. TypeScript: `nome.toUpperCase()`, `nome.toLowerCase()`, `nome.replace(/\s/g, "").length` e `nome.trim().split(/\s+/)[0].length`.

## Complexidade
Tempo O(n), espaço O(n), onde n = len(nome).

## Assinaturas / Stub
- **Python**: `analisar_nome(nome: str) -> tuple[str, str, int, int]`
- **TypeScript**: `analisarNome(nome: string): [string, string, number, number]`

Stub de partida (Python):
```python
def analisar_nome(nome: str) -> tuple[str, str, int, int]:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function analisarNome(nome: string): [string, string, number, number] {
  throw new Error("Not implemented");
}
```
