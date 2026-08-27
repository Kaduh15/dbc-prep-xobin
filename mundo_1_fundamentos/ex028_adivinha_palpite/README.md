# Ex 028 — Adivinhação (0 a 5)

**Enunciado original (Curso em Vídeo / Guanabara):** “Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.”

## Descrição
Versão determinística do jogo: dado o palpite do usuário e o número “pensado” (segredo), retorna se o usuário acertou (venceu). A geração do segredo ocorre fora da função testada.

## Parâmetros e Tipos
| Nome | Tipo | Descrição |
|------|------|-----------|
| palpite | int | Palpite dado pelo usuário. |
| segredo | int | Número “pensado” pelo computador. |

## Formato do Retorno
Booleano: `True` se `palpite == segredo` (usuário venceu); caso contrário `False`.

## Casos de Exemplo
```py
venceu_adivinhacao(3, 3)  ->  True
```
```py
venceu_adivinhacao(3, 5)  ->  False
```
```py
venceu_adivinhacao(0, 0)  ->  True
```
## Restrições / Edge Cases
- Função pura: a aleatoriedade fica fora (segredo é passado como argumento).
- Palpites fora do intervalo [0,5] continuam válidos como comparação.

## Assinatura canônica
```python
def venceu_adivinhacao(palpite: int, segredo: int) -> bool:
```
```ts
export function venceuAdivinhacao(palpite: number, segredo: number): boolean
```
