# EX45 — Jokenpô (Pedra, Papel e Tesoura)

## Descrição
Programa determinístico e testável para o Jokenpô: recebe as duas jogadas (usuário e computador) e retorna o vencedor, sem aleatoriedade. Regras: pedra vence tesoura; tesoura vence papel; papel vence pedra; jogadas iguais → empate.

## Parâmetros e Tipos
- `jogada_usuario` (str) — `pedra`, `papel` ou `tesoura`.
- `jogada_computador` (str) — `pedra`, `papel` ou `tesoura`.

## Retorno
`str` — `"usuario"`, `"computador"` ou `"empate"`.

## Casos de Exemplo
```python
jokenpo('pedra', 'tesoura') -> "usuario"
jokenpo('tesoura', 'papel') -> "usuario"
jokenpo('papel', 'pedra')   -> "usuario"
jokenpo('tesoura', 'pedra') -> "computador"
jokenpo('papel', 'tesoura') -> "computador"
jokenpo('pedra', 'papel')   -> "computador"
jokenpo('papel', 'papel')   -> "empate"
```

## Casos de Teste (todos, incluindo extremos)
```python
# vitorias do usuario
(('pedra', 'tesoura'), 'usuario'), (('tesoura', 'papel'), 'usuario'), (('papel', 'pedra'), 'usuario'),
# vitorias do computador
(('tesoura', 'pedra'), 'computador'), (('papel', 'tesoura'), 'computador'), (('pedra', 'papel'), 'computador'),
# empates (todos)
(('papel', 'papel'), 'empate'), (('pedra', 'pedra'), 'empate'), (('tesoura', 'tesoura'), 'empate'),
# invalidas -> ValueError
[('lagarto', 'papel'), ('pedra', 'lagarto'), ('', 'pedra'), ('PAPEL', 'pedra')]
```

## Edge Cases / Extremos
- Empates para as três combinações iguais.
- Jogada inválida em **qualquer** um dos dois lados → `ValueError` (incluindo string vazia e maiúsculas, que são sensíveis a caixa).

## Abordagem / Dica
1. Validar ambas as jogadas contra o conjunto `{pedra, papel, tesoura}`.
2. Se iguais → `empate`.
3. Lista explícita dos 3 casos de vitória do usuário; caso contrário → `computador`.

## Complexidade
- Tempo O(1), espaço O(1).

## Assinatura Canônica
- **Python**: `def jokenpo(jogada_usuario: str, jogada_computador: str) -> str:`
- **TypeScript**: `export function jokenpo(jogadaUsuario: string, jogadaComputador: string): string`

> Stub para editar: `ex045_jokenpo/solution_ex045_jokenpo.py` (Python) e `solution.ts` (TS).
