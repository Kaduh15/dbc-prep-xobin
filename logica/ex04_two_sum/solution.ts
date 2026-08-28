export function twoSum(nums: number[], alvo: number): number[] | null {
  console.log(!nums.length)

  if (!nums.length) return null

  let ponteiroEsquerdo = 0
  let ponteiroDireito = 1

  while (ponteiroEsquerdo < nums.length) {
    const numero1 = Number(nums.at(ponteiroEsquerdo))
    const numero2 = Number(nums.at(ponteiroDireito))

    if (numero1 + numero2 === alvo) {
      return [ponteiroEsquerdo, ponteiroDireito]
    }


    if (ponteiroDireito <= nums.length) {
      ponteiroDireito++
      ponteiroEsquerdo++
    }
  }


  return null
}
