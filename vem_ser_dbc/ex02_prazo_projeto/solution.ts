export function prazoProjeto(equipe: string[], pontos: number): number | null {
  console.log(equipe)

  if (equipe.length === 0) return null

  const nivelPontoMap: Record<string, number> = {
    'junior': 10,
    'pleno': 20,
    'senior': 30,
    'lider': 40
  }

  return pontos / equipe.reduce((acc, curr) => {
    console.log(nivelPontoMap[curr])

    acc += nivelPontoMap[curr]

    return acc
  }, 0.0)
}
