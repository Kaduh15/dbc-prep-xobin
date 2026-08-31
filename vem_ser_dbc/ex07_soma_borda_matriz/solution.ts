export function somaBordaMatriz(matriz: number[][]): number {
  if (matriz.length === 0) return 0
  if (matriz.length === 1) {
    if (matriz[0].length === 0) return 0
  }

  const primeiraLinha = matriz[0]
  const ultimaLinha = matriz.at(-1) !== undefined && matriz.length > 1 ? matriz.at(-1) as number[] : []

  const somaDasLinhas = [...primeiraLinha, ...ultimaLinha].reduce((acc, curr) => {
    acc += curr

    return acc
  }, 0)

  if (matriz.length === 2) {
    return somaDasLinhas
  }

  let somaDasColunas = 0

  for (let i = 1; i < matriz.length - 1; i++) {
    const primeiroDaLinha = matriz[i][0]
    const ultimoDaLinha = matriz[i].at(-1) === undefined ? 0 : matriz[i].at(-1) as number

    somaDasColunas += primeiroDaLinha + ultimoDaLinha
  }

  return somaDasColunas + somaDasLinhas
}

// console.log(somaBordaMatriz([
//   [1, 2, 3, 4]
// ]))
