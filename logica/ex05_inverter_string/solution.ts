export function inverterString(texto: string): string {
  let textoInvertido = ''

  for (let i = 1; i <= texto.length; i++) {
    textoInvertido += texto.at(i * -1) ?? ''
  }

  return textoInvertido
}
