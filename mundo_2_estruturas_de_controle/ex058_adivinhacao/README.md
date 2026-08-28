# EX058 — Jogo de adivinhação (quantos palpites)

**Enunciado (Curso em Vídeo):**
> Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Agora o jogador tenta adivinhar até acertar, mostrando no final quantos palpites foram necessários.

## Descrição
O número secreto vira parâmetro (determinismo). A função conta **quantos palpites foram necessários** a partir da sequência de tentativas.

## Parâmetros e Tipos
- `numero` — `int`: número secreto (0 a 10).
- `tentativas` — `list[int]`: sequência de palpites do jogador.

## Retorno
`int`: quantidade de palpites até o **primeiro acerto** (1-base). Se nunca acertar, retorna o total de tentativas.

## Casos de Exemplo
```python
palpites_para_acertar(5, [8, 2, 5, 9])  # 3
palpites_para_acertar(7, [7])  # 1
palpites_para_acertar(3, [1, 2, 3])  # 3
palpites_para_acertar(9, [1, 2, 3])  # 3
```

## Edge Cases / Extremos
- **Acerto de primeira:** Retorna 1.
- **Acerto no último:** Retorna o tamanho da lista.
- **Sem acerto:** Retorna o total de tentativas.
- **Lista vazia:** Retorna 0 (nenhum palpite dado).
- **Acerto repetido:** Para no **primeiro** acerto (palpites seguintes ignorados).

## Abordagem
Itera enumerando os palpites; no primeiro igual a `numero`, devolve a posição 1-base; se terminar sem acerto, devolve `len(tentativas)`.

## Complexidade
Tempo O(k) (k = nº de tentativas, pior caso percorre tudo); Espaço O(1).

## Assinatura canônica
```python
def palpites_para_acertar(numero: int, tentativas: list[int]) -> int
```
```typescript
export function palpitesParaAcertar(numero: number, tentativas: number[]): number
```

## Stub TDD (para implementar)
Arquivos: `solution_ex058_adivinhacao.py`, `solution.ts`. Testes: `test_ex058_adivinhacao.py`, `solution.test.ts`.

```python
def palpites_para_acertar(numero: int, tentativas: list[int]) -> int:
    raise NotImplementedError
```
```typescript
export function palpitesParaAcertar(numero: number, tentativas: number[]): number {
  throw new Error("not implemented");
}
```
