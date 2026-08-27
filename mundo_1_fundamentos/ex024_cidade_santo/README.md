# EX024 — Cidade que Começa com "SANTO"

## Descrição
Receba o nome de uma cidade e indique se ela **começa** com o nome "SANTO" (ignorando maiúsculas/minúsculas e espaços antes/depois).

## Parâmetros e Tipos
- `cidade` (`str`): nome da cidade.

## Formato do Retorno
`bool` — `True` se a cidade começa com "SANTO" (comparação case-insensitive, após remover espaços das bordas), senão `False`.

## Casos de Exemplo
```python
comeca_com_santo("Santo Amaro")       # True
comeca_com_santo("santos")            # True
comeca_com_santo("SANTO ANDRÉ")       # True
comeca_com_santo("Porto Alegre")      # False
comeca_com_santo("Rio de Janeiro")    # False
```

## Restrições / Edge Cases
- A comparação é case-insensitive e ignora espaços no início/fim.
- "Santos" conta como verdadeiro porque começa com "SANTO".

## Assinaturas canônicas
- **Python**: `comeca_com_santo(cidade: str) -> bool`
- **TypeScript**: `comecaComSanto(cidade: string): boolean`