export function lucroAcoes(precos: number[]): number {
  if (precos.length <= 1) return 0

  let menorValor = precos[0]
  let maiorValor = precos[0]

  let ponteiro = 0

  while (ponteiro < precos.length) {
    const valorDoDia = precos[ponteiro]

    if (valorDoDia < menorValor) {
      menorValor = precos[ponteiro]
      maiorValor = precos[ponteiro]

      ponteiro++
      continue
    }

    if (valorDoDia > maiorValor) {
      maiorValor = precos[ponteiro]
    }

    ponteiro++
  }


  return maiorValor - menorValor
}

// console.log(lucroAcoes([7, 1, 5, 3, 6, 4]))
