export function fibonacciDecrescente(limite: number): number[] {
  if (limite <= 0) return []
  if (limite === 1) return [0]

  let fibonacci = 0

  const resultado: number[] = [0]

  while (fibonacci < limite) {

    const ultimoResultado = resultado.at(-1)
    const penultiResultado = resultado.at(-2)

    if (ultimoResultado === undefined) continue

    if(penultiResultado === undefined) {
      fibonacci = 1 + ultimoResultado

      resultado.push(fibonacci)
      continue
    }

    if (ultimoResultado === 1){
      fibonacci = ultimoResultado + ultimoResultado
    } else {
      fibonacci = penultiResultado + ultimoResultado
    }

    if (fibonacci >= limite) break

    resultado.push(fibonacci)
  }

  return resultado.sort((a, b) => b - a)
}
