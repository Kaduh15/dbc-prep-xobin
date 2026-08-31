export function detectarDuplicatas(nums: number[]): boolean {
  const valoresVistos = new Set<number>()

  for (const num of nums) {
    if (valoresVistos.has(num)) return true

    valoresVistos.add(num)
  }

  return false
}
