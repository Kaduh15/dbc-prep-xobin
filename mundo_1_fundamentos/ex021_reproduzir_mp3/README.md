# EX021 — Reproduzir Arquivo de Áudio (MP3)

## Descrição
O programa deve abrir e reproduzir o áudio de um arquivo MP3. Como a reprodução real envolve bibliotecas externas e saída de mídia, a **função testável** representa a operação de forma lógica e determinística: recebe o caminho do arquivo e retorna a confirmação da reprodução, validando que o arquivo indicado é `.mp3`.

## Parâmetros e Tipos
- `caminho` (`str`): caminho do arquivo de áudio.

## Formato do Retorno
`str` — mensagem de confirmação `"Reproduzindo: {caminho}"` se o arquivo terminar em `.mp3` (case-insensitive); caso contrário `"Formato de áudio não suportado"`.

## Casos de Exemplo
```python
reproduz_audio("musica.mp3")        # "Reproduzindo: musica.mp3"
reproduz_audio("audio/voz.mp3")     # "Reproduzindo: audio/voz.mp3"
reproduz_audio("PODCAST.MP3")       # "Reproduzindo: PODCAST.MP3"
reproduz_audio("clipe.mp4")         # "Formato de áudio não suportado"
reproduz_audio("sem_extensao")      # "Formato de áudio não suportado"
```

## Edge Cases / Extremos
- A reprodução de mídia real fica **fora** da função; não há I/O de áudio, apenas validação + retorno de string.
- A validação compara o sufixo com `.mp3` de forma **case-insensitive** (`PODCAST.MP3`, `arquivo.Mp3` são válidos).
- Extensões parecidas (`x.mp33`, `clipe.mp4`) e ausência de extensão são rejeitadas.
- Nome com ponto interno (`a.b.mp3`) é válido (termina em `.mp3`).
- String vazia `""` não termina em `.mp3` → não suportado.
- Casos adicionados: `arquivo.Mp3 → Reproduzindo`, `"" → não suportado`, `x.mp33 → não suportado`, `a.b.mp3 → Reproduzindo`.

## Abordagem / Dica
Use `caminho.lower().endswith(".mp3")` (Python) / `caminho.toLowerCase().endsWith(".mp3")` (TypeScript). Monte a string de retorno com f-string / template literal.

## Complexidade
Tempo O(len(caminho)), espaço O(len(caminho)) (strings imutáveis/f-string).

## Assinaturas / Stub
- **Python**: `reproduz_audio(caminho: str) -> str`
- **TypeScript**: `reproduzAudio(caminho: string): string`

Stub de partida (Python):
```python
def reproduz_audio(caminho: str) -> str:
    raise NotImplementedError
```

Stub de partida (TypeScript):
```typescript
export function reproduzAudio(caminho: string): string {
  throw new Error("Not implemented");
}
```
