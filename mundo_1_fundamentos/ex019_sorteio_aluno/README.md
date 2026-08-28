# EX019 — Sorteio de Aluno

## Descrição
O professor quer sortear um entre quatro alunos para apagar o quadro. Para manter a função **pura e testável**, o sorteio recebe o índice sorteado e retorna o aluno correspondente.

## Parâmetros e Tipos
- `alunos` (`list[str]`): nomes dos alunos candidatos.
- `indice` (`int`): índice do aluno sorteado.

## Formato do Retorno
`str` — o nome do aluno escolhido (`alunos[indice]`).

## Casos de Exemplo
```python
sorteia_aluno(["Ana", "Bia", "Caio", "Duda"], 2)  # "Caio"
sorteia_aluno(["Ana", "Bia", "Caio", "Duda"], 0)  # "Ana"
sorteia_aluno(["Ana", "Bia", "Caio", "Duda"], 3)  # "Duda"
sorteia_aluno(["Solo"], 0)                              # "Solo"
```

## Edge Cases / Extremos
- A aleatoriedade do sorteio fica **fora** da função; apenas o índice é aplicado sobre a lista.
- Assume `0 <= indice < len(alunos)`; índice `0` (primeiro) e `len-1` (último) são cobertos.
- Funciona com um único aluno (`["Solo"]` → índice `0`).
- Casos adicionados: lista de 6 alunos com índice `5` (último), lista de 3 com índice `2` (último).

## Abordagem / Dica
`return alunos[indice]`. Acessa diretamente a posição na lista; nenhuma lógica extra é necessária.

## Complexidade
Tempo O(1), espaço O(1).

## Assinaturas / Stub
- **Python**: `sorteia_aluno(alunos: list[str], indice: int) -> str`
- **TypeScript**: `sorteiaAluno(alunos: string[], indice: number): string`

Stub de partida (Python):
```python
def sorteia_aluno(alunos: list[str], indice: int) -> str:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function sorteiaAluno(alunos: string[], indice: number): string {
  throw new Error("Not implemented");
}
```
