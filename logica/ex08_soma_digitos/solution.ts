export function somaDigitos(n: number): number {
  const valorSomado = n.toString()
    .replace('-', '')
    .split('')
    .reduce((acc, curr) => {
      acc += Number(curr)

      return acc
    }, 0)

  return valorSomado
}
