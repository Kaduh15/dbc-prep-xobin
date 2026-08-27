# EX058 — Jogo de adivinhação (quantos palpites)

**Enunciado (Curso em Vídeo, DESAFIO 058):**
> Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

## Descrição
O número secreto (que o computador "pensa") vira um parâmetro da função para manter a determinismo da lógica de um jogo interativo. A função conta **quantos palpites foram necessários** para o jogador vencer (a partir da sequência de tentativas).

## Parâmetros e Tipos
- `numero` — `int`: número secreto (0 a 10).
- `tentativas` — `list[int]`: sequência de palpites dados pelo jogador.

## Retorno
- `int`: quantidade de palpites até o **primeiro acerto** (1-base). Se o número nunca for acertado, retorna o total de tentativas.

## Casos de Exemplo
```python
palpites_para_acertar(5, [8, 2, 5, 9])  # 3  -> acerta no 3º palpite
palpites_para_acertar(7, [7])           # 1  -> acerta de primeira
palpites_para_acertar(3, [1, 2, 3])     # 3  -> acerta no último
palpites_para_acertar(9, [1, 2, 3])     # 3  -> nunca acerta, usa todos
```

## Restrições / Edge Cases
- A contagem é 1-base (primeiro palpite = 1).
- Para de contar no **primeiro** acerto (palpites seguintes são ignorados).
- Sem acerto → retorna o número total de tentativas.
- As dicas "maior/menor" do jogo original ficam fora da função pura.

## Assinatura canônica
```python
def palpites_para_acertar(numero: int, tentativas: list[int]) -> int
```
```typescript
export function palpitesParaAcertar(numero: number, tentativas: number[]): number
```
