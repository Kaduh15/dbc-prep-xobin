# EX053 — Palíndromo

**Enunciado (Curso em Vídeo):**
> Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

## Descrição
Um palíndromo é uma frase que se lê da mesma forma de trás para frente. A função ignora espaços e trata maiúsculas/minúsculas como equivalentes.

## Parâmetros e Tipos
- `frase` — `str`: texto a ser verificado.

## Retorno
`bool`: `True` se a frase for palíndromo, senão `False`.

## Casos de Exemplo
```python
eh_palindromo('arara')  # True
eh_palindromo('Ana')  # True
eh_palindromo('a sacada da casa')  # True
eh_palindromo('socorram me subi no onibus em marrocos')  # True
eh_palindromo('banana')  # False
```

## Edge Cases / Extremos
- **Espaços:** Removidos antes da comparação.
- **Case-insensitive:** `Ana` invertido == `ana`.
- **Palavra única:** `ovo`, `php`, `reviver` → True.
- **String vazia:** Normalizada para `""` → True (vacuamente).
- **Sem palíndromo:** `casa`, `banana` → False.

## Abordagem
Normaliza a frase (remove espaços e converte para minúsculas) e compara com sua própria inversão.

## Complexidade
Tempo O(m) (m = tamanho normalizado); Espaço O(m).

## Assinatura canônica
```python
def eh_palindromo(frase: str) -> bool
```
```typescript
export function ehPalindromo(frase: string): boolean
```

## Stub TDD (para implementar)
Arquivos: `solution_ex053_palindromo.py`, `solution.ts`. Testes: `test_ex053_palindromo.py`, `solution.test.ts`.

```python
def eh_palindromo(frase: str) -> bool:
    raise NotImplementedError
```
```typescript
export function ehPalindromo(frase: string): boolean {
  throw new Error("not implemented");
}
```
