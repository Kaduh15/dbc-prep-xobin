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
```

## Restrições / Edge Cases
- A aleatoriedade do sorteio fica **fora** da função; o índice sorteado é passado como parâmetro.
- Assume `0 <= indice < len(alunos)`.

## Assinaturas canônicas
- **Python**: `sorteia_aluno(alunos: list[str], indice: int) -> str`
- **TypeScript**: `sorteiaAluno(alunos: string[], indice: number): string`