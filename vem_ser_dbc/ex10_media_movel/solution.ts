export function mediaMovel(valores: number[], janela: number): number[] {
  if (valores.length === 0) return []

  return valores.reduce((acc, curr) => {

    if (curr < janela) return acc

    acc.push((curr + janela) / 2)


    return acc
  }, [] as number[])
}

console.log(mediaMovel([1, 2, 3, 4], 2))
