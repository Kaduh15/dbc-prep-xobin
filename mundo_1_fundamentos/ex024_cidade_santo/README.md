# EX024 — Cidade que Começa com "SANTO"

## Descrição
Receba o nome de uma cidade e indique se ela **começa** com o nome "SANTO" (ignorando maiúsculas/minúsculas e espaços antes/depois).

## Parâmetros e Tipos
- `cidade` (`str`): nome da cidade.

## Formato do Retorno
`bool` — `True` se a cidade começa com "SANTO" (comparação case-insensitive, após remover espaços das bordas), senão `False`.

## Casos de Exemplo
```python
comeca_com_santo("Santo Amaro")     # True
comeca_com_santo("santos")          # True
comeca_com_santo("SANTO ANDRÉ")     # True
comeca_com_santo("  Santo Antonio  ")  # True
comeca_com_santo("Porto Alegre")    # False
comeca_com_santo("Rio de Janeiro")  # False
```

## Edge Cases / Extremos
- Comparação case-insensitive e ignora espaços no início/fim (`"  Santo Antonio  "` → `True`).
- "Santos" conta como verdadeiro porque começa com "SANTO" (o mesmo vale para "Santorini").
- "Santo" isolado → `True`; prefíxos que não iniciam com SANTO ("Asantos", "Porto Alegre") → `False`.
- String vazia `""` → `False`.
- Casos adicionados: `"Santo" → True`, `"SANTOS" → True`, `"santorini" → True`, `"" → False`, `"Asantos" → False`.

## Abordagem / Dica
Python: `cidade.strip().upper().startswith("SANTO")`. TypeScript: `cidade.trim().toUpperCase().startsWith("SANTO")`. `.strip()`/`.trim()` remove espaços das bordas antes da comparação.

## Complexidade
Tempo O(len(cidade)), espaço O(len(cidade)) (`strip` + `upper` criam novas strings).

## Assinaturas / Stub
- **Python**: `comeca_com_santo(cidade: str) -> bool`
- **TypeScript**: `comecaComSanto(cidade: string): boolean`

Stub de partida (Python):
```python
def comeca_com_santo(cidade: str) -> bool:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function comecaComSanto(cidade: string): boolean {
  throw new Error("Not implemented");
}
```
