export function maiorMenor(nums: number[]): [number, number] | null {
  if (nums.length <= 0) return null

  let maior = nums[0]
  let menor = nums[0]

  for(let i = 0; i < nums.length; i++) {
    const numeroDaVez = nums[i]

    if (numeroDaVez > maior) {
      maior = numeroDaVez
      continue
    }

    if (numeroDaVez < menor) menor = numeroDaVez
  }


  return [maior, menor]
}
