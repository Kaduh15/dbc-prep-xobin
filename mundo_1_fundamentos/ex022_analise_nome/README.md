# EX022 — Análise do Nome Completo

## Descrição
Receba o **nome completo** de uma pessoa e retorne informações sobre ele: o nome em **maiúsculas**, o nome em **minúsculas**, o **total de letras** (desconsiderando espaços) e a **quantidade de letras do primeiro nome**.

## Parâmetros e Tipos
- `nome` (`str`): nome completo da pessoa.

## Formato do Retorno
Tupla `(maiusculas, minusculas, total_letras, letras_primeiro_nome)` — `tuple[str, str, int, int]`.

`total_letras` ignora espaços; `letras_primeiro_nome` é `len(nome.split()[0])`.

## Casos de Exemplo
```python
analisar_nome("Maria Silva")    # ("MARIA SILVA", "maria silva", 10, 5)
analisar_nome("JOAO PEREIRA")   # ("JOAO PEREIRA", "joao pereira", 11, 4)
analisar_nome("A")              # ("A", "a", 1, 1)
```

## Restrições / Edge Cases
- A contagem de letras desconsidera qualquer espaço em branco.
- Assume nome não vazio (existe ao menos um nome).

## Assinaturas canônicas
- **Python**: `analisar_nome(nome: str) -> tuple[str, str, int, int]`
- **TypeScript**: `analisarNome(nome: string): [string, string, number, number]`