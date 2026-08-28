export function contarCaracteres(texto: string): Record<string, number> {
  const resultado: Record<string, number> = {}

  for (let i = 0; i < texto.length; i++) {
    const letra = texto.at(i)

    if (!letra) continue

    if (!Object.keys(resultado).includes(letra)) {
      resultado[letra] = 1
      continue
    }

    resultado[letra] += 1
  }

  return resultado
}
