export function frequenciaIgnorandoPrimeira(texto: string): Record<string, number> {
  console.log(texto)

  const frequencia: Record<string, number> = {}
  const visto: string[] = []

  for (const letra of texto) {
    if (!visto.includes(letra)) {
      visto.push(letra)
      continue
    }
    if (!frequencia[letra]) {
      frequencia[letra] = 1
      continue
    }

    frequencia[letra] += 1
  }

  return frequencia
}
