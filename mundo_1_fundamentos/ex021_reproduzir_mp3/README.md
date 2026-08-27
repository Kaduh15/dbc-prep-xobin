# EX021 — Reproduzir Arquivo de Áudio (MP3)

## Descrição
O programa deve abrir e reproduzir o áudio de um arquivo MP3. Como a reprodução real envolve bibliotecas externas e saída de mídia, a **função testável** representa a operação de forma lógica e determinística: recebe o caminho do arquivo e retorna a confirmação da reprodução, validando que o arquivo indicado é `.mp3`.

## Parâmetros e Tipos
- `caminho` (`str`): caminho do arquivo de áudio.

## Formato do Retorno
`str` — mensagem de confirmação da reprodução no formato `"Reproduzindo: {caminho}"`. Se o arquivo não terminar em `.mp3`, retorna `"Formato de áudio não suportado"`.

## Casos de Exemplo
```python
reproduz_audio("musica.mp3")        # "Reproduzindo: musica.mp3"
reproduz_audio("audio/voz.mp3")     # "Reproduzindo: audio/voz.mp3"
reproduz_audio("clipe.mp4")         # "Formato de áudio não suportado"
```

## Restrições / Edge Cases
- A reprodução de mídia real fica **fora** da função; ela não faz I/O de áudio.
- A validação compara o sufixo (case-insensitive) com `.mp3`.

## Assinaturas canônicas
- **Python**: `reproduz_audio(caminho: str) -> str`
- **TypeScript**: `reproduzAudio(caminho: string): string`