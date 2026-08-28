export function palindromo(texto: string): boolean {
  if (!texto.length) return true

  let textoInvertido = ''

  const textoCaixaBaixa = texto.toLocaleLowerCase().replaceAll(' ', '')

  for (let i = 1; i <= texto.length; i++) {
    const letra = textoCaixaBaixa.at(i * -1)

    textoInvertido += letra || ''
  }

  return textoCaixaBaixa === textoInvertido
}