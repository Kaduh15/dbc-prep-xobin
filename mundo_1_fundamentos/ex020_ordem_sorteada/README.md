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
```

## Restrições / Edge Cases
- A aleatoriedade do embaralhamento fica **fora** da função; apenas a permutação é aplicada.
- `indices` é uma permutação válida de `0..len(alunos)-1`.

## Assinaturas canônicas
- **Python**: `ordem_apresentacao(alunos: list[str], indices: list[int]) -> list[str]`
- **TypeScript**: `ordemApresentacao(alunos: string[], indices: number[]): string[]`