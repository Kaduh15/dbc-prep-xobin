export function contarParesImpares(nums: number[]): [number, number] {
  if (nums.length === 0) return [0, 0]

  let contadorPar = 0
  let contadorImpar = 0

  for(let num of nums) {
    if (num % 2 === 0) {
      contadorPar++
      continue
    }

    contadorImpar++
  }

  return [contadorPar, contadorImpar]
}
