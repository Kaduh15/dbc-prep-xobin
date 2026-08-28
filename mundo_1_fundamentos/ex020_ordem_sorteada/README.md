# EX020 — Ordem de Apresentação

## Descrição
O mesmo professor quer sortear a **ordem de apresentação** dos trabalhos de quatro alunos. Para manter a função pura e testável, o sorteio recebe a permutação de índices já sorteada e produz a lista de alunos nessa ordem.

## Parâmetros e Tipos
- `alunos` (`list[str]`): nomes dos alunos.
- `indices` (`list[int]`): permutação de índices que define a nova ordem (do primeiro ao último apresentador).

## Formato do Retorno
`list[str]` — alunos reordenados conforme os índices (`[alunos[i] for i in indices]`).

## Casos de Exemplo
```python
ordem_apresentacao(["Ana", "Bia", "Caio", "Duda"], [1, 3, 0, 2])
# ["Bia", "Duda", "Ana", "Caio"]
ordem_apresentacao(["Ana", "Bia", "Caio", "Duda"], [0, 1, 2, 3])
# ["Ana", "Bia", "Caio", "Duda"]
ordem_apresentacao(["Ana"], [0])  # ["Ana"]
```

## Edge Cases / Extremos
- A aleatoriedade do embaralhamento fica **fora** da função; apenas a permutação é aplicada.
- Permutação identidade `[0,1,2,3]` e reversa `[3,2,1,0]` são cobertas.
- Listas vazias `([], [])` retornam `[]` (caso extremo).
- Casos adicionados: `([], []) → []`, `(["a","b","c"], [2,1,0]) → ["c","b","a"]`, `(["x","y"], [1,0]) → ["y","x"]`.

## Abordagem / Dica
Compreensão de lista (Python) / `indices.map(i => alunos[i])` (TypeScript): para cada índice, pegue `alunos[i]`.

## Complexidade
Tempo O(n), espaço O(n), onde n = len(indices).

## Assinaturas / Stub
- **Python**: `ordem_apresentacao(alunos: list[str], indices: list[int]) -> list[str]`
- **TypeScript**: `ordemApresentacao(alunos: string[], indices: number[]): string[]`

Stub de partida (Python):
```python
def ordem_apresentacao(alunos: list[str], indices: list[int]) -> list[str]:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function ordemApresentacao(alunos: string[], indices: number[]): string[] {
  throw new Error("Not implemented");
}
```
