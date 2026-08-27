# EX45 — Jokenpô (Pedra, Papel e Tesoura)

## Descrição
Crie um programa que faça o computador jogar Jokenpô com o usuário. Para tornar a lógica determinística e testável, exponha uma função que recebe as duas jogadas (usuário e computador) e retorna o vencedor, sem aleatoriedade.

## Parâmetros e Tipos
- `jogada_usuario` (str) — jogada do usuário: `pedra`, `papel` ou `tesoura`.
- `jogada_computador` (str) — jogada do computador: `pedra`, `papel` ou `tesoura`.

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

## Restrições / Edge Cases
- Regras: pedra vence tesoura; tesoura vence papel; papel vence pedra.
- Jogadas iguais → `empate`.
- Jogada inválida lança `ValueError`.

## Assinatura canônica

```python
def jokenpo(jogada_usuario: str, jogada_computador: str) -> str:
```

```typescript
jokenpo(jogadaUsuario: string, jogadaComputador: string): string
```
