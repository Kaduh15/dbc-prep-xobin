export function frequenciaPalavras(frase: string): Record<string, number> {
  if (frase.length === 0 ) return {}

  const frequenciaPalavras: Record<string, number> = {}

  const fraseNormalizada = frase
    .replaceAll('!', '')
    .replaceAll(',', '')
    .replaceAll('.', '')
    .replaceAll(':', '')
    .toLocaleLowerCase()
    .split(' ')

  for (const palavra of fraseNormalizada) {
    if (frequenciaPalavras[palavra]) {
      frequenciaPalavras[palavra] += 1
      continue
    }

    frequenciaPalavras[palavra] = 1
  }


  return frequenciaPalavras
}
